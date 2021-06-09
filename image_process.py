import cv2
image= cv2.imread("photo.jpg")

#create the  white background for image
image[:]=[255,255,255] 

###############create an image#################
image=cv2.circle(image,(500,200),100,(0,225,225),5)
image=cv2.circle(image,(465,175),5,(0,225,225),4)
image=cv2.circle(image,(535,175),5,(0,225,225),4)
image=cv2.ellipse(image,(500,225),(50,15),0,0,180,(0,225,225),4)

###############Displaying created image################
cv2.imshow('myphoto',image)
cv2.waitKey()
cv2.destroyAllWindows()

# import the two images
boy1=cv2.imread('boy1.png')        #image 1
boy2=cv2.imread('boy2.png')         #image 2

################  boy2 image before swap################
cv2.imshow('myphoto',boy2)
cv2.waitKey()
cv2.destroyAllWindows()

#############swaping the faces of two images###########:
import numpy 
temp_boy1=boy1.tolist()
boy1[3:290,120:350]=boy2[3:290,120:350]
boy2[3:290,120:350]=numpy.array(temp_boy1,dtype='uint8')[3:290,120:350]


############Displaying boy1 image after swap##############
cv2.imshow('myphoto',boy1)
cv2.waitKey()
cv2.destroyAllWindows()

############Displaying boy2 image after swap##############
cv2.imshow('myphoto',boy2)
cv2.waitKey()
cv2.destroyAllWindows()


##############combining two images###############
boy3=numpy.hstack((boy1,boy2))


############Displaying  comibined image##############
cv2.imshow('myphoto',boy3)
cv2.waitKey()
cv2.destroyAllWindows()




