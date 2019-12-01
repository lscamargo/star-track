#!/bin/python3
import RPi.GPIO as io
import cv2

class output:
    u,d,l,r = 31,33,36,37 #pinos de controle para cima, baixo, esquerda e direita

    def preparar():
        io.setmode(io.BOARD)
        io.setup(u, io.OUT)
        io.setup(d, io.OUT)
        io.setup(l, io.OUT)
        io.setup(r, io.OUT)
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

class cam:
    width = 640
    height = 480
    exposure_time = 0.1

    ExposureMode = 'manual';
    Exposure=-9
    Brightness=235
    WhiteBalance=3500
    Sharpness = 10
    Gain=230
    Saturation=10
    Contrast=150

    ymax = 479
    xmax = 639

    def preparar():
        #capture from camera at location 0
        cap = cv2.VideoCapture(0)
        #set the width and height, and UNSUCCESSFULLY set the exposure time
        cap.set(3,width)
        cap.set(4,height)
        cap.set(15, exposure_time)

    def capturar():
        ret, img = cap.read()
        cv2.imshow("input", img)

#info fisica
d = 1.51e-3         #pupil size = 1.51 mm
l = 635e-9    #Wavelength = 635nm
f = 75e-3       #Focal Length = 75 mm
pixsize = 3.75e-6       #Pixel size

print (d+" "+l+" "+f)

# truncating the image's boundaries to its limits. Makes possible the
# cropping
[ret, img] = cam.capturar()
cv2.imshow("Selecione a Região de Interesse", img)
[x,y] = ginput(1)

if y>cam.ymax-50 :
   y=cam.ymax-50
elif y<50 :
   y=50

if x>xmax-50 :
   x=xmax-50
elif x<50 :
   x=50;

# Acquire a single image.
[ret, rgbImage] = cam.capture()

# Convert RGB to grayscale.
grayImage = rgb2gray(rgbImage);
# Crops the image
grayImageCrop = grayImage[(y-49):(y+49)][(x-49):(49+x)];

# TCOG calculus over the cropped image
[slopey, slopex] = TCOG(double(grayImageCrop),0.8);    #Thresholded center of gravity

#circle coordinates
y_circle=slopey+50;
x_circle=slopex+50;

# Display the image.
cam.imshow("output", grayImageCrop);
plot(x_circle, y_circle, 'ro', 'MarkerSize', 10);

#gera os comandos
if slopey>5 :
    cima()
elif slopey<-5 :
    baixo
else:
    parado()

if slopex<-5 :
    direita()
elif slopex>5 :
    esquerda()
else:
    parado()
