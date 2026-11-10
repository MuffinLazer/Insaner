import cv2
<<<<<<< HEAD
=======
import sys

canvas = np.zeros((1024, 600, 3), dtype=np.uint8)

larp = "TEST"
org = (150, 200)  
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1.2
color = (255, 0, 0)
thickness = 2
line_type = cv2.LINE_AA


>>>>>>> 451642a971557851adc0912e76a23da94bfe26f0

WindowName = "CAMS"
cv2.namedWindow(WindowName, cv2.WINDOW_NORMAL) 
cv2.moveWindow(WindowName, 0, 0)
cv2.setWindowProperty(WindowName, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

<<<<<<< HEAD
BootUpWindow = cv2.putText("TEST", (30, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

cv2.imshow(WindowName, BootUpWindow)
=======

cv2.putText(
    canvas, larp, org, font, font_scale, color, thickness, line_type
)

cv2.imshow(WindowName, canvas)
>>>>>>> 451642a971557851adc0912e76a23da94bfe26f0
