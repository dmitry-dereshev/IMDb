/*
Part of IMDb project by Dmitry Dereshev. 2019 MIT Licence.
https://github.com/dmitry-dereshev/IMDb

This SQL query transforms existing tables with multi-value columns (like
listing all films an actor was in as a single value) into singe-value
columns by creating extra rows.
*/

--Cleaning ACTOR_INFO
    /*
    CREATE TABLE ACTOR_INFO_CLEAN_1
    ( PERSON_ID TEXT, 
    FULL_NAME TEXT, 
    BIRTH_YEAR FLOAT, 
    DEATH_YEAR FLOAT, 
    PROFESSION TEXT, 
    TITLES TEXT) ;

    INSERT INTO ACTOR_INFO_CLEAN_1
    SELECT person_id, 
        full_name, 
        birth_year, 
        death_year, 
        profession, 
        unnest(string_to_array(known_for_titles, ','))
    FROM ACTOR_INFO
    */
    /*
    CREATE TABLE ACTOR_INFO_CLEAN_2
    ( PERSON_ID TEXT, 
    FULL_NAME TEXT, 
    BIRTH_YEAR FLOAT, 
    DEATH_YEAR FLOAT, 
    PROFESSION TEXT, 
    KNOWN_FOR_TITLES TEXT) ;

    INSERT INTO ACTOR_INFO_CLEAN_2
    SELECT person_id, 
        full_name, 
        birth_year, 
        death_year, 
        unnest(string_to_array(profession, ',')), 
        TITLES
    FROM ACTOR_INFO_CLEAN_1
*/
--Cleaning TITLE_TYPES
    /*
    CREATE TABLE TITLE_TYPES_1
    ( TITLE_ID TEXT, 
    ORDER_IN_TABLE BIGINT, 
    LOCALIZED_TITLE TEXT, 
    TITLE_REGION TEXT, 
    TITLE_LANGUAGE TEXT, 
    TITLE_TYPE TEXT, 
    TITLE_ATTRIBUTES TEXT, 
    IS_ORIGINAL_TITLE BOOLEAN ) ;
    
    INSERT INTO TITLE_TYPES_1
    SELECT TITLE_ID, 
        ORDER_IN_TABLE, 
        LOCALIZED_TITLE, 
        TITLE_REGION, 
        TITLE_LANGUAGE, 
        unnest(string_to_array(TITLE_TYPE, ',')), 
        TITLE_ATTRIBUTES, 
        IS_ORIGINAL_TITLE
    FROM title_types;

    CREATE TABLE TITLE_TYPES_2
    ( TITLE_ID TEXT, 
    ORDER_IN_TABLE BIGINT, 
    LOCALIZED_TITLE TEXT, 
    TITLE_REGION TEXT, 
    TITLE_LANGUAGE TEXT, 
    TITLE_TYPE TEXT, 
    TITLE_ATTRIBUTES TEXT, 
    IS_ORIGINAL_TITLE BOOLEAN ) ;

    INSERT INTO TITLE_TYPES_2
    SELECT TITLE_ID, 
        ORDER_IN_TABLE, 
        LOCALIZED_TITLE, 
        TITLE_REGION, 
        TITLE_LANGUAGE, 
        TITLE_TYPE, 
        unnest(string_to_array(TITLE_ATTRIBUTES, ',')), 
        IS_ORIGINAL_TITLE
    FROM TITLE_TYPES_1
*/
-- Cleaning TITLE_INFO
    /*
    CREATE TABLE TITLE_INFO_1
    --Table to title.basics 
    ( TITLE_ID TEXT, 
    TITLE_FORMAT TEXT, 
    TITLE_POPULAR_NAME TEXT, 
    TITLE_ORIGINAL_NAME TEXT, 
    IS_ASULT INTEGER, 
    RELEASE_YEAR FLOAT, 
    END_YEAR_FOR_SERIES FLOAT, 
    RUNTIME_MINUTES TEXT, 
    GENRES TEXT ) ;

    INSERT INTO TITLE_INFO_1
    SELECT TITLE_ID, 
        TITLE_FORMAT, 
        TITLE_POPULAR_NAME, 
        TITLE_ORIGINAL_NAME, 
        IS_ASULT, 
        RELEASE_YEAR, 
        END_YEAR_FOR_SERIES, 
        RUNTIME_MINUTES, 
        unnest(string_to_array(GENRES, ','))
    FROM title_info
*/
--CLEANING CREW_INFO
    /*
    CREATE TABLE CREW_INFO_1
    --Table for title.crew
    ( TITLE_ID TEXT, 
    DIRECTORS_IDS TEXT, 
    WRITERS_IDS TEXT ) ;

    INSERT INTO CREW_INFO_1
    SELECT TITLE_ID, 
        unnest(string_to_array(DIRECTORS_IDS, ',')), 
        WRITERS_IDS
    FROM crew_info;

    CREATE TABLE CREW_INFO_2
    ( TITLE_ID TEXT, 
    DIRECTORS_IDS TEXT, 
    WRITERS_IDS TEXT ) ;

    INSERT INTO CREW_INFO_2
    SELECT TITLE_ID, 
        DIRECTORS_IDS, 
        unnest(string_to_array(WRITERS_IDS, ','))
    FROM CREW_INFO_1;
*/
--Remove multi-valued tables; rename single-valued tables
    /*
    DROP TABLE actor_info;
    DROP TABLE actor_info_clean_1;
    ALTER TABLE actor_info_clean_2 RENAME TO actor_info;

    DROP TABLE title_types;
    DROP TABLE TITLE_TYPES_1;
    ALTER TABLE TITLE_TYPES_2 RENAME TO title_types;

    DROP TABLE title_info;
    ALTER TABLE title_info_1 RENAME TO title_info;

    DROP TABLE crew_info;
    DROP TABLE crew_info_1;
    ALTER TABLE crew_info_2 RENAME TO crew_info;
*/