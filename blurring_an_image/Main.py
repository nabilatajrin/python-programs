from PIL import Image

image1 = Image.open('test.ppm')
image2 = Image.open('treepic.jpg')
image1.show()
image2.show()
image1.save('test.png')


