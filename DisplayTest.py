import sys
import cv2
import digitalio
import time
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789

from picamera2 import Picamera2

spi = board.SPI()

cs_pin1 = digitalio.DigitalInOut(board.D22)
cs_pin1.direction = digitalio.Direction.OUTPUT

cs_pin2 = digitalio.DigitalInOut(board.D23)
cs_pin2.direction = digitalio.Direction.OUTPUT

dc_pin = digitalio.DigitalInOut(board.D25)
dc_pin.direction = digitalio.Direction.OUTPUT

reset_pin = digitalio.DigitalInOut(board.D24)
reset_pin.direction = digitalio.Direction.OUTPUT

FPS_BAUDRATE=32000000

Disp1 = st7789.ST7789(
	spi,
	cs=cs_pin1,
	dc=dc_pin,
	rst=reset_pin,
	baudrate=32000000,
	width=240,
	height=320,
	x_offset=0,
	y_offset=0,
)
Disp2 = st7789.ST7789(
	spi,
	cs=cs_pin2,
	dc=dc_pin,
	rst=reset_pin,
	baudrate=32000000,
	width=240,
	height=320,
	x_offset=0,
	y_offset=0,
)

w1, h1,= Disp1.width, Disp1.height
w2, h2 = Disp2.width, Disp2.height

print("initializing cams")

try: 
	cam1 = Picamera2(0)
	print("CAMERA 1 INITIALIZED")
except Exception:
	print("CRITICAL ERROR ON CAMERA ONE, FALLBACK.")
	sys.exit

try: 
	cam2 = Picamera2(1)
	print("CAMERA 2 INITIALIZED")
	dual_mode = True 
except Exception:
	print("CRITICAL ERROR ON CAMERA TWO, FALLBACK.")
	dual_mode = False
			
cam1.configure(cam1.create_preview_configuration(main={"format": "RGB888", "size": (w1, h1)}))
cam1.start()

if dual_mode:
	cam2.configure(cam2.create_preview_configuration(main={"format": "RGB888", "size": (w1, h1)}))
	cam2.start()

time.sleep(1.0)
print("SYSTEM: ONLINE")

try: 
	while True:
		frame1 = cam1.capture_array()
		img1 = Image.fromarray(frame1)
		Disp1.image(img1)
		
		if dual_mode:
			frame2 = cam2.capture_array()
			img2 = Image.fromarray(frame2)
			Disp2.image(img2)
		else:
			Disp2.image(img1)

#cam1 = cv2.VideoCapture(0)
	
#cam2 = cv2.VideoCapture(1)
	
	
#if not cam2.isOpened():
#	print("Secondary camera not found, initializing fallback display")
#	cam2 = cam1
	
#if not cam1.isOpened():
#	print("CRITICAL PROGRAM ERRORS, SHUTTING DOWN")
#	sys.exit()
#print("LIVESTREAM: ONLINE")

#try: 
#	while True:
#	# display 1
#		ret1, frame1 = cam1.read()
#		#reading cam frames
#		if ret1:
#			#converts colors to rgb
#			frame1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB)
#			
#			frame1_resized = cv2.resize(frame1, (w1, h1))
#			#converts the size to fir properly
#			
#			#Data type converstion from numpy array to pillow image
#			img1 = Image.fromarray(frame1_resized)
#			
#			Disp1.image(img1)
#		ret2, frame2 = cam2.read()
#		if ret2:
#			frame2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2RGB)
#			frame2_resized = cv2.resize(frame2, (w2, h2))
#			img2 = Image.fromarray(frame2_resized)
#			Disp2.image(img2)


#this is so you can shut it down
except KeyboardInterrupt:
	print("HALTING CAMERA STREAMS")
	cam1.release()
	#this is because we made them overlay earilier
	if cam2 is not cam1:
		cam2.release()
	print("PROCCESES STOPED")
		
	
	
# Fallback programs to help error catching

#image1 = Image.new("RGB", (Disp1.width, Disp1.height))
#draw1 = ImageDraw.Draw(image1)
#draw1.rectangle((0, 0, Disp1.width, Disp1.height), fill=(255, 0, 0))
#font = ImageFont.load_default()
#draw1.text((30,40), "pi yadda yadda 1", font=font, fill=(255,225,225))


#image2 = Image.new("RGB", (Disp2.width, Disp2.height))
#draw2 = ImageDraw.Draw(image2)
#draw2.rectangle((0, 0, Disp2.width, Disp2.height), fill=(255, 0, 0))
#draw2.text((30,40), "pi yadda yadda 2", font=font, fill=(255,225,225))


#Disp1.image(image1)
#Disp2.image(image2)
#print("Working!")
