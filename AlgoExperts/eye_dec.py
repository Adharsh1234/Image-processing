import cv2
import winsound
camera=cv2.VideoCapture(0)
face_dectector= cv2.CascadeClassifier("Algoexperts\Face_dec.xml")#used for finding xml files
eye_dectector= cv2.CascadeClassifier("Algoexperts\Eye_dec.xml")

while True:
    success,frame=camera.read()
    frame=cv2.flip(frame,1)
    grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces= face_dectector.detectMultiScale(grey,minNeighbors=6)
    eyes = eye_dectector.detectMultiScale(grey,minNeighbors=23)
    for x,y,w,h in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        frame[y:y+h,x:x+w]
    if len(faces):
        for a,b,c,d in eyes:
            cv2.rectangle(frame,(a,b),(a+c,b+d),(0,255,0),2)

        if not len(eyes):
            frequency = 500
            duration = 100
            winsound.Beep(frequency,duration)
            cv2.putText(frame,"Get Up Lazy Driver !!!!",(10,70),cv2.FONT_HERSHEY_COMPLEX,1.5,(0,0,255),3)
        else:
            cv2.putText(frame,"Good",(10,70),cv2.FONT_HERSHEY_COMPLEX,3,(0,255,0),3)


    cv2.imshow("Face",frame)
    end=cv2.waitKey(1)
    if end == ord("q"):
        cv2.destroyAllWindows()
        camera.release()
        break


# hsv=cv2.cvtColor(frame[y:y+h,x:x+w], cv2.COLOR_BGR2HSV)
# blurred=cv2.blur(frame[y:y+h,x:x+w],(50,50))
# frame[y:y+h,x:x+w]=blurred