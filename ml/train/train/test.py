#https://www.w3schools.com/python/python_ml_train_test.asp
'''
What is Train/Test
Train/Test is a method to measure the accuracy of your model.

It is called Train/Test because you split the the data set into two sets: a training set and a testing set.

80% for training, and 20% for testing.

You train the model using the training set.

You test the model using the testing set.

Train the model means create the model.

Test the model means test the accuracy of the model.

Start With a Data Set
Start with a data set you want to test.

Our data set illustrates 100 customers in a shop, and their shopping habits.
'''
import numpy
import matplotlib.pyplot as plt
numpy.random.seed(2)

x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

plt.scatter(x, y)
plt.show()
'''
Result:
The x axis represents the number of minutes before making a purchase.

The y axis represents the amount of money spent on the purchase.

Split Into Train/Test
The training set should be a random selection of 80% of the original data.

The testing set should be the remaining 20%.
'''

train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]
plt.scatter(train_x, train_y)
plt.show()
#to make sure the testing set is not completely different, we will have a loook at the testing set as well
plt.scatter(test_x, test_y)
plt.show()
'''
Fit the Data Set
What does the data set look like? In my opinion I think the best fit would be a polynomial regression, so let us draw a line of polynomial regression.

To draw a line through the data points, we use the plot() method of the matplotlib module:
'''
print('polynomial regression through thhe data points')
numpy.random.seed(2)

x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))

myline = numpy.linspace(0, 6, 100)

plt.scatter(train_x, train_y)
plt.plot(myline, mymodel(myline))
plt.show()


print('how well does my training data fit in a polynomial regression')
import numpy
from sklearn.metrics import r2_score
numpy.random.seed(2)

x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))

r2 = r2_score(train_y, mymodel(train_x))

print(r2)


print('find r2 score when testing data')
from sklearn.metrics import r2_score
numpy.random.seed(2)

x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))

r2 = r2_score(test_y, mymodel(test_x))

print(r2)
#predict values
print('#predict values')
print(mymodel(5))