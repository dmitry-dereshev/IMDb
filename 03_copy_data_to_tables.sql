/*
Part of IMDb project by Dmitry Dereshev. 2019 MIT Licence.
https://github.com/dmitry-dereshev/IMDb

This SQL query populates the 7 tables created by 02_create_tables.sql with the
data cleaned up by 01_tsv_to_csv_clean_fix.py
*/

COPY ACTOR_INFO
FROM 'path\to\name.basics.csv' DELIMITER ',' CSV HEADER;

COPY TITLE_TYPES
FROM 'path\to\title.akas.csv' DELIMITER ',' CSV HEADER;

COPY TITLE_INFO
FROM 'path\to\title.basics.csv' DELIMITER ',' CSV HEADER;

COPY CREW_INFO
FROM 'path\to\title.crew.csv' DELIMITER ',' CSV HEADER;

COPY SERIES_EPISODES
FROM 'path\to\title.episode.csv' DELIMITER ',' CSV HEADER;

COPY PEOPLE_JOBS_CHARACTERS
FROM 'path\to\title.principals.csv' DELIMITER ',' CSV HEADER;

COPY TITLE_RATINGS
FROM 'path\to\title.ratings.csv' DELIMITER ',' CSV HEADER;
