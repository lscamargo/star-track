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
    def cima(self):
        io.output(self.u, io.LOW)
        io.output(self.d, io.HIGH)
        io.output(self.l, io.HIGH)
        io.output(self.r, io.HIGH)
    def baixo(self):
        io.output(self.u, io.HIGH)
        io.output(self.d, io.LOW)
        io.output(self.l, io.HIGH)
        io.output(self.r, io.HIGH)
    def esquerda(self):
        io.output(self.u, io.HIGH)
        io.output(self.d, io.HIGH)
        io.output(self.l, io.LOW)
        io.output(self.r, io.HIGH)
    def direita(self):
        io.output(self.u, io.HIGH)
        io.output(self.d, io.HIGH)
        io.output(self.l, io.HIGH)
        io.output(self.r, io.LOW)
    def parado(self):
        io.output(self.u, io.HIGH)
        io.output(self.d, io.HIGH)
        io.output(self.l, io.HIGH)
        io.output(self.r, io.HIGH)

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
	
	ymax = height-1
	xmax = width-1
	
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
		mouseX, mouseY, mouseFlag = -1, -1, 0
		cv2.namedWindow("Selecione a Região de Interesse")
		cv2.setMouseCallback("Selecione a Região de Interesse", get_mouse_position)
		ret, img = cam.capturar()
		if (ret == 0) :
			print ("Falha o capturar")
			return -1, -1, -1
		center_img = display.getCenter(img)
		cv2.imshow("Selecione a Região de Interesse", center_img)
		
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
				
def move_test():
	ret, img = cam.capturar()
	if (ret == 0) :
		print ("Falha o capturar")
		return -1, -1, -1
	center_img = display.getCenter(img)
	cv2.imshow("Teste de movimento", center_img)
	while( True) :
		key = cv2.waitKey(1) & 0xFF 
		if (key == ord('q')) :
			print ("Q button pressed.")
			sys.exit(0)
		if (key == ord('u')) :
			print ("U button pressed.")
			out.cima()
		if (key == ord('d')) :
			print ("D button pressed.")
			out.baixo()
		if (key == ord('l')) :
			print ("L button pressed.")
			out.esquerda()
		if (key == ord('r')) :
			print ("R button pressed.")
			out.direita()


def get_mouse_position(event,x,y,flags,param):
	global mouseX, mouseY, mouseFlag
	if event == cv2.EVENT_LBUTTONUP:
		print('Mouse flag detected click', x, y, mouseFlag)
		mouseX, mouseY = x,y
		mouseFlag = 1
		print("mouseFlag =", mouseFlag)

class displayClass :
	height = 480
	width = 320
	def getCenter(self, image) :
		camWidth, camHeight, channels = image.shape
		x = int((camWidth - self.width)/2)
		y = int((camHeight - self.height)/2)
		outImage = image[x:x+self.width, y:y+self.height]
		return outImage
	
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
display = displayClass()
out = outputClass()
#ret, img = cam.capturar()
#cv2.imshow("imagem capturada", img)
#cv2.waitKey(0)
#cv2.destroyWindow("imagem capturada")
move_test()
