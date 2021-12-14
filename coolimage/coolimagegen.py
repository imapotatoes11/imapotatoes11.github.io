import numpy as np
from PIL import Image

arr = np.random.randint(low = 0, high = 255, size = (300, 300, 3), dtype=np.uint8)

im = Image.fromarray(arr.astype('uint8'))
im.show()


import numpy as np
import scipy.ndimage as ndimage
import matplotlib.pyplot as plt

#import matplotlib.image as mpimg
#img = mpimg.imread(im)
img=im

plt.imshow(img, interpolation='nearest')
plt.show()
# Note the 0 sigma for the last axis, we don't wan't to blurr the color planes together!
img = ndimage.gaussian_filter(img, sigma=(5, 5, 0), order=0)
plt.imshow(img, interpolation='nearest')
plt.show()