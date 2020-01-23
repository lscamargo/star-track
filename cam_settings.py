#!/usr/bin/python3
import cv2
import time

class camClass:
	Width = 320
	Height = 240
	exposure_time = -5
	Brightness=235
	Gain=100
	Saturation=1
	Contrast=150
	
	ymax = Height-1
	xmax = Width-1
	
	def __init__(self):
		self.cap = cv2.VideoCapture(1)
		time.sleep(2)
		print('Opened camera: ', self.cap)

		self.cap.set(3, self.Width)	#CV_CAP_PROP_FRAME_WIDTH 
		self.cap.set(4, self.Height)	#CV_CAP_PROP_FRAME_HEIGHT
		self.cap.set(10, self.Brightness)	#CV_CAP_PROP_BRIGHTNESS
		self.cap.set(11, self.Contrast)	#CV_CAP_PROP_CONTRAST
		self.cap.set(12, self.Saturation)	#CV_CAP_PROP_SATURATION
		self.cap.set(14, self.Gain)	#CV_CAP_PROP_GAIN
		time.sleep(2)
		self.cap.set(15, self.exposure_time)	#CV_CAP_PROP_EXPOSURE
		
		#capture from camera at location 0
				#set the width and height, and UNSUCCESSFULLY set the exposure time
		#self.cap.set(3,self.width)
		#self.cap.set(4,self.height)
		#self.cap.set(15, self.exposure_time)

	def capturar(self):
		ret, img = self.cap.read()
		#print('Read camera. ret = ', ret)
		#while(True):
		#	ret, img = self.cap.read()
			#print('ret=', ret, ' img=',img)
			#if cv2.waitKey(1) & 0xFF == ord('q'):
			#	break
		return ret, img

cam = camClass()

while(True):
	ret, img = cam.capturar()
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	cv2.imshow("ROI", img)
	key = cv2.waitKey(1) & 0xFF
	if(key == ord('q')):
		break
	elif(key == ord('b')):
		print("Brightness=", cam.Brightness)
		cam.Brightness+=1
		cam.cap.set(10, cam.Brightness)
	elif(key == ord('v')):
		print("Brightness=", cam.Brightness)
		cam.Brightness-=1
		cam.cap.set(10, cam.Brightness)
	elif(key == ord('e')):
		print("Exposure=", cam.exposure_time)
		cam.exposure_time+=0.1
		cam.cap.set(15, cam.exposure_time)
	elif(key == ord('w')):
		print("Exposure=", cam.exposure_time)
		cam.exposure_time-=0.1
		cam.cap.set(15, cam.exposure_time)
	elif(key == ord('c')):
		print("Contrast=", cam.Contrast)
		cam.Contrast+=1
		cam.cap.set(11, cam.Contrast)
	elif(key == ord('x')):
		print("Contrast=", cam.Contrast)
		cam.Contrast-=1
		cam.cap.set(11, cam.Contrast)
	elif(key == ord('s')):
		print("Saturation=", cam.Saturation)
		cam.Saturation+=1
		cam.cap.set(12, cam.Saturation)
	elif(key == ord('a')):
		print("Saturation=", cam.Saturation)
		cam.Saturation-=1
		cam.cap.set(12, cam.Saturation)
	elif(key == ord('g')):
		print("Gain=", cam.Gain)
		cam.Gain+=1
		cam.cap.set(14, cam.Gain)
	elif(key == ord('f')):
		print("Gain=", cam.Gain)
		cam.Gain-=1
		cam.cap.set(14, cam.Gain)

