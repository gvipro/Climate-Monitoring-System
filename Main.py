from flask               import Flask #Create web server
from flask               import Response #Create generator function to generates frames
from flask               import request #
from flask               import render_template #Render home paga
from sense_hat           import SenseHat    #SenseHat
from Video               import VideoCamera #Video Object
from flask_basicauth     import BasicAuth


#Create App object from Flask
app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = 'Admin'   #Username to access web page
app.config['BASIC_AUTH_PASSWORD'] = '12345678'#Password to access web page
app.config['BASIC_AUTH_FORCE'] = True #Require authentication
basic_auth = BasicAuth(app) #Intialising BasicAuth

videoStream = VideoCamera() # Create VideoStream object from Video


#Set the home page route
@app.route('/')
#Requre authentication 
@basic_auth.required
#Define index
def index():
    #Render index.html when user request web page
    return render_template('index.html') #you can customze index.html here

#Video generator
def gen(Video):
    while True:
        #Call the update() method from VideoCamera to grab frame
        frame = Video.update()
        #Create videostream from received frames
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

#Set the video feed url
@app.route('/video_feed')
#Define video feed
def video_feed():
    #When user access the web page, send response
    return Response(gen(videoStream),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


#Start applicaiton
if __name__ == '__main__':

    app.run(host='0.0.0.0', debug=False)