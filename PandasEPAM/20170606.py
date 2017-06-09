import pandas as pd

df = pd.read_csv('161003sprd.csv', names=['time_stamp', 'fftt', 'sspot', 'ssprt'], skiprows=1)
# print df.head()
# print df.ndim, df.shape, df.size
# print df.axes

# df = pd.read_csv('161003sprd.csv', names=['time_stamp', 'fftt', 'sspot', 'ssprt'], skiprows=1, index_col=1)
# df = pd.read_csv('161003sprd.csv', names=['time_stamp', 'fftt', 'sspot', 'ssprt'], skiprows=1, index_col='time_stamp')
df = pd.read_csv('161003sprd.csv', index_col=0)
# print df.ndim, df.shape, df.size
# print df.axes

# print df['sspot']
# print df.sspot

# df.new_col = 0
# print df.head()
# print df.__dict__

# df['new_col'] = 0
# print df.head()
# print df.__dict__

# df.new_col = 1
# print df.head()

# df[start:stop:step]

# print df.loc[:'2016-10-03 10:00:00.837']
# print df.loc['2016-10-03 10:00:00.837', ['spot', 'spr']]
# print df.loc['2016-10-03 10:00:00.837', 'spot':'spr']

# print df[df.spot >= 62830]
# print df.spot[lambda s: s > 0]

df['-1sd'] = df.spr.mean() - df.spr.std()
df['+1sd'] = df.spr.mean() + df.spr.std()
vect_by = df.spr < df['-1sd']
vect_sell = df.spr > df['+1sd']
print vect_by
df['by'] = vect_by
df['sell'] = vect_sell
print df.head()