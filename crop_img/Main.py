import csv
from io import BytesIO
import requests
from PIL import Image
import matplotlib.pyplot as plt

filename = "images"

# open file to read
with open("test.csv".format(filename), 'r') as csvfile:
    reader = csv.reader(csvfile)
    # pop header row (1st row in csv)
    header = next(reader)

    # iterate on all lines
    i = 0
    for line in csvfile:
        splitted_line = line.split(',')
        # check if we have an image URL
        if splitted_line[1] != '' and splitted_line[1] != "\n":
            response = requests.get(splitted_line[1])
            img = Image.open(BytesIO(response.content))

            #im.crop(box) ⇒ 4-tuple defining the left, upper, right, and lower pixel coordinate
            left_x = int(splitted_line[2])
            top_y = int(splitted_line[3])
            right_x = int(splitted_line[4])
            bottom_y = int(splitted_line[5])
            crop = img.crop((left_x, top_y, right_x, bottom_y))
            new_img = crop.resize((256, 256))
            """ 
            # preview new images
            imgplot = plt.imshow(new_img)
            plt.show()
            """
            new_img.save(str(i) + ".png")
            print("Image saved for {0}".format(splitted_line[0]))
            i += 1
        else:
            print("No result for {0}".format(splitted_line[0]))
