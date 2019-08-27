# Part of IMDb project by Dmitry Dereshev
# https://github.com/dmitry-dereshev/IMDb

# This script looks through a folder to pick up .tsv files, remove '\N', and
# convert them to Unicode-compliant .csv files.

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


data_in = 'path/to/folder/with/.tsv'
data_out = 'path/to/desired/output/folder'
tsv_to_csv_pandas(data_in, data_out)
