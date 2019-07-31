from PIL import Image
import os

srcPath = '/media/iit/R a i n/2019/ML/pythonprojects/image_manipulation'
dstPath = '/media/iit/R a i n/2019/ML/pythonprojects/image_manipulation/pngs/'

#convert and save images in different directory
def convertImage():
    for filename in os.listdir(srcPath):
        print(filename)

        if filename.endswith('.ppm'):
            print(filename)
            convertImage = Image.open(filename)
            # convertImage.show(filename)
            # convertImage.save('test.png')

            #convert images to .png and save it to different folder
            fn, fext = os.path.splitext(filename)
            print(fext)
            convertImage.save(dstPath + '{}.png'.format(fn))

convertImage()






