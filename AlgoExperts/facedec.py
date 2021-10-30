import cv2
camera=cv2.VideoCapture(0)
face_dectector= cv2.CascadeClassifier("Algoexperts\Face_dec.xml")#used for finding xml files


while True:
    success,frame=camera.read()
    frame=cv2.flip(frame,1)
    grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces= face_dectector.detectMultiScale(grey,minNeighbors=6)
    for x,y,w,h in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        frame[y:y+h,x:x+w]
        hsv=cv2.cvtColor(frame[y:y+h,x:x+w], cv2.COLOR_BGR2HSV)
        blurred=cv2.blur(frame[y:y+h,x:x+w],(50,50))
        frame[y:y+h,x:x+w]=blurred

    cv2.imshow("Face",frame)
    end=cv2.waitKey(1)
    if end == ord("q"):
        cv2.destroyAllWindows()
        camera.release()
        break