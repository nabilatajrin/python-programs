from PIL import Image
import os

srcPath = "/media/iit/R a i n/2019/ML/pythonprojects/image_manipulation/pngs/"
dstPath = "/media/iit/R a i n/2019/ML/pythonprojects/image_manipulation/256/"
dirs = os.listdir(srcPath)

def resizeto256():
    for item in dirs:
        if os.path.isfile(srcPath + item):
            im = Image.open(srcPath + item)
            file, e = os.path.splitext(dstPath + item)
            imResize = im.resize((256, 256), Image.ANTIALIAS)
            imResize.save(file + '.jpg', 'JPEG', quality = 90)

resizeto256()
