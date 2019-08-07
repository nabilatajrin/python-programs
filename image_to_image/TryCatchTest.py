import PIL
from PIL import Image, ImageFilter
import os

srcPath = '/media/iit/Transcend/nabila/data-set/test/src/'
dstPath = '/media/iit/Transcend/nabila/data-set/test/dst/'
dirs = os.listdir(srcPath)

# convert images to .jpg and save in a different directory
def image_to_image():
    #count = 4
    for item in dirs:
        #print(count)
        #count += 1
        #if count <= 4:
            #pass
        #else:
            #if count >= 7:
             #   break
        try:
            if os.path.isfile(srcPath + item):
                print(item)
                img = Image.open(srcPath + item)
                # img.show(item)

                file, e = os.path.splitext(dstPath + item)
                img_blur = img.filter(PIL.ImageFilter.BoxBlur(10))
                img_Resize = img.resize((256, 256), Image.ANTIALIAS)
                blur_img_resize = img_blur.resize((256, 256), Image.ANTIALIAS)
                img_Resize.save(file + '.jpg', 'JPEG', quality=90)
                blur_img_resize.save(file + '_blur.jpg', 'JPEG', quality=100)
        except:
            print("\n#######################This is an error message!\n")
            #pass

#image_to_image()

dstPath = "/media/iit/Transcend/nabila/data-set/image_to_image/box_blur/"
mrgPath = "/media/iit/Transcend/nabila/data-set/image_to_image/original_and_box_blur_mrg/"
dirs2 = os.listdir(dstPath)
images = list(map(Image.open, [(dstPath + i) for i in dirs2]))


def mergeImage():
    count = 1
    total_width = 512
    max_height = 256

    new_im = Image.new('RGB', (total_width, max_height))

    x_offset = 0
    i = 0
    j = 0

    for im in images:
        print(count)
        count += 1

        new_im.paste(im, (x_offset, 0))
        x_offset += im.size[0]
        i += 1
        if (i % 2 == 0):
            j += 1
            x_offset = 0
            new_im.save(mrgPath + "box_blur_" + str(j) + '.jpg')
            # new_im.show()

mergeImage()
