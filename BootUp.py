import cv2
import sys

canvas = np.zeros((1024, 600, 3), dtype=np.uint8)

larp = "TEST"
org = (150, 200)  
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1.2
color = (255, 0, 0)
thickness = 2
line_type = cv2.LINE_AA



WindowName = "CAMS"
cv2.namedWindow(WindowName, cv2.WINDOW_NORMAL) 
cv2.moveWindow(WindowName, 0, 0)
cv2.setWindowProperty(WindowName, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)


cv2.putText(
    canvas, larp, org, font, font_scale, color, thickness, line_type
)

cv2.imshow(WindowName, canvas)