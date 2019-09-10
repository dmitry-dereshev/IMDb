/*
Part of IMDb project by Dmitry Dereshev. 2019 MIT Licence.
https://github.com/dmitry-dereshev/IMDb

This SQL query creates 3 tables:
1. People with unique info about people
2. Media with unique info about media
3. Crew, which connects people and media
*/

CREATE TABLE PEOPLE -- Unique person's information
(PERSON_ID TEXT PRIMARY KEY, 
FIRST_NAME TEXT,
LAST_NAME TEXT,
BIRTH_YEAR INTEGER, 
DEATH_YEAR INTEGER) ;

CREATE TABLE MEDIA -- Unique media (films, series, games) information
(MEDIA_ID TEXT PRIMARY KEY,
ORIGINAL_TITLE TEXT,
LOCALIZED_TITLE TEXT,
YEAR_PRODUCED INTEGER,
MEDIA_TYPE TEXT, 
MEDIA_REGION TEXT,
MEDIA_LANGUAGE TEXT,
MEDIA_RUNTIME_MINUTES INTEGER,
MEDIA_ADULT_STATUS BOOLEAN,
AVERAGE_RATING FLOAT,
NUMBER_OF_VOTES INTEGER) ;

CREATE TABLE CREW -- Junction table between people and media
(MEDIA_ID TEXT,
PERSON_ID TEXT,
JOB TEXT) ;