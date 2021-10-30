import cv2
import actual_drawing
camera =cv2.VideoCapture(0)
lower_range=(75,50,50)
upper_range=(166,255,255)

while True:
    sucess,frame = camera.read()
    frame=cv2.flip(frame,1)
    if sucess:
        cv2.rectangle(frame,(0,0),(100,50),(0,255,0),-1)
        cv2.putText(frame,"CLEAR",(0,27),cv2.FONT_HERSHEY_DUPLEX,1,(255,0,255),2)
        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        mask=cv2.inRange(hsv,lower_range,upper_range)
        erodedimg=cv2.erode(mask,None,iterations=2)
        dilatedimg=cv2.dilate(erodedimg,None,iterations=2)
        contours,hierarchy = cv2.findContours(dilatedimg, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        # print(len(contours))
        # print(contours[0]
        if len(contours):
            c = sorted(contours, key=cv2.contourArea, reverse=True)[0]#area , sorted(descenting),find 1
            ((x, y), radius) = cv2.minEnclosingCircle(c)#circle radius got imagine 
            print(radius)
            # cv2.drawContours(frame, [c], -1, (0, 255, 0), 2)
            cv2.circle(frame, (int(x),int(y)), int(radius),(0,0,255), 2)#circle drawn with here
            cv2.circle(frame, (int(x),int(y)), int(2),(0,0,255), 2)#center point of the circle
            print(x,y)
            actual_drawing.start_draw(frame,x,y)
        cv2.imshow("Tracker",frame)
        end=cv2.waitKey(1)
        if end == ord("q"):
            cv2.destroyAllWindows()
            camera.release()
            break