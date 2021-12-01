import numpy as np
import matplotlib.pyplot as plt
x=np.random.exponential(5.0,10000)
y=np.random.exponential(5.0,10000)

plt.scatter(x,y,s=0.1)
plt.show()