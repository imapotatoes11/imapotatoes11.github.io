#https://www.w3schools.com/python/python_ml_scatterplot.asp
'''
Scatter Plot
A scatter plot is a diagram where each value in the data set is represented by a dot.
'''
#basic scatter plot
import numpy
import matplotlib.pyplot as plt
import numpy as np

#x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
#y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x=np.random.normal(50,0.1,1000)
y=np.random.normal(50,0.1,1000)

plt.scatter(x, y)
plt.show()

#scatter plot with 1000 dots
#you can see that the standard deviation is small(1 on the x axis and 2 on the y axis)

x = numpy.random.normal(5.0, 1.0, 1000)
y = numpy.random.normal(10.0, 2.0, 1000)

plt.scatter(x, y)
plt.show()