import pandas
import numpy as np
from sklearn.tree import DecisionTreeClassifier

data = pandas.read_csv('../1.1/titanic.csv', index_col='PassengerId')
# print data.head()
data = data[['Survived', 'Pclass', 'Fare', 'Age', 'Sex']].dropna()
predictor = data[['Pclass', 'Fare', 'Age']]
predictor['Sex'] = data['Sex'].replace(to_replace=['male', 'female'], value=[0, 1])
print predictor.head()
response = data[['Survived']]
print predictor.__len__(), response.__len__()

clf = DecisionTreeClassifier(random_state=241)
clf.fit(predictor, response)
print clf.feature_importances_