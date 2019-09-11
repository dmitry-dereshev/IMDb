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
        data.to_csv(save_to, index=0)

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

def clean_title_principals(data_in, data_out):
    data = pd.read_csv(data_in, usecols=['tconst','nconst','category'])
    data.to_csv(data_out, index=False)

def fix_title_akas(data_in, data_out):
    data = pd.read_csv(data_in,\
        usecols=['titleId', 'title', 'region', 'isOriginalTitle'])
    data.dropna(subset=['region', 'isOriginalTitle'], inplace=True)
    data.to_csv(data_out,na_rep="", float_format="%.0f", index=False)

def fix_title_basics(data_in, data_out):
    data = pd.read_csv(data_in,\
        usecols=['tconst', 'titleType', 'originalTitle', 'isAdult',\
             'startYear', 'runtimeMinutes'])
    data = data[~data.runtimeMinutes.str.contains('Ani|Real', na=False)]
    data.to_csv(data_out, na_rep="", float_format="%.0f", index=False)

def make_media(data_1, data_2, data_out):
    data_1 = pd.read_csv(data_1)
    data_2 = pd.read_csv(data_2)
    merged_data = data_1.merge(data_2, how='left', on='tconst')
    merged_data = merged_data[['tconst', 'originalTitle', 'titleType',\
         'startYear', 'runtimeMinutes', 'isAdult', 'averageRating', 'numVotes']]
    merged_data.dropna(subset=['tconst', 'originalTitle', 'titleType',\
        'startYear', 'isAdult', 'averageRating', 'numVotes'], inplace=True)
    merged_data = merged_data.astype({'startYear': 'int64',\
        'numVotes': 'int64'}, errors='ignore')
    print(merged_data.dtypes)
    merged_data.to_csv(data_out, na_rep="", index=False)

data_in = 'path/to/csv'
data_out = 'path/to/csv'
