from PIL import Image
import os

path = "/media/iit/R a i n/2019/ML/pythonprojects/image_manipulation/256/"
out = "/media/iit/R a i n/2019/ML/pythonprojects/image_manipulation/merge_image/"
dirs = os.listdir(path)
images = list(map(Image.open, [(path + i) for i in dirs]))

# widths, heights = zip(*(i.size for i in images))
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
            new_im.save(out + str(j) + '.jpg')
            new_im.show()

mergeImage()

