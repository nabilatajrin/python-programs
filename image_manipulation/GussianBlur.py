from PIL import Image, ImageFilter
import os

srcPath = "/media/iit/R a i n/2019/ML/pythonprojects/image_manipulation/pngs/"
dstPath = "/media/iit/R a i n/2019/ML/pythonprojects/image_manipulation/blurred_image/"
dirs = os.listdir(srcPath)

def gaussianBlur():
    for item in dirs:
        if os.path.isfile(srcPath + item):
            im = Image.open(srcPath + item)
            file, e = os.path.splitext(dstPath + item)
            imblur = im.filter(ImageFilter.GaussianBlur(10))
            imblur.save(file + '.jpg', 'JPEG', quality = 90)

gaussianBlur()
