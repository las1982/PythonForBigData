import pandas

data = pandas.read_csv('titanic.csv', index_col='PassengerId')
print data.head()
# 1
print data[['Sex']].groupby(['Sex']).size()
# 2
