import os
import cv2
import numpy as np
from PIL import Image

srcPath = '/media/iit/R a i n/2019/Intelligent Machines Ltd/face-propagation/dummy-data-set/colorferet/colorferet/test_blur/src_blur/'
dstPath = '/media/iit/R a i n/2019/Intelligent Machines Ltd/face-propagation/dummy-data-set/colorferet/colorferet/test_blur/motion_blur/'
dirs = os.listdir(srcPath)

#convert images to .jpg and save in a different directory
def image_to_image():
    for item in dirs:
        if os.path.isfile(srcPath + item):
            print(item)
            img = cv2.imread(srcPath + item)
            cv2.imshow('Original', img)
            size = 15
            #img.show(item)

            # generating the kernel
            kernel_motion_blur = np.zeros((size, size))
            kernel_motion_blur[int((size - 1) / 2), :] = np.ones(size)
            kernel_motion_blur = kernel_motion_blur / size

            # applying the kernel to the input image
            output = cv2.filter2D(img, -1, kernel_motion_blur)

            cv2.imshow('Motion Blur', output)
            cv2.waitKey(0)

            file, e = os.path.splitext(dstPath + item)
            #img_blur = img.filter(PIL.ImageFilter.EMBOSS)

            img_Resize = img.resize((256, 256), Image.ANTIALIAS)
            blur_img_resize = kernel_motion_blur.resize((256, 256), Image.ANTIALIAS)

            img_Resize.save(file + '.jpg', 'JPEG', quality = 90)
            blur_img_resize.save(file + '_blur.jpg', 'JPEG', quality = 100)

image_to_image()

dstPath = "/media/iit/R a i n/2019/Intelligent Machines Ltd/face-propagation/dummy-data-set/colorferet/colorferet/test_blur/motion_blur/"
mrgPath = "/media/iit/R a i n/2019/Intelligent Machines Ltd/face-propagation/dummy-data-set/colorferet/colorferet/test_blur/original_and_motion_blur_mrg/"
dirs2 = os.listdir(dstPath)
images = list(map(Image.open, [(dstPath + i) for i in dirs2]))

def mergeImage():
    total_width = 512
    max_height = 256

    new_im = Image.new('RGB', (total_width, max_height))

    x_offset = 0
    i = 0
    j = 0

    for im in images:
        new_im.paste(im, (x_offset, 0))
        x_offset += im.size[0]
        i += 1
        if (i % 2 == 0):
            j += 1
            x_offset = 0
            new_im.save(mrgPath + "motion_blur_" + str(j) + '.jpg')
            #new_im.show()

mergeImage()











