import cv2
img=cv2.imread('a.jpg')
cv2.imshow('my_mehnat',img)
cv2.imwrite('Output.jpg',img)
cv2.imwrite('Output.png',img)
cv2.waitKey(0)
cv2.destroyAllwindows()