#resizing and interpolation
import cv2
import numpy as  pd
img=cv2.imread('a.jpg')
cv2.imshow('orginal Image',img)
cv2.waitKey(0)

img_scaled=cv2.resize(img,None,fx=.75,fy=.75)
cv2.imshow('Scaling- linear interpolation',img_scaled) #making the size of image 3/4 of its orginal sized)
cv2.waitKey(0)
#doubling image dimension doublin x axis and y axis
img_scaled1=cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)
cv2.imshow('Scaling- CUBIC interpolation',img_scaled1)

cv2.waitKey(0)
# resizing by exact dimension
img_scaled2=cv2.resize(img,(500,300),interpolation=cv2.INTER_AREA)
cv2.imshow('scaling-skewed size ',img_scaled2)
cv2.waitKey(0)
cv2.destroyAllWindows()