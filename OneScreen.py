import time
from picamera2 import Picamera2, Preview
from libcamera import Transform


try:
    picam1 = Picamera2(0)
    picam1.start_preview(Preview.QTGL)
    picam1.start()
    
    picam2 = Picamera2(1)
    picam2.start_preview(Preview.QTGL)
    picam2.start()
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    picam1.close()
    picam2.close()
