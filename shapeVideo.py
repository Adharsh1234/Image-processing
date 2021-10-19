import cv2
camera=cv2.VideoCapture(0)
lower_range=(75,50,50)
upper_range=(166,255,255)

while True:
    success,frame=camera.read()
    if success:
        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        mask=cv2.inRange(hsv,lower_range,upper_range)
        erodedimg=cv2.erode(mask,None,iterations=2) #iterations is a keyword argument
        dilatedimg=cv2.dilate(erodedimg,None,iterations=2)#imgtobedilate,defkenal,iteration or number of times the img process
        contours,hierarchy = cv2.findContours(dilatedimg, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        # print(len(contours))
        arc_length=cv2.arcLength(contours[0],True)#list[]
        cv2.drawContours(frame,contours,0,(0,255,0),2)#where to draw contours,where is contours,apperence of contours
        approx_contours = cv2.approxPolyDP(contours[0],arc_length*0.09,True)#contours,apsilon of contours,closed or open
        cv2.drawContours(frame,[approx_contours],0,(255,0,0),2)
        print(len(approx_contours))
        if len(approx_contours) == 4:
            print("It is a Square!!")
        else:
            print("It is not a Square!")
        cv2.imshow("Shape Dectector With Video",frame)
        end= cv2.waitKey(1)
        if end == ord("q"):
            cv2.destroyAllWindows()
            camera.release()
            break