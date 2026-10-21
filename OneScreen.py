import sys
import time
from picamera2 import Picamera2, Preview
from libcamera import Transform
import cv2


try:
    picam1 = Picamera2(0)
    config1 = picam1.create_preview_configuration(lores={"size": (320, 240)}, display="lores")
    picam1.configure(config1)
    picam1.start()
    
    picam2 = Picamera2(1)
    config2 = picam2.create_preview_configuration(lores={"size": (320, 240)}, display="lores")
    picam2.configure(config2)
    picam2.start()
    while True:
        frame1 = picam1.capture_array()
        frame2 = picam2.capture_array()

        r, g, b, = frame1.split()
        frame1 = Image.merge("RGB", (b, g, r))

        r, g, b, = frame2.split()
        frame2 = Image.merge("RGB", (b, g, r))

        framecombined = cv2.hconcat([frame1, frame2])

        if frame1 & frame2 is not None: 
            cv2.imshow('CamCombined', framecombined)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    picam1.close()
    picam2.close()
    sys.exit()