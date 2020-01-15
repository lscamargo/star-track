#!/usr/bin/python3
import numpy as np

def show(img, name = "name"):
	cv2.imshow(name, img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

def centro_gravidade(grayImg, threshold = 127):
	height, width = grayImg.shape
	#print("width = ", width)
	#print("height = ", height)
	#thImg = np.zeros((width, height))
	thImg = (grayImg >= threshold) * grayImg
	cv2.waitKey(0)
	xcenter, ycenter, w, wTotal = 0, 0, 0, 0
	for x in range(0, width-1):
		for y in range(0, height-1):
			w = thImg[y,x]
			#print("w = ", w)
			wTotal += w
			#print("wTotal = ", wTotal)
			xcenter += x*w
			ycenter += y*w
	print("wTotal = ", wTotal)
	xcenter /= wTotal
	ycenter /= wTotal
	return xcenter, ycenter

import cv2
width = 640
height = 480
exposure_time = 0.1

cap = cv2.VideoCapture(0)

#w, h = 3, 5;
#Matrix = np.matrix([[0 for x in range(w)] for y in range(h)])
#Matrix[0,0] = 2
#Matrix[0,1] = 2
#Matrix[0,2] = 2
#Matrix[1,0] = 2
#Matrix[2,0] = 2
#print(Matrix)
#x,y = centro_gravidade(Matrix, 0)
#print(x,y)

ret, img = cap.read()
show(img)

while (True):
	ret, img = cap.read()
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	cutGray = gray[0:100,0:70]
	cutGray[00:10,50:70] = np.ones((10,20)) * 255
	x,y = centro_gravidade(cutGray)
	cv2.imshow("recorte", cutGray)
	key = cv2.waitKey(1) & 0xFF
	print(x,y)
	if(key == ord('q')):
		break
