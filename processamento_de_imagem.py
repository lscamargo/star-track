#!/usr/bin/python3
import numpy as np
import cv2

def show(img, name = "name"):
	cv2.imshow(name, img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

def centro_gravidade(grayImg, threshold = 127):
	height, width = grayImg.shape
	thImg = (grayImg >= threshold) * grayImg
	xcenter, ycenter, w, wTotal = 0, 0, 0, 0
	for x in range(0, width-1):
		for y in range(0, height-1):
			w = thImg[y,x]
			wTotal += w
			xcenter += x*w
			ycenter += y*w
	xcenter /= wTotal
	ycenter /= wTotal
	return xcenter, ycenter

cap = cv2.VideoCapture(0)

while (True):
	ret, img = cap.read()
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	cutGray = gray[0:50,0:50]
	x,y = centro_gravidade(cutGray)
	print(x,y)
	cv2.imshow("recorte", cutGray)
	key = cv2.waitKey(1) & 0xFF
	if(key == ord('q')):
		break
