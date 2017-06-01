import pandas as pd
import numpy as np
import matplotlib


# df = pandas.read_csv('161003sprd.csv', sep='\t',columns=["1","2","3","4","5"])
df = pd.read_csv('161003sprd.csv')[0:10]
print df.head()
# print len(df.columns)
# print df.shape

# print(df.ix[1:2, 2:].head())
print(df.ix[1:2, 2:].head())

df_new = df.append(df)
#print df_new[['new','spot']].sub(df['spot'])

d = {'one' : pd.Series([1,2,5]),
     'two' : pd.Series([3,4,7])}
d = pd.DataFrame(d)

e = {'one' : pd.Series([1,2,8]),
     'two' : pd.Series([3,3,9])}
#print(d.head())

e = pd.DataFrame(e)
print(d.head())
print(e.head())

c=d[d.isin(e)].sort_index
print(d[d.isin(e)].dropna())

print(d[~d.isin(e).all(axis=1)])

ts = pd.Series(np.random.rand(100), index=pd.date_range('1/1/2000', periods=1000))

print(ts)






