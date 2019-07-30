import os
from PIL import Image

def main():

    src = '/media/iit/R a i n/2019/Intelligent Machines Ltd/face-propagation/dummy-data-set/colorferet/colorferet/test_blurr/dst_blurr'
    dst = '/media/iit/R a i n/2019/Intelligent Machines Ltd/face-propagation/dummy-data-set/colorferet/colorferet/test_blurr/src_blurr'

    #img = Image.open("source")
    #im = Image.copy(img)

    for filename in os.listdir(src):
        print(filename)

        srcFolder = src + '/' + filename
        dstFolder = dst + '/' +filename

        # move all the files
        os.rename(srcFolder, dstFolder)



# Driver Code
if __name__ == '__main__':
    # Calling main() function
    main()