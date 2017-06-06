import pandas as pd


df = pd.read_csv('161003sprd.csv', names=['time_stamp', 'fftt', 'sspot', 'ssprt'], skiprows=1)
print df.head()