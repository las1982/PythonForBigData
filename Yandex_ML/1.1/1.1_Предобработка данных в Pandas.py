import pandas
import re

data = pandas.read_csv('titanic.csv', index_col='PassengerId')
print data.head()
# 1
print data[['Sex']].groupby(['Sex']).size()
# 2
survived = data[['Survived']].groupby(['Survived'])
print survived.size()
print float(survived.size()[1])/(survived.size()[0] + survived.size()[1]) * 100
# 3
first_class = data[['Pclass']].groupby(['Pclass'])
print first_class.size()
print float(first_class.size()[1])/(first_class.size()[1] + first_class.size()[2] + first_class.size()[3]) * 100
# 4
print data[['Age']].mean()
print data[['Age']].median()
# 5
print 'corr=', data[['SibSp', 'Parch']].corr(method='pearson')
# 6
data['f_name'] = data['Name'].str.findall('((Mrs\.\s)|(Miss\.\s))(\()?([a-zA-Z])+?(\s.+)')
print data[['Name', 'f_name', 'Sex']][data['Sex'] == 'female']