import numpy as np
import matplotlib.pyplot as plt
import psycopg2 as sql
import pandas as pd

db = sql.connect(
    database='IMDb',
    user='username',
    password = 'password'
)
c = db.cursor()

def media_scores(q_tvEpisode, q_short, q_movie, q_video, q_tvMovie, q_tvSeries, whichplot='overall'):
    c.execute(q_tvEpisode)
    rows = c.fetchall()
    tv_Episode_data = pd.DataFrame(rows, columns=['year_produced', 'Average_Score', 'st_dev_score'])
    
    c.execute(q_short)
    rows = c.fetchall()
    short_data = pd.DataFrame(rows, columns=['year_produced', 'Average_Score', 'st_dev_score'])

    c.execute(q_movie)
    rows = c.fetchall()
    movie_data = pd.DataFrame(rows, columns=['year_produced', 'Average_Score', 'st_dev_score'])

    c.execute(q_video)
    rows = c.fetchall()
    video_data = pd.DataFrame(rows, columns=['year_produced', 'Average_Score', 'st_dev_score'])

    c.execute(q_tvMovie)
    rows = c.fetchall()
    tvMovie_data = pd.DataFrame(rows, columns=['year_produced', 'Average_Score', 'st_dev_score'])

    c.execute(q_tvSeries)
    rows = c.fetchall()
    tvSeries_data = pd.DataFrame(rows, columns=['year_produced', 'Average_Score', 'st_dev_score'])
    
    db.close()
    
    if whichplot == 'overall':
        fig, axs = plt.subplots(2, 3)
        fig.suptitle('Films, Shorts, TV AVG Scores & Standard Deviations Per Year')

        
        plt.subplot(231)
        plt.errorbar(short_data.year_produced,\
            short_data.Average_Score, \
                short_data.st_dev_score,\
                    label='Shorts', ecolor='tab:orange')
        plt.legend()
        #plt.xlim(2006, 2012)
        plt.ylim(3, 10)
        plt.xticks(np.arange(1860, 2021, 20))
        plt.yticks([3, 4, 5, 6, 7, 8, 9, 10])
        plt.grid()

        plt.subplot(234)
        plt.errorbar(video_data.year_produced,\
            video_data.Average_Score,\
                video_data.st_dev_score,\
                    label='Videos', ecolor='tab:orange')
        plt.legend()
        #plt.xlim(2006, 2012)
        plt.ylim(3, 10)
        plt.xticks(np.arange(1860, 2021, 20))
        plt.yticks([3, 4, 5, 6, 7, 8, 9, 10])
        plt.grid()

        plt.subplot(232)
        plt.errorbar(movie_data.year_produced,\
            movie_data.Average_Score,\
                movie_data.st_dev_score,\
                    label='Films', ecolor='tab:orange')
        plt.legend()
        #plt.xlim(2006, 2012)
        plt.ylim(3, 10)
        plt.xticks(np.arange(1860, 2021, 20))
        plt.yticks([3, 4, 5, 6, 7, 8, 9, 10])
        plt.grid()

        plt.subplot(235)
        plt.errorbar(tvMovie_data.year_produced,\
            tvMovie_data.Average_Score,\
                tvMovie_data.st_dev_score,\
                    label='TV Films', ecolor='tab:orange')
        plt.legend()
        #plt.xlim(2006, 2012)
        plt.ylim(3, 10)
        plt.xticks(np.arange(1860, 2021, 20))
        plt.yticks([3, 4, 5, 6, 7, 8, 9, 10])
        plt.grid()

        plt.subplot(233)
        plt.errorbar(tvSeries_data.year_produced,\
            tvSeries_data.Average_Score,\
                tvSeries_data.st_dev_score,\
                    label='TV Series', ecolor='tab:orange')
        plt.legend()
        #plt.xlim(2006, 2012)
        plt.ylim(3, 10)
        plt.xticks(np.arange(1860, 2021, 20))
        plt.yticks([3, 4, 5, 6, 7, 8, 9, 10])
        plt.grid()

        plt.subplot(236)
        plt.errorbar(tv_Episode_data.year_produced,\
            tv_Episode_data.Average_Score,\
                tv_Episode_data.st_dev_score,\
                    label='TV Episode', ecolor='tab:orange')
        plt.legend()
        #plt.xlim(2006, 2012)
        plt.ylim(3, 10)
        plt.xticks(np.arange(1860, 2021, 20))
        plt.yticks([3, 4, 5, 6, 7, 8, 9, 10])
        plt.grid()

        plt.show()

    elif whichplot == 'detailed':
        #Shorts and Videos
        fig_1 = plt.figure(1)
        fig_1.suptitle('Shorts & Videos: AVG Scores & Standard Deviations Per Year')
        plt.subplot(221)
        plt.errorbar(short_data.year_produced,\
            short_data.Average_Score, \
                short_data.st_dev_score,\
                    label='Shorts', ecolor='tab:orange')
        plt.legend()
        #plt.xlim(2006, 2012)
        plt.ylim(3, 10)
        plt.xticks(np.arange(1860, 2021, 20))
        plt.yticks([3, 4, 5, 6, 7, 8, 9, 10])
        plt.grid()

        plt.subplot(223)
        plt.plot(short_data.year_produced,\
            short_data.st_dev_score,\
                label='Shorts Score Deviation Over Time')
        plt.legend()
        plt.xticks(np.arange(1860, 2021, 20))
        plt.ylim(0, 2)
        plt.grid()

        plt.subplot(222)
        plt.errorbar(video_data.year_produced,\
            video_data.Average_Score,\
                video_data.st_dev_score,\
                    label='Videos', ecolor='tab:orange')
        plt.legend()
        #plt.xlim(2006, 2012)
        plt.ylim(3, 10)
        plt.xticks(np.arange(1860, 2021, 20))
        plt.yticks([3, 4, 5, 6, 7, 8, 9, 10])
        plt.grid()

        plt.subplot(224)
        plt.plot(video_data.year_produced,\
            video_data.st_dev_score,\
                label='Videos Score Deviation Over Time')
        plt.legend()
        plt.xticks(np.arange(1860, 2021, 20))
        plt.ylim(0, 2)
        plt.grid()
        
        #Films and TV Films
        fig_2 = plt.figure(2)
        fig_2.suptitle('Films & TV Films: AVG Scores & Standard Deviations Per Year')
        
        plt.subplot(221)
        plt.errorbar(movie_data.year_produced,\
            movie_data.Average_Score,\
                movie_data.st_dev_score,\
                    label='Films', ecolor='tab:orange')
        plt.legend()
        #plt.xlim(2006, 2012)
        plt.ylim(3, 10)
        plt.xticks(np.arange(1860, 2021, 20))
        plt.yticks([3, 4, 5, 6, 7, 8, 9, 10])
        plt.grid()

        plt.subplot(223)
        plt.plot(movie_data.year_produced,\
            movie_data.st_dev_score,\
                label='Films Score Deviation Over Time')
        plt.legend()
        plt.xticks(np.arange(1860, 2021, 20))
        plt.ylim(0, 2)
        plt.grid()

        plt.subplot(222)
        plt.errorbar(tvMovie_data.year_produced,\
            tvMovie_data.Average_Score,\
                tvMovie_data.st_dev_score,\
                    label='TV Films', ecolor='tab:orange')
        plt.legend()
        #plt.xlim(2006, 2012)
        plt.ylim(3, 10)
        plt.xticks(np.arange(1860, 2021, 20))
        plt.yticks([3, 4, 5, 6, 7, 8, 9, 10])
        plt.grid()

        plt.subplot(224)
        plt.plot(tvMovie_data.year_produced,\
            tvMovie_data.st_dev_score,\
                    label='TV Films Score Deviation Over Time')
        plt.legend()
        plt.xticks(np.arange(1860, 2021, 20))
        plt.ylim(0, 2)
        plt.grid()

        #TV Series & Episodes
        fig_3 = plt.figure(3)
        fig_3.suptitle('TV Series & TV Episodes: AVG Scores & Standard Deviations Per Year')
        
        plt.subplot(221)
        plt.errorbar(tvSeries_data.year_produced,\
            tvSeries_data.Average_Score,\
                tvSeries_data.st_dev_score,\
                    label='TV Series', ecolor='tab:orange')
        plt.legend()
        #plt.xlim(2006, 2012)
        plt.ylim(3, 10)
        plt.xticks(np.arange(1860, 2021, 20))
        plt.yticks([3, 4, 5, 6, 7, 8, 9, 10])
        plt.grid()
        
        plt.subplot(223)
        plt.plot(tvSeries_data.year_produced,\
            tvSeries_data.st_dev_score,\
                    label='TV Series Score Deviation Over Time')
        plt.legend()
        plt.xticks(np.arange(1860, 2021, 20))
        plt.ylim(0, 2)
        plt.grid()

        plt.subplot(222)
        plt.errorbar(tv_Episode_data.year_produced,\
            tv_Episode_data.Average_Score,\
                tv_Episode_data.st_dev_score,\
                    label='TV Episode', ecolor='tab:orange')
        plt.legend()
        #plt.xlim(2006, 2012)
        plt.ylim(3, 10)
        plt.xticks(np.arange(1860, 2021, 20))
        plt.yticks([3, 4, 5, 6, 7, 8, 9, 10])
        plt.grid()

        plt.subplot(224)
        plt.plot(tv_Episode_data.year_produced,\
            tv_Episode_data.st_dev_score,\
                label='TV Episode Score Deviation Over Time')
        plt.legend()
        plt.xticks(np.arange(1860, 2021, 20))
        plt.ylim(0, 2)
        plt.grid()

        plt.show()




q_tvEpisode = """SELECT m.year_produced, AVG(r.average_rating), stddev_pop(r.average_rating)
FROM media m
JOIN ratings r ON m.media_id = r.media_id
WHERE m.media_type = 'tvEpisode' AND m.year_produced < 2020
GROUP BY m.year_produced
ORDER BY m.year_produced"""

q_short = """SELECT m.year_produced, AVG(r.average_rating), stddev_pop(r.average_rating)
FROM media m
JOIN ratings r ON m.media_id = r.media_id
WHERE m.media_type = 'short' AND m.year_produced < 2020
GROUP BY m.year_produced
ORDER BY m.year_produced"""

q_movie = """SELECT m.year_produced, AVG(r.average_rating), stddev_pop(r.average_rating)
FROM media m
JOIN ratings r ON m.media_id = r.media_id
WHERE m.media_type = 'movie' AND m.year_produced < 2020
GROUP BY m.year_produced
ORDER BY m.year_produced"""

q_video = """SELECT m.year_produced, AVG(r.average_rating), stddev_pop(r.average_rating)
FROM media m
JOIN ratings r ON m.media_id = r.media_id
WHERE m.media_type = 'video' AND m.year_produced < 2020
GROUP BY m.year_produced
ORDER BY m.year_produced"""

q_tvMovie = """SELECT m.year_produced, AVG(r.average_rating), stddev_pop(r.average_rating)
FROM media m
JOIN ratings r ON m.media_id = r.media_id
WHERE m.media_type = 'tvMovie' AND m.year_produced < 2020
GROUP BY m.year_produced
ORDER BY m.year_produced"""

q_tvSeries = """SELECT m.year_produced, AVG(r.average_rating), stddev_pop(r.average_rating)
FROM media m
JOIN ratings r ON m.media_id = r.media_id
WHERE m.media_type = 'tvSeries' AND m.year_produced < 2020
GROUP BY m.year_produced
ORDER BY m.year_produced"""

whichplot = 'detailed'
media_scores(q_tvEpisode, q_short, q_movie, q_video, q_tvMovie, q_tvSeries, whichplot)