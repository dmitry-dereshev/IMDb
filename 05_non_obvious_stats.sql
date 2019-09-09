/*
Part of IMDb project by Dmitry Dereshev. 2019 MIT Licence.
https://github.com/dmitry-dereshev/IMDb

This SQL query showcases some stats about IMDb and what it contains.
*/

-- Top 10 Films of all time
    SELECT DISTINCT TF.title_original_name, TR.average_rating, TR.number_of_votes
    FROM TITLE_INFO as TF, TITLE_RATINGS as TR
    WHERE TF.title_id = TR.title_id 
    AND (TR.number_of_votes > 100000)
    AND title_format = 'movie'
    ORDER BY TR.average_rating DESC
    LIMIT 10;
-- Top 10 'Disaster of Cinematography' Films
    SELECT DISTINCT TF.title_original_name, TF.release_year, TR.average_rating, TR.number_of_votes
    FROM TITLE_INFO as TF, TITLE_RATINGS as TR
    WHERE TF.title_id = TR.title_id 
    AND (TR.number_of_votes > 100000)
    AND title_format = 'movie'
    ORDER BY TR.average_rating
    LIMIT 10;
-- Most popular names in cinematography
    SELECT DISTINCT full_name, count(*) as num
    FROM actor_info
    GROUP BY full_name
    ORDER BY num DESC
    LIMIT 10;
-- Most popular languages in cinematography
    SELECT DISTINCT COUNT(*) AS NUM, title_region 
    FROM TITLE_TYPES
    GROUP BY title_region
    ORDER BY num DESC
    LIMIT 10;
-- The 10 types of films in the database
    SELECT DISTINCT COUNT(*) AS NUM, TITLE_FORMAT
    FROM TITLE_INFO
    GROUP BY title_format
    ORDER BY NUM DESC
    LIMIT 20;
-- Top 10 most numerous series
    SELECT DISTINCT COUNT(se.episode_id) AS num_episodes, ti.title_original_name, tr.average_rating
    FROM SERIES_EPISODES as se, TITLE_INFO as ti, TITLE_RATINGS as tr
    WHERE se.SERIES_ID = ti.title_id
    GROUP BY ti.title_original_name, tr.average_rating
    ORDER BY num_episodes DESC
    LIMIT 10;
-- Different Jobs in Cinematography
    SELECT DISTINCT COUNT(*) AS NUM, PERSON_JOB_TYPE
    FROM PEOPLE_JOBS_CHARACTERS
    GROUP BY person_job_type
    ORDER BY NUM DESC
    LIMIT 20;