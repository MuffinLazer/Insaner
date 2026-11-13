from time import sleep
from picamera2 import Picamera2, Preview

picam0 = Picamera2(0)
picam1 = Picamera2(1)

config0=picam0.create_preview_configuration(main={"size": (400,300)}) 
config1=picam1.create_preview_configuration(main={"size": (400,300)}) 

picam0.configure(config0)
picam1.configure(config1)

picam0.start_preview(Preview.QTGL)
picam1.start_preview(Preview.QTGL)

picam0.start()
picam1.start()

sleep(60)

picam0.stop
picam1.stop
