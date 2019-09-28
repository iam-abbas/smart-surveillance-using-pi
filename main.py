import cv2
import numpy as np
import telepot
from telepot.loop import MessageLoop
import time
import random 
import keyboard  # using module keyboard
from flask import Flask, request, render_template, Response
import os
import sys




bot = telepot.Bot("987039509:AAHX_HjTmoaqG_9ZUiGMBKzuBrq7-d9_Xcg")




# Pretrained classes in the model
classNames = {0: 'background',
              1: 'person'}


def id_class_name(class_id, classes):
    for key, value in classes.items():
        if class_id == key:
            return value

def adjust_gamma(image, gamma=1.0):
    # build a lookup table mapping the pixel values [0, 255] to
    # their adjusted gamma values
    invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** invGamma) * 255
        for i in np.arange(0, 256)]).astype("uint8")
 
    # apply gamma correction using the lookup table
    return cv2.LUT(image, table)

cap= cv2.VideoCapture(0)

# Loading model
model = cv2.dnn.readNetFromTensorflow('models/frozen_inference_graph.pb',
                                      'models/ssd_mobilenet_v2_coco_2018_03_29.pbtxt')

send_status = 1
i = 0
br = 0
foo = 1

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    #should work thanks to Winston
    if msg['from']['id'] != 824389035:
        bot.sendMessage(chat_id, "Sorry this is a personal bot. Access Denied!")
        exit(1)
    print(command)
    if command == '/yes':
        bot.sendMessage(chat_id, "Calling Police")
    if command == '/no':
        bot.sendMessage(chat_id, "Ok ignoring now, send /cancel to stop monitoring")
    if command == '/cancel':
        bot.sendMessage(chat_id, "Aborted Monitoring. Click /start to start again")
    if command == '/start':
        bot.sendMessage(chat_id, "Started Monitoring")
        global foo
        foo = 0

MessageLoop(bot, handle).run_as_thread()

while True:
        if(br == 1 and foo == 1):
                break
        ret, image = cap.read()
        if cv2.waitKey(50) & 0xFF == ord('q'):
                break
        if ret == False:
                break

        image_height, image_width, _ = image.shape

        model.setInput(cv2.dnn.blobFromImage(image, size=(200, 200), swapRB=True))
        output = model.forward()


        for detection in output[0, 0, :, :]:
                confidence = detection[2]
                if confidence > 0.5:
                        class_id = detection[1]
                        if class_id == 1.0:
                                class_name=id_class_name(class_id,classNames)
                                box_x = detection[3] * image_width
                                box_y = detection[4] * image_height
                                box_width = detection[5] * image_width
                                box_height = detection[6] * image_height
                                cv2.rectangle(image, (int(box_x), int(box_y)), (int(box_width), int(box_height)), (23, 230, 210), thickness=1)
                                i += 1
                                if(send_status == 1):
                                        name = "img/cap_"+str(random.randint(1, 9999))+".jpg"
                                        cv2.imwrite(name, image)
                                        cv2.imwrite("static/images/1.jpg", image)
                                        bot.sendPhoto(824389035, photo=open(name, 'rb'), caption="<b>[Motion Detected]</b> \n<pre>I think there is someone in your house</pre>. \n\nDo you want to take any action? \nClick /yes to call police \nClick /no to ignore", parse_mode='HTML')
                                        send_status = 0
                                        br = 1
                                if keyboard.is_pressed('a'):
                                        cv2.imwrite("webimg/cap_"+str(random.randint(1, 9999))+".jpg", image)

        # cv2.imshow('image', image)

cap.release()
cv2.waitKey(0)
cv2.destroyAllWindows()

app = Flask(__name__)
video = cv2.VideoCapture(0)
video.set(16, 854)
video.set(9, 480)

rand = str(random.randint(0, 999))

@app.route('/')


def index():
   return render_template('index.html', value=rand)

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

