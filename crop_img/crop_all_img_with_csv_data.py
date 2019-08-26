import os
from PIL import Image
import csv

def main():
    src = '/media/iit/R a i n/2019/ML/pythonprojects/crop_img/src/'
    dst = '/media/iit/R a i n/2019/ML/pythonprojects/crop_img/dst/'

    for filename in os.listdir(src):
        print(filename)

        try:
            img = Image.open(src + filename)
            print("#####", img)
            width, height = img.size

            file = open(src + "Uniliver-export.csv".format(filename), "r")
            reader = csv.reader(file)

            for line in reader:
                t = line[0], line[1], line[2], line[3], line[4], line[5]
                print(t)
                area = (line[1], line[2], line[3], height / 2)
                img = img.crop(area)

                img.save(dst + filename + '_cropped.jpg')

        except IOError:
            pass

# Driver Code
if __name__ == '__main__':
    # Calling main() function
    main()