#https://www.w3schools.com/python/python_ml_data_distribution.asp
#https://www.w3schools.com/python/python_ml_normal_data_distribution.asp

import numpy
import matplotlib.pyplot as plt

print('small uniform')
x = numpy.random.uniform(0.0, 5.0, 250)

plt.hist(x, 5)
plt.show()
"""
Histogram Explained
We use the array from the example above to draw a histogram with 5 bars.

The first bar represents how many values in the array are between 0 and 1.

The second bar represents how many values are between 1 and 2.

Etc.

Which gives us this result:

52 values are between 0 and 1
48 values are between 1 and 2
49 values are between 2 and 3
51 values are between 3 and 4
50 values are between 4 and 5
"""

#big boy distributions
print('big boy uniform')
x = numpy.random.uniform(0.0, 5.0, 100000)

plt.hist(x, 100)
plt.show()

#normal data distribution
print('big boy normal distribution')
x = numpy.random.normal(5.0,1.0,100000)
#                       /\==mean value
#                            /\==standard deviation
#                                /\==number of values
plt.hist(x,100)
plt.show()