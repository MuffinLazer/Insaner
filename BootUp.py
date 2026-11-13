import cv2

Canvas = cv2.imread("canvas.png")
Canvas = cv2.putText(Canvas, "TEST", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255))
# the 20, 230 thing means it is placed at coords 20, 30, it is using hershy simplex font, 0, 0, 255 means rgb, so blue, 1.2 means refrences the smoothness of the font