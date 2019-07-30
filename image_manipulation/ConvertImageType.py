from PIL import Image
import os

src = '/media/iit/R a i n/2019/ML/pythonprojects/image_manipulation'

#convert and save image in different directory
for filename in os.listdir(src):
    print(filename)

    if filename.endswith('.ppm'):
        print(filename)
        image1 = Image.open(filename)
        # image1.show(filename)
        # image1.save('test.png')

        #convert image extention to .png and save it to different folder
        fn, fext = os.path.splitext(filename)
        print(fext)
        image1.save('pngs/{}.png'.format(fn))






