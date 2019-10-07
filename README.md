# IMDb
Transforms and queries to the IMDb offline databases (https://www.imdb.com/interfaces/)

# Scripts
- **01_tsv_to_csv_clean_fix** - transforms IMDb .tsv files to .csv and forces primary and foreign key compliance.
- **02_create_tables.sql** - creates necessary tables for the data.
- **03_populate_tables.sql** - populates the tables with data.
- **04_analysis_people.py** - graphs and queries that analyse the "People" table.
- **05_quantity_analysis_media.py** - graphs and queries that analyse the "Media" table.
- **06_quality_analysis_media.py** - graphs and queries that analyse the combined info across tables pertaining to how well-liked various media are.
- **07_actor_rating.py** - generates actor score based on media they starred in, and compared the averages to any individual of your choosing.

How the DB looks like after scripts 01 through 03:
![Image of db](https://github.com/dmitry-dereshev/IMDb/blob/master/DB_looks.png)
