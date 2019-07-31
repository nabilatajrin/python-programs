from PIL import Image, ImageFilter
import os

srcPath = '/media/iit/R a i n/2019/Intelligent Machines Ltd/face-propagation/dummy-data-set/colorferet/colorferet/test_blur/src_blur/'
dstPath = '/media/iit/R a i n/2019/Intelligent Machines Ltd/face-propagation/dummy-data-set/colorferet/colorferet/test_blur/dst_blur/'
dirs = os.listdir(srcPath)

#convert images to .jpg and save in a different directory
def convertImageType():
    for item in dirs:
        if os.path.isfile(srcPath + item):
            print(item)
            img = Image.open(srcPath + item)
            #img.show(item)

            file, e = os.path.splitext(dstPath + item)
            img_blur = img.filter(ImageFilter.GaussianBlur(10))
            #img_blur.show(item)
            img_Resize = img.resize((256, 256), Image.ANTIALIAS)
            blur_img_resize = img_blur.resize((256, 256), Image.ANTIALIAS)
            img_Resize.save(file + '.jpg', 'JPEG', quality = 90)
            blur_img_resize.save(file + '_blur.jpg', 'JPEG', quality = 90)



convertImageType()








