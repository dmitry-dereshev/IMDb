/*
Part of IMDb project by Dmitry Dereshev. 2019 MIT Licence.
https://github.com/dmitry-dereshev/IMDb

This SQL query populates the 4 tables created by 02_create_tables.sql with the
data cleaned up by 01_tsv_to_csv_clean_fix.py
*/

COPY PEOPLE
FROM 'path\to\.csv' DELIMITER ',' CSV HEADER;

COPY MEDIA
FROM 'D:\Downloads\IMBD\.csv files\media.csv' DELIMITER ',' CSV HEADER;

COPY MEDIA_REGIONS
FROM 'D:\Downloads\IMBD\.csv files\title.akas.short.csv' DELIMITER ',' CSV HEADER;

COPY CREW
FROM 'path\to\.csv' DELIMITER ',' CSV HEADER;
