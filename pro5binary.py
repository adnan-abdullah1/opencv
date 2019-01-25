import cv2
img=cv2.imread('a.jpg',0) #convert to greyscale
cv2.imshow('gray',img)
cv2.waitKey(0)
ret,bw=cv2.threshold(img,127,255,cv2.THRESH_BINARY)

cv2.imshow('binary',bw)
cv2.waitKey(0)

