import numpy as np
import cv2

cap = cv2.VideoCapture(0) # video capture source camera (Here webcam of laptop) 
ret,frame = cap.read() # return a single frame in variable `frame`

while(True):
    cv2.imshow('img1',frame) #display the captured image
    cv2.imwrite('/home/chinmay/tf_files/rand.jpg',frame)
#cv2.imwrite('/home/chinmay/tf_files/rand.jpg',frame)
    cv2.destroyAllWindows()
    break

cap.release()
execfile("Main.py")
