#!/usr/bin/python3
import numpy as np

def show(img, name = "name"):
	cv2.imshow(name, img)
	cv2.waitKey()
	cv2.destroyAllWindows()

def print_size(img):
	print("Width:", len(img))
	print("Height:", len(img[0]))

def centro_gravidade(grayImg, threshold = 127):
	width = len(grayImg)
	height = len(grayImg[0])
	thImg = (grayImg >= threshold) * grayImg

	xcenter, ycenter, w, wTotal = 0, 0, 0, 0
	for x in range(0, width-1):
		for y in range(0, height-1):
			w = thImg[x][y]
			wTotal += w
			xcenter += x*w
			ycenter += y*w
	xcenter /= wTotal
	ycenter /= wTotal
	return xcenter, ycenter

import cv2
width = 640
height = 480
exposure_time = 0.1

cap = cv2.VideoCapture(0)

w, h = 3, 3;
Matrix = np.matrix([[0 for x in range(w)] for y in range(h)])
Matrix[0][0]=1
print(Matrix)
x,y = centro_gravidade(Matrix, 0)
print(x,y)

while (False):
	ret, img = cap.read()
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	cv2.imshow("Escala de cinza", gray)
	x,y = centro_gravidade(gray)
	print(x,y)
	key = cv2.waitKey(1) & 0xFF 
	if (key == ord('q')) :
		break
