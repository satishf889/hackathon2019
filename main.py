import cv2
from flask import Flask, render_template, Response
from camera import VideoCamera
from PIL import Image
import io
import uuid
import time
import os
st1=1
starttime=time.localtime()
app = Flask(__name__)

@app.route('/start')
def index():
    return render_template('index.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        image = Image.open(io.BytesIO(frame))
        if(time.localtime().tm_sec-starttime.tm_sec%5==0):
        	name=str(uuid.uuid4())
        	image.save("croppedimages/"+name+".jpg")

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def stop_feed():
	return "Thank You"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)