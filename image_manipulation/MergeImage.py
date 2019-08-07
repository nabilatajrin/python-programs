from PIL import Image
import os

srcPath = "/media/iit/Transcend/nabila/data-set/image_to_image/box_blur/"
#srcPath = "/media/iit/Transcend/nabila/data-set/test/dst/"
dstPath = "/media/iit/Transcend/nabila/data-set/image_to_image/original_and_box_blur_mrg/"
#dstPath = "/media/iit/Transcend/nabila/data-set/test/dst2/"
dirs = os.listdir(srcPath)
images = list(map(Image.open, [(srcPath + i) for i in dirs]))

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
                new_im.save(dstPath + str(j) + '.jpg')
                #new_im.show()

mergeImage()

