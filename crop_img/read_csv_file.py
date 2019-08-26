import csv

path = '/media/iit/R a i n/2019/ML/pythonprojects/crop_img/'
filename = "images"

file = open( path + "Uniliver-export.csv".format(filename), "r")
reader = csv.reader(file)

for line in reader:
    t = line[0], line[1], line[2], line[3], line[4], line[5]
    print( t )