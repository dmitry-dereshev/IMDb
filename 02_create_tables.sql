/*
Part of IMDb project by Dmitry Dereshev. 2019 MIT Licence.
https://github.com/dmitry-dereshev/IMDb

This SQL query creates 4 tables:
1. People with unique info about people
2. Media with unique info about media
3. Crew, which connects people and media
4. Media regions, which has information about tranlsations of media into other
   languages
*/

CREATE TABLE PEOPLE -- Unique person's information derived from name.basics 
(PERSON_ID TEXT PRIMARY KEY, 
FIRST_NAME TEXT,
LAST_NAME TEXT,
BIRTH_YEAR INTEGER, 
DEATH_YEAR INTEGER) ;

CREATE TABLE MEDIA -- Unique media (films, series, games) information
(MEDIA_ID TEXT PRIMARY KEY,
ORIGINAL_TITLE TEXT,
MEDIA_TYPE TEXT,
YEAR_PRODUCED INTEGER,
MEDIA_RUNTIME_MINUTES FLOAT,
MEDIA_ADULT_STATUS BOOLEAN) ;

CREATE TABLE CREW -- Junction table between people and media
(MEDIA_ID TEXT REFERENCES MEDIA,
PERSON_ID TEXT REFERENCES PEOPLE,
JOB TEXT) ;

CREATE TABLE MEDIA_REGIONS -- Info about tranlsations of a given media
(MEDIA_ID TEXT REFERENCES MEDIA,
LOCALIZED_TITLE TEXT,
MEDIA_REGION TEXT,
IS_ORIGINAL_TITLE BOOLEAN) ;

CREATE TABLE RATINGS -- Table for media ratings
(MEDIA_ID TEXT REFERENCES MEDIA,
AVERAGE_RATING FLOAT,
NUMBER_OF_VOTES INTEGER);