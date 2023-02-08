## define sql create tables queries

create_songs_library = """
CREATE TABLE IF NOT EXISTS songs_library
                        (
                        session_id INT,
                        item_in_session INT,
                        artist TEXT,
                        song_title TEXT,
                        song_length FLOAT,
                        PRIMARY KEY (session_id, item_in_session)
                        );
"""

create_song_playlist_session = """
CREATE TABLE IF NOT EXISTS song_playlist_session
                    (
                    user_id INT,
                    session_id INT,
                    item_in_session INT,
                    user_firstname TEXT,
                    user_lastname TEXT,
                    song_title TEXT,
                    artist TEXT,
                    PRIMARY KEY ((user_id, session_id), item_in_session))
                    WITH CLUSTERING ORDER BY (item_in_session DESC);
"""

create_users_session = """
CREATE TABLE IF NOT EXISTS users_session
                    (
                    song_title TEXT,
                    user_id int,
                    user_firstname TEXT,
                    user_lastname TEXT,
                    PRIMARY KEY (song_title, user_id)
                    );
"""




## define insert queries
insert_songs_library = """
INSERT INTO songs_library 
                    (
                    session_id,
                    item_in_session,
                    artist,
                    song_title,
                    song_length
                    ) 
                    VALUES 
                    (%s, %s, %s, %s, %s);
"""

insert_song_playlist_session = """
INSERT INTO song_playlist_session
                    (
                    user_id,
                    session_id,
                    item_in_session,
                    artist,
                    song_title,
                    user_firstname,
                    user_lastname
                    )
                    VALUES (%s, %s, %s, %s, %s, %s, %s);
"""
        

insert_users_session  = """
INSERT INTO users_session 
                    (
                    song_title,
                    user_id,
                    user_firstname,
                    user_lastname
                    )
                    VALUES (%s, %s, %s, %s);
"""