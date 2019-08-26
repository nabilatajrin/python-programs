import csv
import os
from PIL import Image


def main():
    src = '/media/iit/R a i n/2019/ML/pythonprojects/crop_img/src/'
    dst = '/media/iit/R a i n/2019/ML/pythonprojects/crop_img/dst/'

    try:
        for filename in os.listdir(src):
            print(filename)

            # Relative Path
            img = Image.open("Laabher_Bazar_07-08-2019_1559_0010.jpg")
            # img = Image.open(filename)
            width, height = img.size

            # area = (0, 0, width / 2, height / 2)
            area = (45.5, 580.6878980892, 160.7941176471, 640.076433121)
            img = img.crop(area)

            # Saved in the same relative location
            img.save("cropped_picture2.jpg")




    except IOError:
        pass


if __name__ == "__main__":
    main()