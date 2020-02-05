import numpy as np
import cv2

'''
   This program generates a random color image of dimensions 256x512 and saves it in current folder
'''

height = 256
width = 512

#generating random numpy array which ranges from 0 to 255 for three channels(r,g,b)
red = (np.random.rand(height, width)*255).astype('uint8')
green = (np.random.rand(height, width)*255).astype('uint8')
blue = (np.random.rand(height, width)*255).astype('uint8')

#combining r,g,b channels
img = cv2.merge((red, green, blue))

#saving generated image
cv2.imwrite('./out_color.png', img)


