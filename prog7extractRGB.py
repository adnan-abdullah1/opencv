import cv2
import numpy as np 
img=cv2.imread('a.jpg')
cv2.imshow("orginal",img)
cv2.waitKey(0)
# now extract R G B 
B,G,R=cv2.split(img)
print(img.shape)
zeros=np.zeros(img.shape[:2],dtype="uint8")
cv2.imshow("Red",cv2.merge([zeros,zeros,R]))
cv2.imshow("GREEn",cv2.merge([zeros,G,zeros]))
cv2.imshow("BLUE",cv2.merge([B,zeros,zeros]))
cv2.imshow("MERGE all three bgr=orginalimage",cv2.merge([B,G,R]))
cv2.waitKey(0)
