## define sql create tables queries

create_songs_table = """
CREATE TABLE IF NOT EXISTS songs
(
session_id INT,
item_in_session INT,
song_title TEXT,
song_length FLOAT,
artist TEXT,
PRIMARY KEY (session_id, item_in_session)
);
"""

create_users_table = """
CREATE TABLE IF NOT EXISTS users
(
user_id INT,
session_id INT,
item_in_session INT,
user_firstname TEXT,
user_lastname TEXT,
song_title TEXT,
artist TEXT,
PRIMARY KEY (user_id, session_id, item_in_session)
);
"""

create_music_table = """
CREATE TABLE IF NOT EXISTS music_library
(
user_firstname TEXT,
user_lastname TEXT,
song_title TEXT,
PRIMARY KEY (song_title)
);
"""


## define insert queries
insert_songs_table = """
INSERT INTO songs 
(
session_id,
item_in_session,
song_title,
song_length,
artist
) 
VALUES 
(%s, %s, %s, %s, %s);
"""

insert_users_table = """
INSERT INTO users
(
user_id,
session_id,
item_in_session,
song_title,
user_firstname,
user_lastname,
artist
)
VALUES (%s, %s, %s, %s, %s, %s, %s);
"""
        

insert_music_table = """
INSERT INTO music_library 
(
song_title,
user_firstname,
user_lastname
)
VALUES (%s, %s, %s);
"""