import cv2
camera =cv2.VideoCapture(0)
lower_range=(75,50,50)
upper_range=(166,255,255)

while True:
    sucess,frame = camera.read()
    frame=cv2.flip(frame,1)
    if sucess:
        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        mask=cv2.inRange(hsv,lower_range,upper_range)
        erodedimg=cv2.erode(mask,None,iterations=2) #iterations is a keyword argument 
        dilatedimg=cv2.dilate(erodedimg,None,iterations=2)#imgtobedilate,defkenal,iteration or number of times the img process
        contours,hierarchy = cv2.findContours(dilatedimg, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        print(len(contours))
        print(contours[0])
        c = sorted(contours, key=cv2.contourArea, reverse=True)[0]
        cv2.drawContours(frame,contours,0,(0,255,0),2)#where to draw contours,where is contours,apperence of contours
        cv2.imshow("Tracker",frame)
        end=cv2.waitKey(1)
        if end == ord("q"):
            cv2.destroyAllWindows()
            camera.release()
            break