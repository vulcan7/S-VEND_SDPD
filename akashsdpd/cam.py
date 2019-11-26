import cv2
import time
cam = cv2.VideoCapture(0)
countdown=3
img_counter = 0
#cv2.namedWindow("test")
ret, frame = cam.read()
#cv2.imshow("test", frame)


while countdown >0:
                time.sleep(1)
                print(countdown)
                countdown -=1
                img_name = "z"+str(countdown)+".jpg"
                cv2.imwrite(img_name, frame)
                print("{} written!".format(img_name))

cam.release()

cv2.destroyAllWindows()
