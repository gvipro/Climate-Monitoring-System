
import cv2 #Opencv to Format Data
from imutils.video.pivideostream import PiVideoStream #Video Object
import time #Time functions library 

class VideoCamera():
    def __init__(self):
        self.captureVideo = PiVideoStream().start()#Initialise Video Stream
        time.sleep(1)#Give camera time to load

    def update(self):#Function to return frames
        frame = self.captureVideo.read()#Store PiVideoStream  method to read frames 
        ret, jpeg = cv2.imencode('.jpg', frame)#Format data from video into streaming data
        return jpeg.tobytes()#Return data as bytes 
    
    #Function to stop
    def stopCamera(self):
        self.captureVideo.stop()