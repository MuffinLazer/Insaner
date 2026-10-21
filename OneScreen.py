import sys
import time
from picamera2 import Picamera2, Preview
from libcamera import Transform
import cv2
import serial

data = serial.Serial('/dev/ttyACM0', 9600, timeout=0.01)

try:
    picam1 = Picamera2(0)
    config1 = picam1.create_preview_configuration(lores={"size": (320, 240)}, display="lores")
    picam1.configure(config1)
  
    picam2 = Picamera2(1)
    config2 = picam2.create_preview_configuration(lores={"size": (320, 240)}, display="lores")
    picam2.configure(config2)

    time.sleep(2)

    picam1.start()
    picam2.start()

    WindowName = "CAMS"
    cv2.namedWindow(WindowName, cv2.WINDOW_NORMAL)
    cv2.setWindowProperty(WindowName, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

sensortxt = ""

    while True:
        if data.in_waiting > 0:
            try:
                line = data.readline().decode('utf-8').strip()
                if line:
                    sensortxt = line
                    print("DATA CAPTURED:", sensortxt)
            except Exception:
                pass

        frame1 = picam1.capture_array()
        frame2 = picam2.capture_array()

        frame1RGB = cv2.cvtColor(frame1, cv2.COLOR_RGB2BGR)
        frame2RGB = cv2.cvtColor(frame2, cv2.COLOR_RGB2BGR)

        if sensortxt:
            cv2.putText(framecombined, f"SENSOR DATA: {sensortxt}", (10,30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        framecombined = cv2.hconcat([frame1RGB, frame2RGB])

        if frame1 & frame2 is not None: 
            cv2.imshow(WindowName, framecombined)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    picam1.close()
    picam2.close()
    sys.exit()