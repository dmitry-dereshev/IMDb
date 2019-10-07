import numpy as np
import matplotlib.pyplot as plt
import psycopg2 as sql
import pandas as pd

def actor_rating(query, individual):

    db = sql.connect(
    database='IMDb',
    user='username',
    password = 'password')
    c = db.cursor()

    c.execute(query)
    rows = c.fetchall()
    data = pd.DataFrame(rows,\
        columns=['person_id', 'First_Name', 'Last_Name', 'Average_Score', 'St_Dev', 'Job_Count'])
    data.sort_values(['Job_Count'], inplace=True)
    groupped = data.groupby(['Job_Count']).mean()
    groupped = groupped[groupped.index < 31]
    
    c.execute(individual)
    rows = c.fetchall()
    individual = pd.DataFrame(rows,\
        columns=['First_Name', 'Last_Name', 'year_produced', 'Rating'])
    individual['cumul_avg'] = individual.Rating.expanding().mean()
    individual['cumul_stdev'] = individual.Rating.expanding().std()
    label_text = str(individual.First_Name[0]) + ' ' + str(individual.Last_Name[0])
    db.close()
    
    fig, axs = plt.subplots(2, 1)
    fig.suptitle("AVG Perons's Score vs. "+str(label_text))
    plt.subplot(211)
    plt.errorbar(groupped.index, groupped.Average_Score, groupped.St_Dev,\
        label='AVG Person Score',color='r', ecolor='tab:orange', alpha=0.6)

    plt.errorbar(individual.index, individual.cumul_avg, individual.cumul_stdev,\
        label=label_text, color='b', ecolor=(.18, .31, .31))
    
    plot_text =  label_text + "'s " + "Median = "+(str(individual.cumul_avg.median())[0:5])+\
            "\nAVG Person Score Median = "+(str(groupped.Average_Score.median())[0:5])
    plt.text(0, 9.5, plot_text)
    plt.grid()
    plt.xlabel('Number of Roles')
    plt.ylabel('Score')
    plt.legend()

    plt.subplot(212)
    plt.plot(individual.cumul_stdev, label="Actor's cumulative st.dev")
    plt.grid()
    plt.legend()
    plt.xlabel('Number of Roles')
    plt.ylabel('Cumulative Standard Deviation')
    
    fig, axs = plt.subplots(3, 1)
    fig.suptitle('Person Score & Number of People Forming That Score')
    
    plt.subplot(311)
    plt.title('AVG Person Score w.r.t. Number of Roles')
    plt.errorbar(groupped.index, groupped.Average_Score, groupped.St_Dev, label='Person Score', ecolor='tab:orange')
    plt.ylim(5, 10)
    plt.grid()
   
    plt.subplot(312)
    plt.title('Number of People with that Many Roles')
    plt.plot(data.groupby(['Job_Count']).count().person_id)
    plt.grid()
    plt.ylim(0, 30)
    plt.xlim(0, 30)

    plt.subplot(313)
    plt.title('Standard Deviation of Person Score')
    plt.plot(groupped.St_Dev)
    plt.xlim(0, 30)
    plt.grid()
    

    plt.show()
    

    
query="""
SELECT c.person_id, 
    p.first_name, 
    p.last_name, 
    AVG(r.average_rating) as average_person_rating,
    stddev_pop(r.average_rating) as st_dev_person_rating,
    count(c.person_id) as job_count
FROM ratings r
JOIN media m ON m.media_id = r.media_id
JOIN crew c ON c.media_id = r.media_id
JOIN  people p ON p.person_id = c.person_id
WHERE r.number_of_votes > 10000
GROUP BY c.person_id, p.first_name, p.last_name
ORDER BY job_count DESC
"""

individual = """
SELECT p.first_name, p.last_name,
m.year_produced,
r.average_rating
FROM people p
JOIN crew c ON c.person_id = p.person_id
JOIN media m ON m.media_id = c.media_id
JOIN ratings r ON r.media_id = c.media_id
WHERE p.person_id = 'nm0000199'
ORDER BY m.year_produced
"""
actor_rating(query, individual)
