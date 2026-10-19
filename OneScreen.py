import time
from picamera2 import Picamera2, Preview
from libcamera import Transform


try:
    picam1 = Picamera2(0)
    camera_config1 = picam1.create_preview_configuration()
    picam1.configure(camera_config1)
    picam1.start_preview(Preview.QTGL, x=0, y=0, width=400, height=400, transform=Transform(hflip=1))
    picam1.start()
    
    picam2 = Picamera2(1)
    camera_config2 = picam2.create_preview_configuration()
    picam2.configure(camera_config2)
    picam2.start_preview(Preview.QTGL, x=0, y=500, width=400, height=400, transform=Transform(hflip=1))
    picam2.start()

except KeyboardInterrupt:
    picam1.close()
    picam2.close()