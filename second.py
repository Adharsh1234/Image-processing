import cv2
camera=cv2.VideoCapture(0)

while True:
    sucess,frame=camera.read()
    if sucess:
        grey=cv2.cvtColor(frame[300:400,300:400], cv2.COLOR_BGR2GRAY)
        hsv=cv2.cvtColor(frame[300:400,300:400], cv2.COLOR_BGR2HSV)
        print(hsv.shape)
        # head=frame[300:400,300:400] #= (255,0,0) # (bgr)
        # grey=cv2.cvtColor(frame[300:400,300:400], cv2.COLOR_BGR2GRAY)
        frame[300:400,300:400]=hsv
        cv2.imshow("Second Class",frame)
        end=cv2.waitKey(1)
        if end == ord("q"):
            cv2.destroyAllWindows()
            camera.release()
            break