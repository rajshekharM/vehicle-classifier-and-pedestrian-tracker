import numpy as np
import cv2
#import time
import subprocess
subprocess.call(['./time.sh'])
cap = cv2.VideoCapture(0) # video capture source camera (Here webcam of laptop) 
ret,frame = cap.read() # return a single frame in variable `frame`

while(True):
    cv2.imshow('img1',frame) #display the captured image
    cv2.imwrite('/home/user_name/Automation_GitHub/tf_files/rand.jpg',frame) #ENTER YOUR USERNAME IN PLACE OF user_name
    cv2.destroyAllWindows()
    break

cap.release()
subprocess.call(['./main.sh'])
#cv2.waitKey(0)
subprocess.call(['./launch_docker.sh']) 
#cv2.waitKey(0)
#subprocess.call(['./classify.sh'])
