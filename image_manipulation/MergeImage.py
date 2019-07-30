from PIL import Image
import os

srcPath = "/media/iit/R a i n/2019/ML/pythonprojects/image_manipulation/256/"
dstPath = "/media/iit/R a i n/2019/ML/pythonprojects/image_manipulation/merge_image/"
dirs = os.listdir(srcPath)
images = list(map(Image.open, [(srcPath + i) for i in dirs]))

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
        new_im.show()

