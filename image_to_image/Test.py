# convert and save images in different directory
def convertImageType():
    for item in dirs:
        if os.path.isfile(srcPath + item):
            print(item)

            if item.endswith('.ppm'):
                print(item)
                convertImage = Image.open(item)
                # convertImage.show(filename)
                # convertImage.save('test.png')

                # convert images to .png and save it to different folder
                fn, fext = os.path.splitext(item)
                print(fext)
                convertImage.save(dstPath + '{}.jpg'.format(fn))


convertImageType()

#test
def gaussianBlur():
    for item in dirs:
        if os.path.isfile(srcPath + item):
            im = Image.open(srcPath + item)
            file, e = os.path.splitext(dstPath + item)
            imblur = im.filter(ImageFilter.GaussianBlur(10))
            imblur.save(file + '.jpg', 'JPEG', quality = 90)

gaussianBlur()