#!/usr/bin/python3
import numpy as np
import cv2


height = 512
width = 512
radius = 100
thickness = 300

#GENERATE RANDOM NUMBERS
bytes = np.zeros((height, width, 3))

# bytes[:, :, 0:3] = np.random.uniform(0, 2, (3,))
# bytes[:, :, 0:3] = np.random.uniform(0, 1, (3,))
bytes = np.multiply(bytes, 255)
for x in range(-radius, width):
  for y in range( -radius, height):
   if ((x * x) + (y * y) >= (radius * radius)) and  ((x * x) + (y * y) <= ((radius * radius) + thickness)):
      bytes[x, y, 2] = 255

bytes = np.roll(bytes, 2 * radius, axis=0) 
bytes = np.roll(bytes, 2 * radius, axis=1) 

# bytes = np.random.randint(255, size=(height, width, 3))
# print(bytes)
# nonzeros = np.count_nonzero(bytes)
# print(nonzeros)

# bytes[:,:,0] = np.ones([height,width])*64/255.0
# bytes[:,:,1] = np.ones([height,width])*128/255.0
# bytes[:,:,2] = np.ones([height,width])*192/255.0
# bytes[255,255,0] = 255
# save as image file: 
# bytes = np.multiply(bytes, )

#SAVE AS IMAGE
cv2.imwrite('output.png', bytes)