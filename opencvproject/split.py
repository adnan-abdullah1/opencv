import cv2
import numpy as np

def transpose():
        img=cv2.imread("/root/Desktop/nielit/gitopencv/opencv/opencvproject/img/a.jpg")
        ri=cv2.transpose(img)
        cv2.imshow('Rotated image',ri)
        cv2.imshow('Orginal image',img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
def read():
        img=cv2.imread("/root/Desktop/nielit/gitopencv/opencv/opencvproject/img/a.jpg")
        cv2.imshow('output image',img)
        cv2.waitKey(0)
        
        cv2.destroyAllWindows()
        
def resize():
        img=cv2.imread("/root/Desktop/nielit/gitopencv/opencv/opencvproject/img/a.jpg")
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
        img=cv2.imread("/root/Desktop/nielit/gitopencv/opencv/opencvproject/img/a.jpg",0) #convert to greyscale
        cv2.imshow('gray',img)
        cv2.waitKey(0)
        ret,bw=cv2.threshold(img,127,255,cv2.THRESH_BINARY)

        cv2.imshow('binary',bw)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
def hsv():
        # HUE: 0 - 180, SATURATION:0 - 255,VALUE; 0 - 255

        img=cv2.imread("/root/Desktop/nielit/gitopencv/opencv/opencvproject/img/a.jpg")
        img_hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        cv2.imshow('Hue channel',img_hsv[:,:,0])
        cv2.imshow(' SAturation',img_hsv[:,:,1])
        cv2.imshow('Value_channel',img_hsv[:,:,2])
        cv2.waitKey(0)
        cv2.destroyAllWindows()

def hsv():
        # HUE: 0 - 180, SATURATION:0 - 255,VALUE; 0 - 255

        img=cv2.imread("/root/Desktop/nielit/gitopencv/opencv/opencvproject/img/a.jpg")
        img_hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        cv2.imshow('Hue channel',img_hsv[:,:,0])
        cv2.imshow(' SAturation',img_hsv[:,:,1])
        cv2.imshow('Value_channel',img_hsv[:,:,2])
        cv2.waitKey(0)
        cv2.destroyAllWindows()


def gray():
        img=cv2.imread("/root/Desktop/nielit/gitopencv/opencv/opencvproject/img/a.jpg")
        cv2.imshow("original",img)
        cv2.waitKey(0)
# now converting to greyscaleimage method1
        """gray_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imshow('grayimage',gray_img) """
# now converting to greyscaleimage method2
        l=cv2.imread("/root/Desktop/nielit/gitopencv/opencv/opencvproject/img/a.jpg",0)
        cv2.imshow('graycolor',l)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


def rotate():
        angle=int(input("enter angle "))
        scale=float(input("enter scale "))
        img=cv2.imread("/root/Desktop/nielit/gitopencv/opencv/opencvproject/img/a.jpg")
        h,w=img.shape[:2]
        rm=cv2.getRotationMatrix2D((w/2,h/2),angle,scale)  # 180 is ange at which img is rotated 1 is scale
        ri=cv2.warpAffine(img,rm,(w,h))
        cv2.imshow("orgianl image",img)
        cv2.waitKey(0)
        cv2.imshow(" Roatated image ",ri)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

def getinfo():
        img=cv2.imread("/root/Desktop/nielit/gitopencv/opencv/opencvproject/img/a.jpg")

        cv2.imshow('info',img)
        cv2.waitKey(0)
        print("\033[1;35;40m",img.shape)
        print("\033[1;35;40m Height Pixel value: ",img.shape[0])
        print(" \033[1;35;40m idth pixel values : ",img.shape[1])
        cv2.destroyAllWindows()

    

def rgb():
        import numpy as np 
        img=cv2.imread("/root/Desktop/nielit/gitopencv/opencv/opencvproject/img/a.jpg")
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
        img=cv2.imread("/root/Desktop/nielit/gitopencv/opencv/opencvproject/img/a.jpg")
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

def pyramid():   
        img=cv2.imread("/root/Desktop/nielit/gitopencv/opencv/opencvproject/img/a.jpg")
        #Rreducing image dimensions by 50%
        smaller=cv2.pyrDown(img)
        #doubling size of image by 200%
        larger=cv2.pyrUp(img)
        cv2.imshow("Dimension*2",larger)


        cv2.imshow("Dimension/2",smaller)
        cv2.imshow("Orginal",img)

        print(" Orginal Dimensions",img.shape)
        print(" smaller image Dimension/n",smaller.shape)
        print(" larger Dimension*n",larger.shape)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

def crop():
        #image cropping
       
        img=cv2.imread("/root/Desktop/nielit/gitopencv/opencv/opencvproject/img/a.jpg")
        # extract height and width
        h,w=img.shape[:2]

        #extract cordinates(top_left of cropping rectangle)
        start_row,start_col=int(h*.25),int(w*.25)
        # geting end pixel cordinates(bottom right)
        end_row,end_col=int(h*.75),int(w*.75)
        #using indexing to crop image
        cropped=img[start_row:end_row,start_col:end_col]

        cv2.imshow('orginal',img)
        cv2.waitKey(0)
        cv2.imshow('cropped',cropped)
        cv2.waitKey()
        cv2.destroyAllWindows()

def bitwise():
        square=np.zeros((300,300),np.uint8) #creating black image
        cv2.rectangle(square,(50,50),(250,250),255,-1) #200 is color -1 fill whole area 1 will give only square white line
        cv2.imshow('Square',square)
        cv2.waitKey(0)
        #making sllipse now
        ellipse=np.zeros((300,300),np.uint8)
        cv2.ellipse(ellipse,(150,150),(150,150),30,0,180,255,-1)

        cv2.imshow('Ellipse',ellipse)
        cv2.waitKey(0)
        #doing bitwise and
        And=cv2.bitwise_and(square,ellipse)
        cv2.imshow("Bitwise_And",And)
        cv2.waitKey(0)
        #bitwise or
        Or=cv2.bitwise_or(square,ellipse)
        cv2.imshow("Bitwise_or", Or)
        cv2.waitKey(0)
        #bitwise xor
        xor=cv2.bitwise_xor(square,ellipse)
        cv2.imshow("Bitwise_Xor",xor)
        cv2.waitKey(0)
        #bitwise not can be done with single image
        Not11=cv2.bitwise_not(square)
        Not22=cv2.bitwise_not(ellipse)
        cv2.imshow("Bitwise_not",Not11)
        cv2.waitKey(0)
        cv2.imshow("Bitwise_not",Not22)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
def smooth():
        img=cv2.imread("/root/Desktop/nielit/gitopencv/opencv/opencvproject/img/a.jpg")
        cv2.imshow('orginal',img)
        cv2.waitKey(0)
        #averaging done by convoling the image with a normalize box fliter
        #this takes the pixela under and replace the central element
        #Box size needs to odd and postive
        blur=cv2.blur(img,(3,3))
        cv2.imshow('Blur Image',blur)
        cv2.waitKey(0)
        #Gaussian
        Gaussian=cv2.GaussianBlur(img,(7,7),0)
        cv2.imshow('Gaussian Blur ',Gaussian)
        cv2.waitKey(0)
        #median blur
        median=cv2.medianBlur(img,5)
        cv2.imshow('Median Blur image',median)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
def blur():
        img=cv2.imread("/root/Desktop/nielit/gitopencv/opencv/opencvproject/img/a.jpg")
        cv2.imshow('orginal',img)
        cv2.waitKey(0)

        #kernel3*3
        kernel_3=np.ones((3,3),np.float32)/9
        #we use 2D.filter2D convolve the kernel with an image
        blurred=cv2.filter2D(img,-1,kernel_3)
        cv2.imshow('3*3 kernel blur',blurred)
        cv2.waitKey(0)

        kernel_7=np.ones((7,7),np.float32)/49
        #we use 2D.filter2D convolve the kernel with an image
        blurred2=cv2.filter2D(img,-1,kernel_7)
        cv2.imshow('3*3 kernel blur',blurred2)
        cv2.waitKey(0)
        #bilateral filter effective among all useful in noise removal(but heavy)
        bilateral=cv2.bilateralFilter(img,9,75,75)#9 is sigma color and 75 is sigma space and can be changed
        cv2.imshow('Bilateral Blur Image',bilateral)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        


#!----------------------------------------------------------------------------------------------------------------------------!
                                       #   Logrithm image
#!-----------------------------------------------------------------------------------------------------------------------------!
def log1():
        img_1=cv2.imread("/root/Desktop/nielit/gitopencv/opencv/opencvproject/img/a.jpg",0)
        img_2=np.uint8(np.log1(img_1))
        thresh=1
        img_3=cv2.threshold(img_2,thresh,255,cv2.THRESH_BINARY)[1]
        cv2.imshow("Input image",img_1)
        cv2.imshow("Log transformed",img_3)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


#!--------------------------------------------------------------------------------------------------------------------------!
                                        #       Negative of image
#!---------------------------------------------------------------------------------------------------------------------------!
def negative():
    import cv2
    img_1=cv2.imread("/root/Desktop/nielit/gitopencv/opencv/opencvproject/img/a.jpg",0)
    img_2=255-img_1
    cv2.imshow("Negative image",img_2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#!--------------------------------------------------------------------------------------------------------------------------!
                                        #       Negative of image
#!-------------------------------------------------------------------------------------------------------------------------------
def edge():

        img=cv2.imread("/root/Desktop/nielit/gitopencv/opencv/opencvproject/img/a.jpg",0)
        h,w=img.shape

        #extract slope edges
        sobel_x=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
        sobel_y=cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
        cv2.imshow("Orginal_Image",img)
        cv2.waitKey(0)
        cv2.imshow("Sobel_X",sobel_x)
        cv2.imshow("Sobel_y",sobel_y)

        sobel_or=cv2.bitwise_or(sobel_x,sobel_y)
        cv2.imshow("Sobel or image",sobel_or)
        cv2.waitKey(0) 

        #laplacian 
        laplacian=cv2.Laplacian(img,cv2.CV_64F)
        cv2.imshow("Laplacian image",laplacian)

        #cani edge detction
        canny=cv2.Canny(img,20,170) # 20 170 are threshold
        cv2.imshow("Canny Edge",canny)
        cv2.waitKey(0)


#  
#!--------------------------------------------------------------------------------------------------------------------------!
 #                                        optical character recogination      
#!-------------------------------------------------------------------------------------------------------------------------------
"""
def ocr():

        from PIL import Image
        import pytesseract
        #location=input("enter location and image name ")
        im=Image.open('a1.jpg')
        text=pytesseract.image_to_string(im,lang='eng')
        return text
       # print(text)
        
"""