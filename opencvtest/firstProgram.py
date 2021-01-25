import numpy as np
import cv2

#read the image
img = cv2.imread("/media/iit/R a i n/2019/ML/pythonprojects/3b.ppm")
#display the image
cv2.namedWindow("Image 3b.ppm", cv2.WINDOW_NORMAL)
cv2.imshow("Image 3b.ppm", img)
#wait for milli-seconds
cv2.waitKey(0)
#save the image
cv2.imwrite("/media/iit/R a i n/2019/ML/pythonprojects/opencvtest/3b.jpg", img)
exit()
