from picamera2 import Picamera2, Preview
import time



picam1 = Picamera2(0)
camera_config1 = picam1.create_preview_configuration()
picam1.configure(camera_config1)
picam1.start_preview(Preview.QTGL)
picam1.start()

picam2 = Picamera2(1)
camera_config2 = picam2.create_preview_configuration()
picam2.configure(camera_config2)
picam2.start_preview(Preview.QTGL)
picam2.start()

time.sleep(2)

picam1.capture_file("Test1.jpg")
picam2.capture_file("Test2.jpg")