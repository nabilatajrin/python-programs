from PIL import Image
import os

src = '/media/iit/R a i n/2019/ML/pythonprojects/image_manipulation'

#convert and save image in different directory
for filename in os.listdir(src):
    if filename.endswith('.jpg'):
        print (filename)


image1 = Image.open('test.ppm')
image2 = Image.open('treepic.jpg')
image1.show()
image2.show()
image1.save('test.png')