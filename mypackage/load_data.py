import pkg_resources
import pandas as pd

data_path = pkg_resources.resource_filename('mypackage', 'data/temples_raw.csv')

pd.read_csv(data_path)