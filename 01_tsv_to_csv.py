# Part of IMDb project by Dmitry Dereshev
# https://github.com/dmitry-dereshev/IMDb

# This script converts a given .tsv file to .csv and saves it in the location
# of choice.

import pandas as pd

def tsv_to_csv_pandas(data_in, data_out):
        
    data = pd.read_csv(data_in, sep='\t')
    print(data.head())

    data.to_csv(data_out)


data_in = 'path/to/.tsv/file'
data_out = 'output/to/.csv/file'
tsv_to_csv_pandas(data_in, data_out)
