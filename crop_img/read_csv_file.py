import csv

path = '/media/iit/R a i n/2019/ML/pythonprojects/crop_img/'
filename = "images"

file = open( path + "test.csv".format(filename), "r")
reader = csv.reader(file)

for line in reader:
    #t = line[0], line[1], line[2], line[3], line[4], line[5]
    #print( t )



    if (line[1] == 'xmin' or line[2] == 'ymin' or line[3] == 'xmax' or line[4] == 'ymax'):
        pass
    else:
        left_x = float(line[1])
        top_y = float(line[2])
        right_x = float(line[3])
        bottom_y = float(line[4])
        print(left_x, top_y, right_x, bottom_y)
