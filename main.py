import cv2
import numpy as np
import adv
import telepot
from telepot.loop import MessageLoop
import time
import os

bot = telepot.Bot("987039509:AAHX_HjTmoaqG_9ZUiGMBKzuBrq7-d9_Xcg")
MessageLoop(bot, adv.handle).run_as_thread()
# Pretrained classes in the model
classNames = {0: 'background',
              1: 'person'}


def id_class_name(class_id, classes):
    for key, value in classes.items():
        if class_id == key:
            return value

def adjust_gamma(image, gamma=1.0):

    invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** invGamma) * 255
        for i in np.arange(0, 256)]).astype("uint8")
    return cv2.LUT(image, table)

cap= cv2.VideoCapture(0)

# Loading model
model = cv2.dnn.readNetFromTensorflow('models/frozen_inference_graph.pb',
                                      'models/ssd_mobilenet_v2_coco_2018_03_29.pbtxt')

send_status = 1
i = 0

br = 0
while True:
        
        ret, image = cap.read()
        if cv2.waitKey(50) & 0xFF == ord('q'):
                break
        if ret == False:
                break
        
        if br == 1:
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
                                        cv2.imwrite("img/cap_"+str(int(i/50))+".jpg", image)
                                        bot.sendPhoto(824389035, photo=open("img/cap_"+str(int(i/50))+".jpg", 'rb'), caption="<b>[Motion Detected]</b> \n<pre>I think there is someone in your house</pre>. \n\nDo you want to take any action? \nClick /yes to call police \nClick /no to ignore", parse_mode='HTML')
                                        send_status = 0
                                        cv2.imwrite("static/images/1.jpg", image)
                                        br = 1
        #cv2.imshow('image', image)


cap.release()
cv2.destroyAllWindows()
#time.sleep(10)
os.system('python web.py')
