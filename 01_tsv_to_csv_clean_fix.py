# Part of IMDb project by Dmitry Dereshev. 2019 MIT Licence.
# https://github.com/dmitry-dereshev/IMDb

# This script looks through a folder to pick up .tsv files, remove '\N', and
# convert them to Unicode-compliant .csv files.
# Original data from: https://www.imdb.com/interfaces/

import pandas as pd
import os

def tsv_to_csv_pandas(data_in, data_out):
    # Collect file paths into a variable. Checks for subfolders as well.
    tsv_files = [os.path.join(root, name)
    for root, dirs, files in os.walk(data_in)
    for name in files]
    
    for i in tsv_files:
        data = pd.read_csv(i, sep='\t')
        data.replace('\\N', '', inplace=True)
        print(os.path.basename(i))
        print(data.dtypes)
        save_to = data_out+'\\'+os.path.basename(i)
        data.to_csv(save_to, index=False)

def clean_name_basics(data_in, data_out):
    data = pd.read_csv(data_in,\
         usecols=['nconst', 'primaryName', 'birthYear', 'deathYear'])
    print(data.head())
    separate_names = pd.DataFrame(data.primaryName.str.split(' ',1).tolist(),
                                   columns = ['First_Name','Last_Name'])

    data.drop('primaryName', axis=1, inplace=True)
    data['First_Name'] = separate_names.First_Name
    data['Last_Name'] = separate_names.Last_Name
    data = data[['nconst', 'First_Name', 'Last_Name', 'birthYear', 'deathYear']]
    print(data.head())
    data.to_csv(data_out, na_rep="",float_format="%.0f",index=False)

def clean_title_basics(data_in, data_out):
    data = pd.read_csv(data_in,\
        usecols=['tconst', 'originalTitle', 'titleType', 'startYear',\
             'runtimeMinutes', 'isAdult'])
    data.dropna(inplace=True)
    data = data[['tconst', 'originalTitle', 'titleType', 'startYear',\
             'runtimeMinutes', 'isAdult']]
    data.to_csv(data_out, na_rep="", float_format="%.0f", index=False)

def clean_title_principals(people, media, title_principals, data_out):
    data = pd.read_csv(title_principals, usecols=['tconst','nconst','category'])
    print(data.shape)
    people_compare = pd.read_csv(people, usecols=['nconst'])
    media_compare = pd.read_csv(media, usecols=['tconst'])
    data = data[data.nconst.isin(people_compare.nconst)]
    print(data.shape)
    data = data[data.tconst.isin(media_compare.tconst)]
    print(data.shape)
    data.to_csv(data_out, index=False)

def clean_title_akas(media, title_akas, data_out):
    data = pd.read_csv(title_akas,\
        usecols=['titleId', 'title', 'region', 'isOriginalTitle'])
    print(data.head())
    data.dropna(subset=['region', 'isOriginalTitle'], inplace=True)
    print(data.shape)
    compare_media = pd.read_csv(media, usecols=['tconst'])
    data = data[data.titleId.isin(compare_media.tconst)]
    print(data.shape)
    data.to_csv(data_out,na_rep="", float_format="%.0f", index=False)

def clean_ratings(media, title_ratings, data_out):
    data = pd.read_csv(title_ratings)
    compare_media = pd.read_csv(media, usecols=['tconst'])
    print(data.shape)
    data = data[data.tconst.isin(compare_media.tconst)]
    print(data.shape)
    data.to_csv(data_out,na_rep="", float_format="%.0f", index=False)
