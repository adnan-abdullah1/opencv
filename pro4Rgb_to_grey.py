import cv2
img=cv2.imread('a.jpg')
cv2.imshow("original",img)
cv2.waitKey(0)
# now converting to greyscaleimage method1
"""gray_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('grayimage',gray_img) """
# now converting to greyscaleimage method2
l=cv2.imread('a.jpg',0)
cv2.imshow('graycolor',l)
cv2.waitKey(0)