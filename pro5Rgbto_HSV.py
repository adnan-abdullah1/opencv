# HUE: 0 - 180, SATURATION:0 - 255,VALUE; 0 - 255
import cv2
img=cv2.imread('a.jpg')
img_hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow('Hue channel',img_hsv[:,:,0])
cv2.imshow(' SAturation',img_hsv[:,:,1])
cv2.imshow('Value_channel',img_hsv[:,:,2])
cv2.waitKey(0)