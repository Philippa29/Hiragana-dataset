from cgi import test
import io
from PIL import Image , ImageFilter 
import tensorflow as tf
import numpy as np
from random import seed
from random import randint
import matplotlib.pyplot as plt
from numpy import expand_dims
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from matplotlib import pyplot
import cv2
class testing: 

    """
    blur function:
        takes the different images in pictures folder and blurs them
    request body: 
        blurr: the degree for GaussianBlur
        counter: the counter of how many images are in the testing folder
    return:
        counter
""" 
    def blur(self,blurr,counter): 
        #blur
        for i in range (0,38):
            manipulated =Image.open('./pictures/test_'+ str(i) + '.png')
            
            gaussImage = manipulated.filter(ImageFilter.GaussianBlur(blurr))
            for j in range (0,5):
                gaussImage.save('../../dataset/test/ni/picture_'+str(counter) + '.png')
                counter = counter + 1
        return counter
    """
   rotate_image_:
        takes the different images in pictures folder and roates them by a degree
    request body: 
        angle: the degree for the rotation
        counter: the counter of how many images are in the testing folder
    return:
        counter
""" 
    def rotate_image_(self,angle,counter):
        
        for i in range (0,38):
            manipulated =Image.open('./pictures/test_'+ str(i) + '.png')
            manipulated = manipulated.rotate(angle)
            for j in range (0,50):
                manipulated.save('../../dataset/test/ni/picture_'+str(counter) + '.png')
                counter = counter + 1
        return counter
    """
   zoom_image:
        takes the different images in pictures folder and zooms in on them 
    request body: 
       
        counter: the counter of how many images are in the testing folder
    return:
        counter
    """
    def zoom_image(self,counter): 
       
        for i in range (0,38):
            manipulated =Image.open('./pictures/test_'+ str(i) + '.png')
            img_buf = io.BytesIO()
            datagen = ImageDataGenerator()
            data = img_to_array(manipulated)
            samples = expand_dims(data,0)
            datagen = ImageDataGenerator(zoom_range=[0.5,1.5])
            it = datagen.flow(samples, batch_size = 1)
            pyplot.subplot(330+1+3)
            batch = it.next()
            image = batch[0].astype('uint8')
            manipulated = Image.fromarray(image)
            for j in range (0,50):
                manipulated.save('../../dataset/test/ni/picture_'+str(counter) + '.png')
                counter = counter + 1
        return counter
    """
   shear:
        takes the different images in pictures folder and shear them 
    request body: 
       
        counter: the counter of how many images are in the testing folder
    return:
        counter
""" 
    def shear(self,counter):
        for i in range (0,38):
            img = cv2.imread("./pictures/test_"+str(i)+".png")
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            plt.axis('off')
        
            rows, cols, dim = img.shape
            M = np.float32([[1, 0.5, 0],
             	[0, 1  , 0],
            	[0, 0  , 1]])
            sheared_img = cv2.warpPerspective(img,M,(int(cols*1.2),int(rows*1.2)))
            plt.axis('off')
            for j in range (0,50):
                plt.imsave('../../dataset/test/ni/picture_'+str(counter) + '.png', sheared_img)
                counter = counter + 1
        return counter
    """
   transpose_90:
        takes the different images in pictures folder and transposes them by 90 degrees
    request body: 
       
        counter: the counter of how many images are in the testing folder
    return:
        counter
""" 
    def transpose_90(self,counter): 
        for i in range (0,38):
            manipulated =Image.open('./pictures/test_'+ str(i) + '.png')
            manipulated = manipulated.transpose(Image.ROTATE_90)
            for j in range (0,50):
                manipulated.save('../../dataset/test/ni/picture_'+str(counter) + '.png')
                counter = counter + 1
        return counter
    """
   transpose_270:
        takes the different images in pictures folder and transposes them by 270 degrees
    request body: 
       
        counter: the counter of how many images are in the testing folder
    return:
        counter
""" 
    def transpose_270(self,counter):
        for i in range (0,38):
            manipulated =Image.open('./pictures/test_'+ str(i) + '.png')
            manipulated = manipulated.transpose(Image.ROTATE_270)
            for j in range (0,50):
                manipulated.save('../../dataset/test/ni/picture_'+str(counter) + '.png')
                counter = counter + 1
        return counter

if __name__ == '__main__':
    testing = testing()
  
    counter = 0
    print(counter)
    counter= testing.rotate_image_(15,counter)
    
   
   
    counter = testing.rotate_image_(30,counter)
  
    
    counter = testing.rotate_image_(45,counter)
   
    counter =  testing.rotate_image_(-15,counter)
   
    counter = testing.rotate_image_(-30,counter)
   
    counter =  testing.rotate_image_(-45,counter)
    counter =  testing.zoom_image(counter)
    counter =  testing.shear(counter)
    counter =  testing.transpose_90(counter)
    counter =  testing.transpose_270(counter)
    counter = testing.blur(1,counter)
    counter =  testing.blur(2,counter)
    counter =  testing.blur(3,counter)
    counter =  testing.blur(4,counter)
    counter =  testing.blur(5,counter)
    print(counter)
    print("done")