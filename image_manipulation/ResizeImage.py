from PIL import Image
import os

path = "/media/iit/R a i n/2019/ML/pythonprojects/image_manipulation/pngs/"
output="/media/iit/R a i n/2019/ML/pythonprojects/image_manipulation/256/"
dirs = os.listdir(path)

def resizeto256():
    for item in dirs:
        if os.path.isfile(path + item):
            im = Image.open(path + item)
            file, e = os.path.splitext(output + item)
            imResize = im.resize((256, 256), Image.ANTIALIAS)
            imResize.save(file + '.jpg', 'JPEG', quality = 90)

resizeto256()
