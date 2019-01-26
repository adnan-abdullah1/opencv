import cv2
import numpy as np

def transpose():
    img=cv2.imread('a.jpg')
    ri=cv2.transpose(img)
    cv2.imshow('Rotated image',ri)
    cv2.imshow('Orginal image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
def read():
        img=cv2.imread('a.jpg')
        cv2.imshow('output image',img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
def resize():
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

def binimg():
        img=cv2.imread('a.jpg',0) #convert to greyscale
        cv2.imshow('gray',img)
        cv2.waitKey(0)
        ret,bw=cv2.threshold(img,127,255,cv2.THRESH_BINARY)

        cv2.imshow('binary',bw)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
def hsv():
        # HUE: 0 - 180, SATURATION:0 - 255,VALUE; 0 - 255

        img=cv2.imread('a.jpg')
        img_hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        cv2.imshow('Hue channel',img_hsv[:,:,0])
        cv2.imshow(' SAturation',img_hsv[:,:,1])
        cv2.imshow('Value_channel',img_hsv[:,:,2])
        cv2.waitKey(0)
        cv2.destroyAllWindows()

def hsv():
        # HUE: 0 - 180, SATURATION:0 - 255,VALUE; 0 - 255

        img=cv2.imread('a.jpg')
        img_hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        cv2.imshow('Hue channel',img_hsv[:,:,0])
        cv2.imshow(' SAturation',img_hsv[:,:,1])
        cv2.imshow('Value_channel',img_hsv[:,:,2])
        cv2.waitKey(0)
        cv2.destroyAllWindows()


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
        cv2.destroyAllWindows()


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
        cv2.destroyAllWindows()

def getinfo():
        img=cv2.imread("a.jpg")

        cv2.imshow('info',img)
        cv2.waitKey(0)
        print("\033[1;35;40m",img.shape)
        print("\033[1;35;40m Height Pixel value: ",img.shape[0])
        print(" \033[1;35;40m idth pixel values : ",img.shape[1])
        cv2.destroyAllWindows()

    

def rgb():
        import numpy as np 
        img=cv2.imread('a.jpg')
        cv2.imshow("orginal",img)
        cv2.waitKey(0)
# now extract R G B 

        B,G,R=cv2.split(img)
        print("\033[1;35;40m",img.shape)
        zeros=np.zeros(img.shape[:2],dtype="uint8")
        cv2.imshow("Red",cv2.merge([zeros,zeros,R]))
        cv2.imshow("GREEn",cv2.merge([zeros,G,zeros]))
        cv2.imshow("BLUE",cv2.merge([B,zeros,zeros]))
        cv2.imshow("MERGE all three bgr=orginalimage",cv2.merge([B,G,R]))
        cv2.waitKey(0)
        cv2.destroyAllWindows()

def dip():
        img=cv2.imread('a.jpg')
# store height and width of image
        height,width=img.shape[:2]
        print("\033[1;35;40m",height)
        print("\033[1;35;40m",width)
        quarter_height,quarter_width=height/4,width/4
        print(" \033[1;35;40m after dividing by 4 ")
        print("\033[1;35;40m",quarter_height)
        print("\033[1;35;40m",quarter_width)

#     | 1 0 Tx |
#   T=| 0 1 Ty |

# T is translation matrix

        T=np.float32([[1,0,quarter_width],[0,1,quarter_width]])
        print("\033[1;35;40mT= ",T)
    # float32 is matrix name

    #we use warpAffine Transformation to shift image
        img_translation=cv2.warpAffine(img,T,(width,height))
        cv2.imshow('orginal image',img)
        cv2.waitKey(0)
        cv2.imshow('Translation',img_translation)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    
