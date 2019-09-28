from flask import Flask, request, render_template, Response
import cv2
import numpy as np


from main import *


def adjust_gamma(image, gamma=1.0):
    # build a lookup table mapping the pixel values [0, 255] to
    # their adjusted gamma values
    invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** invGamma) * 255
        for i in np.arange(0, 256)]).astype("uint8")
 
    # apply gamma correction using the lookup table
    return cv2.LUT(image, table)



app = Flask(__name__)
video = cap
video.set(16, 854)
video.set(9, 480)


@app.route('/')
def index():
   return render_template('index.html')

def gen():
    """Video streaming generator function."""
    while True:
        rval, frame = video.read()
        cv2.imwrite('t.jpg', adjust_gamma(frame, 1.5))
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + open('t.jpg', 'rb').read() + b'\r\n')


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(),mimetype='multipart/x-mixed-replace; boundary=frame')



if __name__ == '__main__':
   app.run(debug = True, host = '0.0.0.0',port=5005)
