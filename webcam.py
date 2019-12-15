#!/usr/bin/python3
import RPi.GPIO as io
import cv2
import time
import sys

class outputClass:
    u,d,l,r = 31,33,36,37 #pinos de controle para cima, baixo, esquerda e direita

    def __init__(self):
        io.setmode(io.BOARD)
        io.setup(self.u, io.OUT)
        io.setup(self.d, io.OUT)
        io.setup(self.l, io.OUT)
        io.setup(self.r, io.OUT)
    def cima():
        io.output(u, io.LOW)
        io.output(d, io.HIGH)
        io.output(l, io.HIGH)
        io.output(r, io.HIGH)
    def baixo():
        io.output(u, io.HIGH)
        io.output(d, io.LOW)
        io.output(l, io.HIGH)
        io.output(r, io.HIGH)
    def esquerda():
        io.output(u, io.HIGH)
        io.output(d, io.HIGH)
        io.output(l, io.LOW)
        io.output(r, io.HIGH)
    def direita():
        io.output(u, io.HIGH)
        io.output(d, io.HIGH)
        io.output(l, io.HIGH)
        io.output(r, io.LOW)
    def parado():
        io.output(u, io.HIGH)
        io.output(d, io.HIGH)
        io.output(l, io.HIGH)
        io.output(r, io.HIGH)

class camClass:
	width = 640
	height = 480
	exposure_time = 0.1
	
	ExposureMode = 'manual'
	Exposure=-9
	Brightness=235
	WhiteBalance=3500
	Sharpness = 10
	Gain=230
	Saturation=10
	Contrast=150
	
	ymax = 479
	xmax = 639
	
	def __init__(self):
		#capture from camera at location 0
		self.cap = cv2.VideoCapture(0)
		time.sleep(2)
		print('Opened camera: ', self.cap)
		#set the width and height, and UNSUCCESSFULLY set the exposure time
		#self.cap.set(3,self.width)
		#self.cap.set(4,self.height)
		#self.cap.set(15, self.exposure_time)

	def capturar(self):
		ret, img = self.cap.read()
		print('Read camera. ret = ', ret)
		#while(True):
		#	ret, img = self.cap.read()
			#print('ret=', ret, ' img=',img)
			#if cv2.waitKey(1) & 0xFF == ord('q'):
			#	break
		return ret, img
	
class uiClass :
	def select_roi (self):
		global mouseX, mouseY, mouseFlag
		print ("Mouse click detectado")
		mouseX, mouseY, mouseFlag = -1, -1, 0
		cv2.namedWindow("Selecione a Região de Interesse")
		cv2.setMouseCallback("Selecione a Região de Interesse", get_mouse_position)
		ret, img = cam.capturar()
		if (ret == 0) :
			print ("Falha o capturar")
			return -1, -1, -1
		cv2.imshow("Selecione a Região de Interesse", img)
		
		print ("Clique na imagem para selecionar uma estrela")

		print("mouseFlag =", mouseFlag)

		while( True) :
			key = cv2.waitKey(1) & 0xFF 
			if (key == ord('q')) :
				print ("Q button pressed.")
				sys.exit(0)
			if (key == ord('\n')) :
				print ("Enter button pressed.")
				print("mouseFlag =", mouseFlag)

			if (mouseFlag == 1) :
				print ("Mouse click detectado")
				return 0, mouseX, mouseY
				

def get_mouse_position(event,x,y,flags,param):
	global mouseX, mouseY, mouseFlag
	if event == cv2.EVENT_LBUTTONUP:
		print('Mouse flag detected click', x, y, mouseFlag)
		mouseX, mouseY = x,y
		mouseFlag = 1
		print("mouseFlag =", mouseFlag)

#info fisica
d = 1.51e-3         #pupil size = 1.51 mm
l = 635e-9    #Wavelength = 635nm
f = 75e-3       #Focal Length = 75 mm
pixsize = 3.75e-6       #Pixel size

print ('d= ', d, "l= ", l, "f= ", f)

#mouse global variables
mouseX, mouseY, mouseFlag = -1, -1, 0

# truncating the image's boundaries to its limits. Makes possible the
# cropping
cam = camClass()
ui = uiClass()
#ret, img = cam.capturar()
#cv2.imshow("imagem capturada", img)
#cv2.waitKey(0)
#cv2.destroyWindow("imagem capturada")
ret, x, y = ui.select_roi()
if (ret > 0):
	print("Closing application")
	sys.exit(0)

if (y>cam.ymax-50) :
	y=cam.ymax-50
elif (y<50) :
	y=50

if (x>cam.xmax-50) :
   x=cam.xmax-50
elif x<50 :
   x=50

## Convert RGB to grayscale.
#grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);
## Crops the image
#grayImageCrop = grayImage[(y-49):(y+49)][(x-49):(49+x)];
#
## TCOG calculus over the cropped image
#[slopey, slopex] = TCOG(double(grayImageCrop),0.8);    #Thresholded center of gravity
#
##circle coordinates
#y_circle=slopey+50;
#x_circle=slopex+50;
#
## Display the image.
#cam.imshow("output", grayImageCrop);
#plot(x_circle, y_circle, 'ro', 'MarkerSize', 10);
#
##gera os comandos
#if slopey>5 :
#    cima()
#elif slopey<-5 :
#    baixo
#else:
#    parado()
#
#if slopex<-5 :
#    direita()
#elif slopex>5 :
#    esquerda()
#else:
#    parado()
