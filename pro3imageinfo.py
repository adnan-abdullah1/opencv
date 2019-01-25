import cv2
img=cv2.imread("a.jpg")

cv2.imshow('info',img)
cv2.waitKey(0)
print(img.shape)
print("Height Pixel value: ",img.shape[0])
print(" idth pixel values : ",img.shape[1])
#cv2.destroyAllWindows()