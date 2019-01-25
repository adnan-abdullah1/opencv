import cv2
import numpy as numpy
img=cv2.imread('a.jpg')
h,w=img.shape[:2]

rm=cv2.getRotationMatrix2D((w/2,h/2),180,1)  # 180 is ange at which img is rotated 1 is scale
ri=cv2.warpAffine(img,rm,(w,h))
cv2.imshow("orgianl image",img)
cv2.waitKey(0)
cv2.imshow(" Roatated image ",ri)
cv2.waitKey(0)
