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

def media_counts(q_tvEpisode, q_short, q_movie, q_video, q_tvMovie, q_tvSeries):
    c.execute(q_tvEpisode)
    rows = c.fetchall()
    tv_Episode_data = pd.DataFrame(rows, columns=['year_produced', 'Amount'])

    c.execute(q_short)
    rows = c.fetchall()
    short_data = pd.DataFrame(rows, columns=['year_produced', 'Amount'])

    c.execute(q_movie)
    rows = c.fetchall()
    movie_data = pd.DataFrame(rows, columns=['year_produced', 'Amount'])

    c.execute(q_video)
    rows = c.fetchall()
    video_data = pd.DataFrame(rows, columns=['year_produced', 'Amount'])

    c.execute(q_tvMovie)
    rows = c.fetchall()
    tvMovie_data = pd.DataFrame(rows, columns=['year_produced', 'Amount'])

    c.execute(q_tvSeries)
    rows = c.fetchall()
    tvSeries_data = pd.DataFrame(rows, columns=['year_produced', 'Amount'])
    
    db.close()




    fig, axs = plt.subplots(1, 3)
    fig.suptitle('Films, Shorts, TV AVG Length Overall')

    
    plt.subplot(131)
    plt.bar(short_data.year_produced, short_data.Amount, label='Shorts')
    plt.bar(video_data.year_produced, video_data.Amount, label='Videos')
    plt.legend()
    #plt.xlim(2006, 2012)
    plt.ylim(0, 100)
    #plt.xticks(np.arange(1900, 2021, 20))
  
    plt.subplot(132)
    plt.bar(movie_data.year_produced, movie_data.Amount, label='Films')
    plt.bar(tvMovie_data.year_produced, tvMovie_data.Amount, label='TV Films')
    plt.legend()
    #plt.xlim(2006, 2012)
    plt.ylim(0, 100)
    #plt.xticks(np.arange(1900, 2021, 20))

    plt.subplot(133)
    plt.bar(tv_Episode_data.year_produced, tv_Episode_data.Amount, label='TV Episode')
    #plt.bar(tvSeries_data.year_produced,tvSeries_data.Amount, label='TV Series')
    plt.legend()
    #plt.xlim(2006, 2012)
    plt.ylim(0, 100)
    #plt.xticks(np.arange(1900, 2021, 20))

    plt.show()


q_tvEpisode = """SELECT year_produced, AVG(Media_Runtime_Minutes) as Average_Minutes
FROM media
WHERE media_type = 'tvEpisode' AND year_produced < 2020
GROUP BY media_type, year_produced
ORDER BY year_produced"""

q_short = """SELECT year_produced, AVG(Media_Runtime_Minutes) as Average_Minutes
FROM media
WHERE media_type = 'short' AND year_produced < 2020
GROUP BY media_type, year_produced
ORDER BY year_produced"""

q_movie = """SELECT year_produced, AVG(Media_Runtime_Minutes) as Average_Minutes
FROM media
WHERE media_type = 'movie' AND year_produced < 2020
GROUP BY media_type, year_produced
ORDER BY year_produced"""

q_video = """SELECT year_produced, AVG(Media_Runtime_Minutes) as Average_Minutes
FROM media
WHERE media_type = 'video' AND year_produced < 2020
GROUP BY media_type, year_produced
ORDER BY year_produced"""

q_tvMovie = """SELECT year_produced, AVG(Media_Runtime_Minutes) as Average_Minutes
FROM media
WHERE media_type = 'tvMovie' AND year_produced < 2020
GROUP BY media_type, year_produced
ORDER BY year_produced"""

q_tvSeries = """SELECT year_produced, AVG(Media_Runtime_Minutes) as Average_Minutes
FROM media
WHERE media_type = 'tvSeries' AND year_produced < 2020
GROUP BY media_type, year_produced
ORDER BY year_produced"""
media_counts(q_tvEpisode, q_short, q_movie, q_video, q_tvMovie, q_tvSeries)