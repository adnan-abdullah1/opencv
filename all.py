import numpy as np 
import cv2
i=1
while i==1:
    print(" ENTER 1 TO READ IMAGE\nENTER 2 TO GET IMAGE INFO \n ENTER 3 TO GET BINARY OF IMAGE \n ENTER 4 TO EXTRACT RGB\nENTER 5 TO DISPACE IMAGE\nENTER 6 TO GET GRAY SCALE\n ENTER 7 TO GET HSV OF IMAGE\nENTER 8 TO ROTATE IMAGE")

    f=int(input(" enter choice "))
    def gray():
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

    def read():
        img=cv2.imread('a.jpg')
        cv2.imshow('output image',img)
        cv2.waitKey(0)
        


    def rotate():
        angle=int(input("enter angle "))
        scale=float(input("enter scale "))
        img=cv2.imread('a.jpg')
        h,w=img.shape[:2]
        rm=cv2.getRotationMatrix2D((w/2,h/2),angle,scale)  # 180 is ange at which img is rotated 1 is scale
        ri=cv2.warpAffine(img,rm,(w,h))
        cv2.imshow("orgianl image",img)
        cv2.waitKey(0)
        cv2.imshow(" Roatated image ",ri)
        cv2.waitKey(0)

    def getinfo():
        img=cv2.imread("a.jpg")

        cv2.imshow('info',img)
        cv2.waitKey(0)
        print(img.shape)
        print("Height Pixel value: ",img.shape[0])
        print(" idth pixel values : ",img.shape[1])
        

    def binimg():
        img=cv2.imread('a.jpg',0) #convert to greyscale
        cv2.imshow('gray',img)
        cv2.waitKey(0)
        ret,bw=cv2.threshold(img,127,255,cv2.THRESH_BINARY)

        cv2.imshow('binary',bw)
        cv2.waitKey(0)
        

    def rgb():
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
        


    def dip():
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
        
    def hsv():
        # HUE: 0 - 180, SATURATION:0 - 255,VALUE; 0 - 255

        img=cv2.imread('a.jpg')
        img_hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        cv2.imshow('Hue channel',img_hsv[:,:,0])
        cv2.imshow(' SAturation',img_hsv[:,:,1])
        cv2.imshow('Value_channel',img_hsv[:,:,2])
        cv2.waitKey(0)



    if f==1:
        read()
    if f==2:
        getinfo()
    if f==3:
        binimg()
    if f==4:
        rgb()
    if f==5:
        dip()
    
    if f==6:
        gray()
    if f==7:
        hsv()
    if f==8:
        rotate()

    i=int(input(" enter 1 if contuniue "))