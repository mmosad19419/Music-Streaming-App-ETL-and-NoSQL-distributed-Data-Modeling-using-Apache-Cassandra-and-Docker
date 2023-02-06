# Nosql-Data-Modeling-With-Apache-Cassandra-using-Docker

## Modeling with Cassandra
In this project, I'll apply what you've learned on data modeling with Apache Cassandra and complete an ETL pipeline using Python.

## Datasets
For this project, I'll be working with one dataset: event_data.
The directory of CSV files is partitioned by date.
Here are examples of file paths to two files in the dataset:

`event_data/2018-11-08-events.csv
event_data/2018-11-09-events.csv`

#### Note: the data is compressed and placed inside _datasets_ dir

## The project template includes one Jupyter Notebook file, in which:
- I will process the event_datafile_new.csv dataset to create a denormalized dataset
- I will model the data tables keeping in mind the analytical queries to be run
- I will load the data into tables I create in Apache Cassandra and run my queries

## Project Steps 
### Step 1: Build ETL Pipeline
1. Implement the logic in section Part I of the notebook to iterate through each event file in event_data to process and create a new CSV file in Python
2. Part II of the notebook to include Apache Cassandra CREATE and INSERT statements to load processed records into relevant tables in my data model

### Step 2: Modeling your NoSQL database or Apache Cassandra database
1. Design tables to answer the queries outlined in the project
2. Write Apache Cassandra CREATE KEYSPACE and SET KEYSPACE statements
3. Develop CREATE statement for each of the tables to address each question
4. Load the data with an INSERT statement for each of the tables
5. Include IF NOT EXISTS clauses in CREATE statements to create tables only if the tables do not already exist.
6. Include a DROP TABLE statement for each table, this way I can drop and create tables whenever I want to reset your database and test my ETL pipeline
7. Test by running the proper select statements with the correct WHERE clause


## Docker
Docker is used to:
1. Develop the data servers using the Cassandra image
2. Setup Jupyter notebook to use throughout the project

#### Image Details
image: cassandra:4.1.0
setup environment variable to mimic the Apache Cassandra database server

image: jupyter/datascience-notebook:x86_64-ubuntu-22.04
setup Jupyter notebook to use throughout the project

#### Use the two containers in a mutual network to access and load the data from and two the database using jupyter notebook and python

## Files:
1. docker-compose.yml: set up docker and configurations
2. etl.py: etl script
3. sql_queries: contain the SQL queries used in the project
4. requirement.txt: required packages for the project
5. NOSQL Data Modeling and ETL pipeline With Apache Cassandra: Project notebook
6. datasets dir: contain datasets used in the project compressed, unzip it to use
7. data dir: used to mount volumes of the container to make the data storage persist whenever I run the container
8. images: contain image file used in the jupyter notebook

## How to run the project:
1. clone the repository
2. run `docker compose up`
3. go to the jupyter server 
4. open the terminal and run `pip install requirements`
5. run the notebook
6. run `python etl.py`
