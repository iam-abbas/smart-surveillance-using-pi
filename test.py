import cv2

cap= cv2.VideoCapture(0)

while True:
        ret, image = cap.read()
        if cv2.waitKey(50) & 0xFF == ord('q'):
                break
        if ret == False:
                break
        cv2.imshow('image', image)
