import time
from picamera2 import Picamera2, Preview
from libcamera import Transform



picam1 = Picamera2(0)
camera_config1 = picam1.create_preview_configuration()
picam1.configure(camera_config1)
picam1.start_preview(Preview.QTGL, x=0, y=0, width=800, height=600, transform=Transform(hflip=1))
picam1.start()

picam2 = Picamera2(1)
camera_config2 = picam2.create_preview_configuration()
picam2.configure(camera_config2)
picam2.start_preview(Preview.QTGL, x=100, y=200, width=800, height=600, transform=Transform(hflip=1))
picam2.start()

time.sleep(2)

picam1.capture_file("Test1.jpg")
picam2.capture_file("Test2.jpg")

picam1.stop()
picam2.stop()