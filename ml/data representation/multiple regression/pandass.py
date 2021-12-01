#https://www.w3schools.com/python/python_ml_multiple_regression.asp
'''
Learn about the Pandas module in our Pandas Tutorial.

The Pandas module allows us to read csv files and return a DataFrame object.

The file is meant for testing purposes only, you can download it here: cars.csv

df = pandas.read_csv("cars.csv")

Then make a list of the independent values and call this variable X.

Put the dependent values in a variable called y.

We will use some methods from the sklearn module, so we will have to import that module as well:
From the sklearn module we will use the LinearRegression() method to create a linear regression object.

This object has a method called fit() that takes the independent and dependent values as parameters and fills the regression object with data that describes the relationship:
'''
import pandas
from sklearn import linear_model

df = pandas.read_csv("cars.csv")

X = df[['Weight', 'Volume']]
y = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(X, y)

#predict the CO2 emission of a car where the weight is 2300kg, and the volume is 1300cm3:
predictedCO2 = regr.predict([[2300, 1300]])

print(predictedCO2)
#result:
#[107.2087328]
#ignore error
#visual bug