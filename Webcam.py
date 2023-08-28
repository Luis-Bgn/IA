import cv2

capture = cv2.VideoCapture(0)

salida = cv2.VideoWriter('WebCam.avi', cv2.VideoWriter_fourcc(*'XVID'), 20, (640,480))

while (capture.isOpened()):
    ret, frame = capture.read()
    if(ret == True):
        cv2.imshow('Webcam',frame)
        salida.write(frame)
        if (cv2.waitKey(1) == ord('s')):
            break
    else:
        break
    
capture.release()
salida.release()
cv2.destroyAllWindows()

video = cv2.VideoCapture("Webcam.avi")

while (video.isOpened()):
    ret, frame2 = video.read()
    if(ret == True):
        cv2.imshow("videoWebcam",frame2)
        cv2.waitKey(30)
    else:
        break

video.release()
cv2.destroyAllWindows()