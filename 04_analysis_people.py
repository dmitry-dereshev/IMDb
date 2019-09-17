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

def birth_dates(query_birth, query_death):
    c.execute(query_birth)
    rows = c.fetchall()
    birth_years = pd.DataFrame(rows, columns=['Birth Year', 'Count'])

    c.execute(query_death)
    rows = c.fetchall()
    death_years = pd.DataFrame(rows, columns=['Death Year', 'Count'])
    db.close()

    plt.bar(birth_years['Birth Year'], birth_years['Count'], label='Birth Years')
    plt.bar(death_years['Death Year'], death_years['Count'], label = 'Death Years')

    plt.title('Cinematograpy Workers Birth and Death Frequencies')
    plt.xlabel('Years')
    plt.ylabel('Count')

    plt.legend()
    plt.show()

query_birth = """SELECT birth_year, count(birth_year) as count FROM people 
WHERE birth_year > 1774
GROUP BY birth_year ORDER BY birth_year;"""
query_death = """SELECT death_year, count(death_year) as count FROM people 
WHERE death_year > 1774
GROUP BY death_year ORDER BY death_year;"""
#birth_death_dates(query_birth, query_death)


def lifespan_visual(query_lifespan):
    c.execute(query_lifespan)
    rows = c.fetchall()
    data = pd.DataFrame(rows, columns=['Lifespan', 'Count'])
    graph_text = "Average = "+(str(data.Lifespan.mean())[0:5])+\
        "\nMedian = "+(str(data.Lifespan.median())[0:2])+\
            "\nstd = "+(str(data.Lifespan.std())[0:5])

    plt.bar(data.Lifespan, data.Count, label='Lifespan')

    plt.title('Cinematograpy Workers Lifespan')
    plt.text(40, 3500, graph_text)
    plt.xlabel('Years')
    plt.ylabel('Count')

    plt.xlim(0, 120)
    plt.legend()
    plt.show()

query_lifespan = """SELECT death_year - birth_year as lifespan, count(*) as count
FROM people 
WHERE death_year > 1774 AND birth_year > 1774 AND (death_year - birth_year) > 0
GROUP BY lifespan
ORDER BY lifespan;"""
#lifespan_visual(query_lifespan)