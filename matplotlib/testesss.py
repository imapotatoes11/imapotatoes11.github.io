import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5,5,100)
y = (x-2)*(x-3)
plt.plot(x, y, '-r', label='y=(x-2)(x-3)')

x=np.linspace(-5,5,100)
y=2*x*x-5*x+3
plt.plot(x,y,'-b',label='y=2x^2-5x+3')

x=np.linspace(-5,5,100)
y=3*x*x-5*x+3
plt.plot(x,y,'g',label='y=3x^2-5x+3')

plt.title('graphs')
plt.xlabel('x', color='#1C2833')
plt.ylabel('y', color='#1C2833')
plt.legend(loc='upper left')
plt.show()