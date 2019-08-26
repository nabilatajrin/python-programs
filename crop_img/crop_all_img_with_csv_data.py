import os
from PIL import Image

def main():
    src = '/media/iit/R a i n/2019/ML/pythonprojects/crop_img/src/'
    dst = '/media/iit/R a i n/2019/ML/pythonprojects/crop_img/dst/'

    for filename in os.listdir(src):
        print(filename)

        try:
            img = Image.open(src + filename)
            print("#####", img)
            width, height = img.size

            area = (0, 0, width / 2, height / 2)
            img = img.crop(area)

            img.save(dst + filename + '_cropped.jpg')

        except IOError:
            pass

# Driver Code
if __name__ == '__main__':
    # Calling main() function
    main()