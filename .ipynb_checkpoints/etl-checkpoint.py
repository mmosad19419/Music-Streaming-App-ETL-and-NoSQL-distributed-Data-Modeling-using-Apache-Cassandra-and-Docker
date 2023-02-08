# import libs
# Import Python packages 
import pandas as pd
import cassandra
import re
import os
import glob
import numpy as np
import json
import csv

# Import sql queries
from sql_queries import *

## connect to cassandra cluster and model our database
# connect to cassandra
from cassandra.cluster import Cluster

# setup a cassandra host server using docker
CASSANDRA_HOST = "cassandra"

# conect to cassandra host server
cluster = Cluster([CASSANDRA_HOST])

# establish connection and begin executing queries, init a session
session = cluster.connect()

# Create a Keyspace
try:
    session.execute("""
                        CREATE KEYSPACE IF NOT EXISTS sparkify
                        WITH REPLICATION = 
                        { 'class' : 'SimpleStrategy', 'replication_factor' : 1 }
    """
    )
    
except Exception as e:
    print(e)
    
    
# Set KEYSPACE to the keyspace sparkify
try:
    session.set_keyspace("sparkify")
except Exception as e:
    print(e)

print("Connected to sparkify database Successfully")


## Create Tables
# create_songs_library
try:
    session.execute(create_songs_library)

except Exception as e:
    print(e)

# create_song_playlist_session table 
try:
    session.execute(create_song_playlist_session)

except Exception as e:
    print(e) 


# create_users_session table  
try:
    session.execute(create_users_session)

except Exception as e:
    print(e) 

print("Tables Craeted Successfully")



## extract the csv files
# checking current working directory
#print(os.getcwd())

# Get your current folder and subfolder event data
filepath = os.getcwd() + '/datasets/event_data'

# Create a for loop to create a list of files and collect each filepath
for root, dirs, files in os.walk(filepath):
    
# join the file path and roots with the subdirectories using glob
    file_path_list = glob.glob(os.path.join(root,'*'))
    #print(file_path_list)
    

## Build the full datafile
# initiating an empty list of rows that will be generated from each file
full_data_rows_list = [] 
    
# for every filepath in the file path list 
for f in file_path_list:

# reading csv file 
    with open(f, 'r', encoding = 'utf8', newline='') as csvfile: 
        # creating a csv reader object 
        csvreader = csv.reader(csvfile) 
        next(csvreader)
        
 # extracting each data row one by one and append it        
        for line in csvreader:
            #print(line)
            full_data_rows_list.append(line) 
            
# uncomment the code below to get total number of rows 
#print(len(full_data_rows_list))
# uncomment the code below to see what the list of event data rows will look like
#print(full_data_rows_list[0])

# creating a smaller event data csv file called event_datafile_full csv that will be used to insert data into the \
# Apache Cassandra tables
csv.register_dialect('myDialect', quoting=csv.QUOTE_ALL, skipinitialspace=True)

with open('./datasets/full_datafile/event_datafile_new.csv', 'w', encoding = 'utf8', newline='') as f:
    # confg write Dialect
    writer = csv.writer(f, dialect='myDialect')
    
    # write header row
    writer.writerow(['artist','firstName','gender','itemInSession','lastName','length',\
                'level','location','sessionId','song','userId'])
    
    # write file data
    for row in full_data_rows_list:
        if (row[0] == ''):
            continue
        # write the required rows only to the new file
        writer.writerow((row[0], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[12], row[13], row[16]))

print("The data extracted and loaded into the full datafile Successfully")


## Data Modeling 
## load from csv full_datafile --> Apache cassandra database

# Extract from full_datafile
# load data from the csv to cassandra Nosql db
file = './datasets/full_datafile/event_datafile_new.csv'

with open(file, encoding = 'utf8') as f:
    csvreader = csv.reader(f)
    next(csvreader) # skip header
    for line in csvreader:
        ##Extract data
        # song data
        song_title = line[9].strip().title()
        song_length = round(float(line[5]), 3)
        artist = line[0].strip().title()
        
        # user data
        user_id = int(line[10])
        user_firstname = line[1].strip().title()
        user_lastname = line[4].strip().title()
        user_gender = line[2].strip().title()
        user_level = line[6].strip().title()
        user_location = line[7].strip().title()
        
        # session data
        item_insession = int(line[3])
        session_id = int(line[8])
        

        ## Load data to sparkify database
        # INSERT into the `songs` table
        songs_library_data = (session_id, item_insession, artist, song_title, song_length)
        ## execute query
        session.execute(insert_songs_library, songs_library_data)
        
        
        # INSERT into the `users` table
        song_playlist_session_data = (user_id, session_id, item_insession, user_firstname, user_lastname, song_title, artist)
        
        # execute query
        session.execute(insert_song_playlist_session, song_playlist_session_data)
        
                                                        
        # INSERT into the `music_library` table
        users_session_data = (song_title, user_id, user_firstname, user_lastname)
        
        # execute query
        session.execute(insert_users_session, users_session_data)

print("Data loaded to database Successfully")


        
## Drop the table before closing out the sessions
session.execute("DROP TABLE IF EXISTS songs")
session.execute("DROP TABLE IF EXISTS user")
session.execute("DROP TABLE IF EXISTS music_library")

## Close session and cluster connection
session.shutdown()
cluster.shutdown()