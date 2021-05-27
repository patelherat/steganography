import numpy as np
import cv2

img1 = cv2.imread('CAT_Kitten_img_31.jpg')

img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2YCrCb)      # converts rgb to ycbcr
cv2.namedWindow('orig-ycrcb', cv2.WINDOW_NORMAL)
cv2.resizeWindow('orig-ycrcb', 600, 600)
cv2.imshow('orig-ycrcb', img1)
# img2 = cv2.cvtColor(img1, cv2.COLOR_BGR2Luv)
# img3 = cv2.cvtColor(img1, cv2.COLOR_BGR2Lab)
y, Cr, Cb = cv2.split(img1)                 # splits ycbcr color space

cv2.namedWindow('cr', cv2.WINDOW_NORMAL)
cv2.resizeWindow('cr', 600, 600)
cv2.imshow('cr', Cr)                    # displays cr color channel

p = []
for i in range(Cr.shape[0]):
    for j in range(Cr.shape[1]):
         p.append(np.binary_repr(Cr[i][j], width=8))  # converts numbers to binary for every pixel in image

# bit planes of an image
# extract ith number and multiply it according to its position(for units place-1, for tens place-2 and so on)
# reshape it to the original image
first = (np.array([int(i[7]) for i in p], dtype=np.uint8) * 1).reshape(Cr.shape[0], Cr.shape[1])
second = (np.array([int(i[6]) for i in p], dtype=np.uint8) * 2).reshape(Cr.shape[0], Cr.shape[1])
third = (np.array([int(i[5]) for i in p], dtype=np.uint8) * 4).reshape(Cr.shape[0], Cr.shape[1])
fourth = (np.array([int(i[4]) for i in p], dtype=np.uint8) * 8).reshape(Cr.shape[0], Cr.shape[1])
fifth = (np.array([int(i[3]) for i in p], dtype=np.uint8) * 16).reshape(Cr.shape[0], Cr.shape[1])
sixth = (np.array([int(i[2]) for i in p], dtype=np.uint8) * 32).reshape(Cr.shape[0], Cr.shape[1])
seventh = (np.array([int(i[1]) for i in p], dtype=np.uint8) * 64).reshape(Cr.shape[0], Cr.shape[1])
eighth = (np.array([int(i[0]) for i in p], dtype=np.uint8) * 128).reshape(Cr.shape[0], Cr.shape[1])

# cv2.namedWindow('one', cv2.WINDOW_NORMAL)
# cv2.resizeWindow('one', 700, 700)
# cv2.imshow('one', first)
#
# cv2.namedWindow('two', cv2.WINDOW_NORMAL)
# cv2.resizeWindow('two', 700, 700)
# cv2.imshow('two', second)
#
# cv2.namedWindow('three', cv2.WINDOW_NORMAL)
# cv2.resizeWindow('three', 700, 700)
# cv2.imshow('three', third)
#
# cv2.namedWindow('four', cv2.WINDOW_NORMAL)
# cv2.resizeWindow('four', 700, 700)
# cv2.imshow('four', fourth)

cv2.namedWindow('five', cv2.WINDOW_NORMAL)
cv2.resizeWindow('five', 700, 700)          # need to do this so that the image don't get clipped
cv2.imshow('five', fifth)

cv2.namedWindow('six', cv2.WINDOW_NORMAL)
cv2.resizeWindow('six', 700, 700)
cv2.imshow('six', sixth)

cv2.namedWindow('seven', cv2.WINDOW_NORMAL)
cv2.resizeWindow('seven', 700, 700)
cv2.imshow('seven', seventh)

cv2.namedWindow('eight', cv2.WINDOW_NORMAL)
cv2.resizeWindow('eight', 700, 700)
cv2.imshow('eight', eighth)
cv2.imwrite("output.jpg", eighth)

cv2.waitKey(0)                              # waits until key is pressed
cv2.destroyAllWindows()
