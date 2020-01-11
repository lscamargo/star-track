#!/usr/bin/python3

def show(img, name = "name"):
	cv2.imshow(name, img)
	cv2.waitKey()
	cv2.destroyAllWindows()

def print_size(img):
	print("Width:", len(img))
	print("Height:", len(img[0]))
	#print("Colors:", len(img[0][0]))


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
