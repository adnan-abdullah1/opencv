import cv2
import numpy as np 
img=cv2.imread('a.jpg')
# store height and width of image
height,width=img.shape[:2]
print(height)
print(width)
quarter_height,quarter_width=height/4,width/4
print(" after dividing by 4 ")
print(quarter_height)
print(quarter_width)

#     | 1 0 Tx |
#   T=| 0 1 Ty |

# T is translation matrix

T=np.float32([[1,0,quarter_width],[0,1,quarter_width]])
print(" T= ",T)
# float32 is matrix name

#we use warpAffine Transformation to shift image
img_translation=cv2.warpAffine(img,T,(width,height))
cv2.imshow('orginal image',img)
cv2.waitKey(0)
cv2.imshow('Translation',img_translation)
cv2.waitKey(0)