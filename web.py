from flask import Flask, request, render_template, Response
import cv2
import numpy as np


app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
video = cv2.VideoCapture(0)
video.set(16, 854)
video.set(9, 480)

@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')

@app.route('/cameras')
def camera():
    """Video streaming home page."""
    return render_template('cameras.html')

@app.route('/alerts')
def alerts():
    """Video streaming home page."""
    return render_template('alerts.html')

@app.route('/settings')
def settings():
    """Video streaming home page."""
    return render_template('settings.html')


def gen():
    """Video streaming generator function."""
    while True:
        rval, frame = video.read()
        cv2.imwrite('t.jpg', frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + open('t.jpg', 'rb').read() + b'\r\n')


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(),mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005, threaded=True, debug=True)