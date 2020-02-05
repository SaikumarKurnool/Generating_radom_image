import numpy as np
import cv2

'''
   This program generates a random image of dimensions 256x512 and saves it in current folder
   (for this example we are going with a single channel image i.e., black and white image)
'''

height = 256
width = 512

#generating random numpy array which ranges from 0 to 255
img = (np.random.rand(height, width)*255).astype('uint8')

#saving generated image
cv2.imwrite('out_bw.png', img)


