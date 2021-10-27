import cv2
camera=cv2.VideoCapture(0)
success,frame1=camera.read()
success,frame2=camera.read()

while True:
    difference=cv2.absdiff(frame1,frame2)
    grey=cv2.cvtColor(difference,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Motion Detector",grey)
    frame2=frame1
    success,frame1=camera.read()
    end=cv2.waitKey(1)
    if end == ord("q"):
        cv2.destroyAllWindows()
        camera.release()
        break