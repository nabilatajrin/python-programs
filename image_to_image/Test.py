import cv2
import numpy as np

img = cv2.imread('/media/iit/R a i n/2019/Intelligent Machines Ltd/face-propagation/dummy-data-set/colorferet/colorferet/test_blur/src_blur/00002_940128_fa.ppm')
cv2.imshow('Original', img)

size = 15

# generating the kernel
kernel_motion_blur = np.zeros((size, size))
kernel_motion_blur[int((size-1)/2), :] = np.ones(size)
kernel_motion_blur = kernel_motion_blur / size

# applying the kernel to the input image
output = cv2.filter2D(img, -1, kernel_motion_blur)

cv2.imshow('Motion Blur', output)
cv2.waitKey(0)

dstPath = "/media/iit/R a i n/2019/Intelligent Machines Ltd/face-propagation/dummy-data-set/colorferet/colorferet/test_blur/motion_blur/"

cv2.output.save(dstPath + '.jpg', 'JPEG', quality = 90)