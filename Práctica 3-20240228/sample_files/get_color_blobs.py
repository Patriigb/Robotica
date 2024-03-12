# -*- coding: utf-8 -*-
#!/usr/bin/python

# Standard imports
import cv2
import numpy as np;

def main():
	# Read image
	img_BGR = cv2.imread("red_blue.jpg")
	#img_BGR = cv2.imread("many.jpg")

	# Setup default values for SimpleBlobDetector parameters.
	params = cv2.SimpleBlobDetector_Params()

	# These are just examples, tune your own if needed
	# Change thresholds
	params.minThreshold = 10
	params.maxThreshold = 200

	# Filter by Area
	params.filterByArea = True
	params.minArea = 200
	params.maxArea = 10000

	# Filter by Circularity
	params.filterByCircularity = True
	params.minCircularity = 0.1

	# Filter by Color
	params.filterByColor = False
	# not directly color, but intensity on the channel input
	#params.blobColor = 0
	params.filterByConvexity = False
	params.filterByInertia = False


	# Create a detector with the parameters
	ver = (cv2.__version__).split('.')
	if int(ver[0]) < 3 :
		detector = cv2.SimpleBlobDetector(params)
	else :
		detector = cv2.SimpleBlobDetector_create(params)

	# keypoints on original image (will look for blobs in grayscale)
	keypoints = detector.detect(img_BGR)
	# Draw detected blobs as red circles.
	# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures
	# the size of the circle corresponds to the size of blob
	im_with_keypoints = cv2.drawKeypoints(img_BGR, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

	# Show blobs
	cv2.imshow("Keypoints on Gray Scale", im_with_keypoints)
	cv2.waitKey(0)

	# filter certain COLOR channels

	# Pixels with 100 <= R <= 255, 15 <= B <= 56, 17 <= G <= 50 will be considered red.
	# similar for BLUE

	# BY DEFAULT, opencv IMAGES have BGR format
	redMin = (10, 10, 100)
	redMax = (50, 50, 255)

	blueMin=(60, 10, 10)
	blueMax=(255, 100, 100)

	mask_red=cv2.inRange(img_BGR, redMin, redMax)
	mask_blue=cv2.inRange(img_BGR, blueMin, blueMax)


	# apply the mask
	red = cv2.bitwise_and(img_BGR, img_BGR, mask = mask_red)
	blue = cv2.bitwise_and(img_BGR, img_BGR, mask = mask_blue)
	# show resulting filtered image next to the original one
	cv2.imshow("Red regions", np.hstack([img_BGR, red]))
	cv2.imshow("Blue regions", np.hstack([img_BGR, blue]))


	# detector finds "dark" blobs by default, so invert image for results with same detector
	keypoints_red = detector.detect(255-mask_red)
	keypoints_blue = detector.detect(255-mask_blue)

	# documentation of SimpleBlobDetector is not clear on what kp.size is exactly, but it looks like the diameter of the blob.
	for kp in keypoints_red:
		print (kp.pt[0], kp.pt[1], kp.size)

	# Draw detected blobs as red circles.
	# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures
	# the size of the circle corresponds to the size of blob
	im_with_keypoints = cv2.drawKeypoints(img_BGR, keypoints_red, np.array([]),
		(255,255,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
	im_with_keypoints2 = cv2.drawKeypoints(img_BGR, keypoints_blue, np.array([]),
		(255,255,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)




	#PREVIO:
	AREA = 15000

	# Centro de la imagen
	h, w = img_BGR.shape[:2]
	center = (w // 2, h // 2)
	print("Centro de la imagen", center)
	# Dibujar el centro
	cv2.circle(im_with_keypoints, center, 2, (0, 0, 0), -1)

	# Centro del blob
	x, y = int(kp.pt[0]), int(kp.pt[1])
	print("Centro del blob", x, y)
	# Dibujarlo
	cv2.circle(im_with_keypoints, (x, y), 2, (0, 0, 0), -1)

	# Calcular distancia entre centro de la imagen y centro del blob
	distance = np.sqrt((center[0] - x)**2 + (center[1] - y)**2)
	print("Distancia entre los centros",distance)

	# Calcular area del blob
	area = np.pi * (kp.size/2)**2
	print("Area del blob", area)

	# Dibujar circulo con AREA
	cv2.circle(im_with_keypoints, center, int(np.sqrt(AREA/np.pi)), (0, 255, 0), 1)

	# Diferencia de areas
	diff = AREA - area
	print("Diferencia de areas", diff)


	# Show mask and blobs found 
	cv2.imshow("Keypoints on RED", im_with_keypoints)
	cv2.imshow("Keypoints on BLUE", im_with_keypoints2)
	cv2.waitKey(0)

