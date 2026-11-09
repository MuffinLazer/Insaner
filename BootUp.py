import cv2

WindowName = "CAMS"
cv2.namedWindow(WindowName, cv2.WINDOW_NORMAL) 
cv2.moveWindow(WindowName, 0, 0)
cv2.setWindowProperty(WindowName, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

BootUpWindow = cv2.putText("TEST", (30, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

cv2.imshow(WindowName, BootUpWindow)