import pandas
import numpy as np
from numpy._distributor_init import N
from sklearn.tree import DecisionTreeClassifier
import scipy

data = pandas.read_csv('../1.1/titanic.csv', index_col='PassengerId')
# data = data[['Pclass', 'Fare', 'Age', 'Sex']]