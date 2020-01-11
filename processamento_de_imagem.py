#!/usr/bin/python3

def show(img, name = "name"):
	cv2.imshow(name, img)
	cv2.waitKey()
	cv2.destroyAllWindows()

def print_size(img):
	print("Width:", len(img))
	print("Height:", len(img[0]))

def centro_gravidade(grayImg, threshold = 127):
	print (grayImg)
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
#cap.set(3,width)
#cap.set(4,height)
#cap.set(15, exposure_time)
ret, img = cap.read()
if (ret != True):
	print ("failed to capture image")
print_size(img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
show(gray, "Escala de cinza")
print_size(gray)

x,y = centro_gravidade(gray)
print(x,y)
