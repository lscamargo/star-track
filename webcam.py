#!/bin/python3
import RPi.GPIO as io
import cv2

class output:
    int u=31, d=33, l=36, r=37 #pinos de controle para cima, baixo, esquerda e direita
    preparar()
        io.setmode(io.BOARD)
        io.setup(u, io.OUT)
        io.setup(d, io.OUT)
        io.setup(l, io.OUT)
        io.setup(r, io.OUT)
    cima()
        io.output(u, io.LOW)
        io.output(d, io.HIGH)
        io.output(l, io.HIGH)
        io.output(r, io.HIGH)
    baixo()
        io.output(u, io.HIGH)
        io.output(d, io.LOW)
        io.output(l, io.HIGH)
        io.output(r, io.HIGH)
    esquerda()
        io.output(u, io.HIGH)
        io.output(d, io.HIGH)
        io.output(l, io.LOW)
        io.output(r, io.HIGH)
    direita()
        io.output(u, io.HIGH)
        io.output(d, io.HIGH)
        io.output(l, io.HIGH)
        io.output(r, io.LOW)
    parado()
        io.output(u, io.HIGH)
        io.output(d, io.HIGH)
        io.output(l, io.HIGH)
        io.output(r, io.HIGH)

class cam:
    width = 640
    height = 480
    exposure_time = 0.1

    preparar()
        #capture from camera at location 0
        cap = cv2.VideoCapture(0)
        #set the width and height, and UNSUCCESSFULLY set the exposure time
        cap.set(3,width)
        cap.set(4,height)
        cap.set(15, exposure_time)

    capturar()
        ret, img = cap.read()
        cv2.imshow("input", img)

#info fisica
d = 1.51e-3;         #pupil size = 1.51 mm
lambda = 635e-9;    #Wavelength = 635nm
f = 75e-3;       #Focal Length = 75 mm
pixsize = 3.75e-6;       #Pixel size

##############
#info resol cam
ymax= 479;
xmax= 639;

#info = imaqhwinfo; para saber o nome da camera

#vid = videoinput('dcam',1,'Y8_1024x768')
#vid = videoinput('dcam');
cam = webcam(1); #1 escolhe a logitech
preview(cam)

cam.ExposureMode = 'manual';
cam.Exposure=-9
cam.Brightness=235
cam.WhiteBalance=3500
cam.Sharpness = 10
cam.Gain=230
cam.Saturation=10
cam.Contrast=150

# truncating the image's boundaries to its limits. Makes possible the
# cropping
img = snapshot(cam);
imshow(img)
[x,y] = ginput(1)
    if y>ymax-50
       y=ymax-50;
    elseif y<50
       y=50
    end

    if x>xmax-50
       x=xmax-50;
    elseif x<50
       x=50;
    end


for k= 1:100

 # Acquire a single image.
 rgbImage = snapshot(cam);

 # Convert RGB to grayscale.
 grayImage = rgb2gray(rgbImage);
 # Crops the image
 grayImageCrop = grayImage(((y-49):(y+49)),((x-49):(49+x)));

 # TCOG calculus over the cropped image
 [slopey, slopex] = TCOG(double(grayImageCrop),0.8);    #Thresholded center of gravity




#circle coordinates
       y_circle=slopey+50;
       x_circle=slopex+50;


# Display the image.
imshow(grayImageCrop);
hold on;
plot(x_circle, y_circle, 'ro', 'MarkerSize', 10);


#gera os comandos
if slopey>5
    cima()
elseif slopey<-5
    baixo
else
    parado()
end
if slopex<-5
    direita()
elseif slopex>5
    esquerda()
    else
    parado()
end
#desenha circulo onde encontra

  # viscircles([236.053891007202,173.628728230168], 100,'EdgeColor','b');
  # drawnow

   #pause
pause(0.2); #use timer para chamar callback

end



#desenha na tela em vermelho onde esta selecionando



#desliga
pause(5); #use timer para chamar callback
close all; #fecha janelas
clear('cam')
