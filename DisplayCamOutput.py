# BEFORE YOU CAN RUN ANY OF THIS ON A RASPBERRY PI, YOU MUST BE ON A PYTHON VM, YOU CAN DO THIS VIA TYPING IN TERMINAL "~/env/bin/activate"

import sys
import cv2
import digitalio
import time
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
from picamera2 import Picamera2
import serial
#All the libarys i need


#preps the board and pins to get ready to communicate, kinda important 
spi = board.SPI()


#cs pins is the actual display pin to tell it to show different colors 
#D22 pin is 17
cs_pin1 = digitalio.DigitalInOut(board.D22)
cs_pin1.direction = digitalio.Direction.OUTPUT

#D23 pin is 16
cs_pin2 = digitalio.DigitalInOut(board.D23)
cs_pin2.direction = digitalio.Direction.OUTPUT

#D25 is pin 22
dc_pin = digitalio.DigitalInOut(board.D25)
dc_pin.direction = digitalio.Direction.OUTPUT


#D24 pin is 18 
reset_pin = digitalio.DigitalInOut(board.D24)
reset_pin.direction = digitalio.Direction.OUTPUT

sir = serial.Serial('/dev/ttyACM0', 9600, timeout=0.01)
#sir is what we capture from the arduino, /dev/ttyACM0is the port that the arduino speaks through

title = "INSANER: INITLIZING"
#this is for the first boot up before cams boot up


Disp1 = st7789.ST7789(
	spi,
	cs=cs_pin1,
	dc=dc_pin,
	rst=reset_pin,
	baudrate=80000000,
	width=240,
	height=320,
	x_offset=0,
	y_offset=0,
)
#These are for the displays and designates them pins, and other broader strokes like baudrate (datatransfer speed)
Disp2 = st7789.ST7789(
	spi,
	cs=cs_pin2,
	dc=dc_pin,
	rst=reset_pin,
	baudrate=80000000,
	width=240,
	height=320,
	x_offset=0,
	y_offset=0,
)

#making more varriables for later 
w1, h1,= Disp1.width, Disp1.height
w2, h2 = Disp2.width, Disp2.height

font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
font = ImageFont.truetype(font_path, 20)

img = Image.new("RGB", (w1,h1), color="black")
draw = ImageDraw.Draw(img)
draw.rectangle([0,0, w1,w2], fill=(0,0,0))
draw.text((0, 130), f"{title}", font=font, fill=(20,150,250))

Disp1.image(img) 
Disp2.image(img) 


# W Larp
print("INITIALZING CAMS")

#this set of statements is for incase one of the cameras dont work it will duplicate the displays and mirror eachother
try: 
	cam1 = Picamera2(0)
	print("CAMERA 1 INITIALIZED")
except Exception:
	print("CRITICAL ERROR ON CAMERA ONE, FALLBACK.")
	sys.exit
#Dual mode is a boolian we keep track of in order to tell if both cams work or not
try: 
	cam2 = Picamera2(1)
	print("CAMERA 2 INITIALIZED")
	dual_mode = True 
except Exception:
	print("CRITICAL ERROR ON CAMERA TWO, FALLBACK.")
	dual_mode = False
			

#since we are using raw ribbin cables, formatting is needed to convert the color and sizing
cam1.configure(cam1.create_preview_configuration(main={"format": "RGB888", "size": (w1, h1)}))
cam1.start()
#dual mode from eariler, just sets up both cams
if dual_mode:
	cam2.configure(cam2.create_preview_configuration(main={"format": "RGB888", "size": (w1, h1)}))
	cam2.start()

#sleeping system so cameras can warm up because amazon said they should :P
time.sleep(2.0)
print("SYSTEM: ONLINE")

sensortxt = "DATA NOT FOUND"
font = ImageFont.load_default() #loading new font


#This makes a combined image with overlay brush were everything below overlay brush will apply to overlay
Overlay = Image.new("RGBA", (w1, h1), (0,0,0,0))
OverlayBrush = ImageDraw.Draw(Overlay) 

OverlayBrush.rectangle([5, 10, 230, 35], fill=(0,0,0,150))


try: 
	while True: # This while setup checks for new data
		if sir.in_waiting > 0:
			try: 
				line = sir.readline().decode('utf-8').strip()
				if line:
					sensortxt = line
					print("DATA CAPTURED: ", sensortxt)
			except Exception:
				pass
				
		#captures one frame at a time and displays it to the lcd screens, this is the best method i could come up with at the time with these kinda cams and displays		
		frame1 = cam1.capture_array()
		img1 = Image.fromarray(frame1)
		
		
		#some code is needed to fix the hardware, the display was reading as BRG instead of RGB
		#What this code does is split the BGR snd aligns it back to RGB
		r, g, b, = img1.split()
		#this merges them back together
		img1 = Image.merge("RGB", (b, g, r))
		
			
		#this is an overlay over the camera image stream to allow arduino data to be put in
		img1 = img1.convert("RGBA")
		img1 = Image.alpha_composite(img1, Overlay)
		
		
		#This places text from serial/arduino where the overlay is
		draw1 = ImageDraw.Draw(img1)
		draw1.text((20, 15), f"DATA: {sensortxt}", font=font, fill=(20,150,250))
	
	
		Disp1.image(img1) #displays final image to the screen 
		#dual mode again as the fallback stuff
		if dual_mode:		
			frame2 = cam2.capture_array()
			img2 = Image.fromarray(frame2)
	
			
			#this is incase the display swaps for some reason
			# img2 = img2.transpose(Image.ROTATE_180)
	
			
			r, g, b, = img2.split()
			img2 = Image.merge("RGB", (b, g, r))
			
			
			img2 = img2.convert("RGBA")
			img2 = Image.alpha_composite(img2, Overlay)
			
			
			draw2 = ImageDraw.Draw(img2)
			draw2.text((20, 15), f"DATA: {sensortxt}", font=font, fill=(20,150,250))
	
	
			Disp2.image(img2)
		else:
			Disp2.image(img1)

#this is so you can shut it down
except KeyboardInterrupt:
	print("HALTING CAMERA STREAMS")
	cam1.stop()
	#this is because we made them overlay earilier
	if cam2 is not cam1:
		cam2.stop()
	print("PROCESS HALTED")
		# W larps
