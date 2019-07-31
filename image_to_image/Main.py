from PIL import Image
import os

srcPath = '/media/iit/R a i n/2019/Intelligent Machines Ltd/face-propagation/dummy-data-set/colorferet/colorferet/test_blur/src_blur/'
dstPath = '/media/iit/R a i n/2019/Intelligent Machines Ltd/face-propagation/dummy-data-set/colorferet/colorferet/test_blur/dst_blur/'
dirs = os.listdir(srcPath)

#convert and save images in different directory
def convertImageType():
    for item in dirs:
        if os.path.isfile(srcPath + item):
            print(item)
            convertImage = Image.open(srcPath + item)
            convertImage.show(item)
            #Image.open(item)
            #convertImage = Image.open(item)
            #convertImage.show(item)



convertImageType()








