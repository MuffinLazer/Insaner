import time
from picamera2 import Picamera2, Preview
from libcamera import Transform


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
        time.sleep(1)

except KeyboardInterrupt:
    picam1.close()
    picam2.close()
