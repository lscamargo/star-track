#!/usr/bin/python3
import RPi.GPIO as io
import cv2
import time
import sys
import math
from matplotlib import pyplot as plt
import numpy as np

class outputClass:
	u,d,l,r = 33,37,36,31 #pinos de controle para cima, baixo, esquerda e direita
	def __init__(self):
		io.setmode(io.BOARD)
		io.setup(self.u, io.OUT)
		io.setup(self.d, io.OUT)
		io.setup(self.l, io.OUT)
		io.setup(self.r, io.OUT)
	def cima(self):
		print("cima")
		self.write(0,1,1,1)
	def baixo(self):
		print("baixo")
		self.write(1,0,1,1)
	def esquerda(self):
		print("esquerda")
		self.write(1,1,0,1)
	def direita(self):
		print("direita")
		self.write(1,1,1,0)
	def parado(self):
		print("parado")
		self.write(1,1,1,1)
	def write(self, du, dd, dl, dr):
		io.output(self.u, self.hl(du))
		io.output(self.d, self.hl(dd))
		io.output(self.l, self.hl(dl))
		io.output(self.r, self.hl(dr))
	def hl(self, x):
		if (x == 0):
			return io.LOW
		else:
			return io.HIGH

class camClass:
	Width = 320
	Height = 240
	exposure_time = -5
	Brightness=255
	Gain=100
	Saturation=0
	Contrast=255
	
	ymax = Height-1
	xmax = Width-1
	
	def __init__(self):
		self.cap = cv2.VideoCapture(0)
		time.sleep(2)
		print('Opened camera: ', self.cap)

		self.cap.set(3, self.Width)	#CV_CAP_PROP_FRAME_WIDTH 
		self.cap.set(4, self.Height)	#CV_CAP_PROP_FRAME_HEIGHT
		self.cap.set(10, self.Brightness)	#CV_CAP_PROP_BRIGHTNESS
		self.cap.set(11, self.Contrast)	#CV_CAP_PROP_CONTRAST
		self.cap.set(12, self.Saturation)	#CV_CAP_PROP_SATURATION
		#self.cap.set(14, self.Gain)	#CV_CAP_PROP_GAIN
		#self.cap.set(15, self.exposure_time)	#CV_CAP_PROP_EXPOSURE
		
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
	
class roiClass :
	roi_width = 50
	roi_height = 50
	def get_click (self):
		global mouseX, mouseY, mouseFlag
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
				print ("Botão Q pressionado. Saindo.")
				sys.exit(0)
			if (key == ord('\n')) :
				print ("Botão Enter pressionado.")
				print("mouseFlag =", mouseFlag)
			if (mouseFlag == 1) :
				print ("Mouse click detectado")
				cv2.destroyAllWindows()
				return 0, mouseX, mouseY
	def get_indexes (self, x, y, w, h):
		roi_width = self.roi_width
		roi_height = self.roi_height
		if(x < roi_width/2):
			xa = 0
			xb = roi_width
		elif(x + roi_width/2 > w):
			xa = w - roi_width
			xb = w
		else:
			xa = x - roi_width/2
			xb = x + roi_width/2

		if(y < roi_height/2):
			ya = 0
			yb = roi_height
		elif(y + roi_height/2 > h):
			ya = h - roi_height
			yb = h
		else:
			ya = y - roi_height/2
			yb = y + roi_height/2
		return int(xa), int(xb), int(ya), int(yb)


def get_mouse_position(event,x,y,flags,param):
	global mouseX, mouseY, mouseFlag
	if event == cv2.EVENT_LBUTTONUP:
		#print('Mouse flag detected click', x, y, mouseFlag)
		mouseX, mouseY = x,y
		mouseFlag = 1
		#print("mouseFlag =", mouseFlag)

class displayClass :
	width = 640
	height = 480
	def getCenter(self, image) :
		camWidth, camHeight, channels = image.shape
		x = int((camWidth - self.width)/2)
		y = int((camHeight - self.height)/2)
		outImage = image[x:x+self.width, y:y+self.height]
		return outImage

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

def show(img, name = "name"):
	cv2.imshow(name, img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

def draw_cross(img, xf, yf):
	if (math.isnan(xf) or math.isnan(yf)) :
		return
	x = int(xf)
	y = int(yf)
	l = 5
	color = (0, 255, 0)
	#ponto_inicial = (y-l, x)
	#ponto_final = (y+l, x)
	ponto_inicial = (x, y-l)
	ponto_final = (x, y+l)
	x
	y
	l
	ponto_inicial
	ponto_final
	img = cv2.line(img, ponto_inicial, ponto_final, color, 1)
	ponto_inicial = (x-l, y)
	ponto_final = (x+l, y)
	img = cv2.line(img, ponto_inicial, ponto_final, color, 1)

class controlClass:
	offset = 4
	estado = "P"
	#def __init__(self):
	#	self.offset = 0
	#	self.estado = "P"
	def on_off(self, x, y, xt, yt):
		print(x)
		print(y)
		print(xt)
		print(yt)
		xe = x-xt
		ye = y-yt
		print(xe)
		print(ye)
		if(abs(xe) > abs(ye)):
			if (xe > 0 + self.offset/2):
				self.change("E")
				out.esquerda()
			elif(xe < 0 - self.offset/2):
				self.change("D")
				out.direita()
			else:
				self.change("P")
				out.parado()
		else:
			if (ye > 0 + self.offset/2):
				self.change("C")
				out.cima()
			elif(ye < 0 - self.offset/2):
				self.change("B")
				out.baixo()
			else:
				self.change("P")
				out.parado()

	def change(self, novo_estado):
		if(self.estado != novo_estado):
			print("change")
			time.sleep(0.5)
			self.estado = novo_estado

class graficoErroClass:
	def __init__(self):
		self.tempo_inicial = time.time()
		self.tamanho_max = 300
		self.tamanho = 0
		self.x_list = []
		self.y_list = []
		self.t_list = []
	def add(self, x, y, t):
		self.tamanho += 1
		print("Tamanho = ", self.tamanho)
		if(self.tamanho > self.tamanho_max):
			return
		self.x_list += [y]
		self.y_list += [x]
		self.t_list += [(int)(t-self.tempo_inicial)]
	def plot(self):
		plt.plot(self.x_list, label='x')
		plt.plot(self.y_list, label='y')
		#personaliza labels do eixo x:
		y_pos = np.arange(len(self.t_list))
		plt.xticks(y_pos, self.t_list, color='orange', fontsize='8')
		plt.title('Gráfico do Centro de Gravidade em função do tempo')
		plt.ylabel('Centro de Gravidade')
		plt.show()

	
#info fisica
d = 1.51e-3         #pupil size = 1.51 mm
l = 635e-9    #Wavelength = 635nm
f = 75e-3       #Focal Length = 75 mm
pixsize = 3.75e-6       #Pixel size

print ('d= ', d, "l= ", l, "f= ", f)

#Variáveis globais do mouse
mouseX, mouseY, mouseFlag = -1, -1, 0

#initializa classes
cam = camClass()
roi = roiClass()
display = displayClass()
control = controlClass()
out = outputClass()
graficoErro = graficoErroClass()

ret, x, y = roi.get_click()
xa, xb, ya, yb = roi.get_indexes(x, y, display.width, display.height)
print(xa, xb, ya, yb)
while(True):
	ret, img = cam.capturar()
	#show(img)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	#cv2.imshow("ROI", gray)
	img_roi = gray[ya:yb,xa:xb]
	x, y = centro_gravidade(img_roi, 180)
	graficoErro.add(x, y, time.time())
	print(x, y)
	img_roi_color = img[ya:yb,xa:xb]
	draw_cross(img_roi_color, x, y)
	cv2.imshow("ROI", img_roi_color)
	control.on_off(x, y, roi.roi_width/2, roi.roi_height/2)
	key = cv2.waitKey(167) & 0xFF #60Hz
	if(key == ord('q')):
		out.parado()
		break
	if(key == ord('s')):
		graficoErro.plot()
		cv2.waitKey(0)
