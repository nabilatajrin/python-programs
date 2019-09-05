import os
import csv
from PIL import Image

def main():
    src = '/media/iit/R a i n/2019/ML/pythonprojects/crop_img/src/'
    dst = '/media/iit/R a i n/2019/ML/pythonprojects/crop_img/dst/test/'

    for filename in os.listdir(src):
        try:
            img = Image.open(src + filename)
            file = open(src + "Unilever-export.csv".format(filename), "r")
            reader = csv.reader(file)

            for line in reader:
                if (line[1] == 'xmin'):
                    pass
                elif (filename == line[0]):
                    print('file found')
                    left_x = float(line[1])
                    top_y = float(line[2])
                    right_x = float(line[3])
                    bottom_y = float(line[4])
                    source_file_name = os.path.splitext(line[0])[0]
                    tag_name = line[5]

                    print(left_x, top_y, right_x, bottom_y)

                    area = (left_x, top_y, right_x, bottom_y)
                    img = img.crop(area)

                    #img.save(dst + filename + '_cropped.jpg'), <source_file_name>__<x1_y1>__<tag_name>.png
                    new_name = source_file_name + '__' + line[1] + '_' + line[2] + '__' + tag_name
                    img.save(dst + new_name + '.png')
                    
        except IOError:
            pass

if __name__ == '__main__':
    main()