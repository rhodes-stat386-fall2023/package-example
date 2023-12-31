"""
This script imports the raw data, cleans it, and explorts the final dataset.
"""

if __name__ == '__main__':
    import pandas as pd


    temple_df = pd.read_csv('mypackage/data/temples_raw.csv')
    temple_df['dateTime'] = pd.to_datetime(temple_df['sortDate'])
    temple_df = temple_df.sort_values('dateTime')
    temple_df.to_csv('mypackage/data/temples.csv', index = False)

# Ideally, you would use some of your custom functions as a part of the clearning.