# Vehicle-classifier-and-pedestrian-tracker
Vehicle classifier using own dataset to train Inception on python-tensorflow platform and using YOLO to identify pedestrians 
# Autonomous-Security-and-Suveillance-System-using-Image-Processing-and-Deep-Learning.
Special thanks to Chaya N Aishwayra and team for making it possible
The system manages to capture an image of a vehicle, identify the type of the vehicle and also the number plate and hence stores the results in a database. This database can hence store details of all blacklisted vehicles. Deep Learning was adopted to identify the type of vehicle by creating a database of images of cars on Indian roads. Image processing was applied to identify the number plate and hence export the result into the database.
The steps involved are summarized in the flowchart below:
Capture photo of car-> Record time of capture-> Run classifier to record car type and record result -> Identify number plate and store registration number

Pre-requisites:
A) OpenCV 2
B) Python 2.7
C) Numpy
D) Tensorflow (via Docker)
I recommend Anaconda in order to install A,B and C.

The instructions in the following link can be followed for installing Tensorflow:
https://codelabs.developers.google.com/codelabs/tensorflow-for-poets/index.html?index=..%2F..%2Findex#1

Run surveillance.py

The system uses a webcam to capture a real-time image of a vehicle. The webcame maybe in-built VideoCapture(0) or external(mostly VideoCapture(1) depending on the port it is connected to.) Upon capturing the image, it takes about 15 seconds to display and store the car type, time of capture and license plate number. The results are stored in a text file named Output.txt

