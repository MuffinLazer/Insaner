import sys
import time
from picamera2 import Picamera2, Preview
from libcamera import Transform
import cv2
import serial
import threading
sensortxt = ""
fpscounter = 0
fpsdisplay = 0
#libary slop 2 eletric boogaloo
def readserial(): # this is a better way to read serial as it runs a fuction that outputs a global string
    global sensortxt
    try:
        data = serial.Serial('/dev/ttyACM0', 9600, timeout=1.0)
        while True:
                if data.in_waiting > 0:
                    try:
                        line = data.readline().decode('utf-8').strip()
                        if line:
                            sensortxt = line
                            print("DATA CAPTURED:", sensortxt)
                    except Exception:
                        pass
                time.sleep(0.01)
    except Exception as error: # funny new way i learned how to do error catching as it will read the error and display it
         print(f"ERROR: {error}")
def fpstimer(): #im starting to love functions 
    global fpscounter, fpsdisplay #outputs these vars
    while True:
        time.sleep(1.0)  
        fpsdisplay = fpscounter # this makes them equal eachother because counter needs to be reset
        fpscounter = 0  #fpsdisplay is changing up and down a lot while fpscounter just runs every frame 

SerialThread = threading.Thread(target=readserial, daemon=True) #this calls the function from eariler (readserial), and runs it on another cpu thread in order to help the rest of the program run faster, daemon means it will shut itself off after main program is done
SerialThread.start() # this is kinda self explainitory
print("BACKGROUND THREAD ONLINE:")

FPSThread = threading.Thread(target=fpstimer, daemon=True)
FPSThread.start()
print("FPS COUNTER ONLINE:")

try:
    picam1 = Picamera2(0)
    config1 = picam1.create_preview_configuration(lores={"size": (512, 300)}, display="lores")
    picam1.configure(config1) 
    # kinda what we did last time, boots up the cameras and sets their sizes, this will likely change later once i have the actual screen 
    picam2 = Picamera2(1)
    config2 = picam2.create_preview_configuration(lores={"size": (512, 300)}, display="lores")
    picam2.configure(config2)

    picam1.start()
    picam2.start()
    time.sleep(2)
    print("CAMERAS INITIALIZED:")

    WindowName = "CAMS"
    cv2.namedWindow(WindowName, cv2.WINDOW_NORMAL) 
    cv2.setWindowProperty(WindowName, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    # this creates a window that goes by the name "CAMS" so that it takes up the full screen, the first line creates the window idifeir identifier while the next line forces it into fullscreen mode
    while True:
            frame1 = picam1.capture_array()
            frame2 = picam2.capture_array() #these just capture raw frames from the cams
            fpscounter+= 1

            if frame1 is not None and frame2 is not None:
                frame1RGB = cv2.cvtColor(frame1, cv2.COLOR_RGB2BGR)
                frame2RGB = cv2.cvtColor(frame2, cv2.COLOR_RGB2BGR) # this is becuse cv2 takes in BGR because it is OLDDDD

                framecombined = cv2.hconcat([frame1RGB, frame2RGB]) # combining the frames for one screen

                if sensortxt: #if we get data, it outputs it onto the onescreen using "putText"
                    cv2.putText(framecombined, f"SENSOR DATA: {sensortxt}", (10,30),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 120, 40), 2)
                    
                cv2.putText(framecombined, f"FPS: {fpsdisplay}", (1175 ,30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 120, 40), 2)
                
                cv2.imshow(WindowName, framecombined)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break #this reads for the letter q to kill the screens
            
except KeyboardInterrupt: #this is so it can be shut down from terminal as well
    print("SHUTTING DOWN")
picam1.close()
picam2.close()
sys.exit()
