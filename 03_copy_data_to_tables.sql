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
