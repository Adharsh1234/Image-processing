import cv2
import numpy # numerical python
def nothing(x):
    pass
cv2.namedWindow("HSV Converter")
cv2.createTrackbar("l_h","HSV Converter",0,180,nothing)
cv2.createTrackbar("l_s","HSV Converter",0,255,nothing)
cv2.createTrackbar("l_v","HSV Converter",0,255,nothing)
cv2.createTrackbar("u_h","HSV Converter",0,180,nothing)
cv2.createTrackbar("u_s","HSV Converter",0,255,nothing)
cv2.createTrackbar("u_v","HSV Converter",0,255,nothing)
camera=cv2.VideoCapture(0)


while True:
    # success,frame=camera.read()
    # frame=cv2.flip(frame,1)
    success = True
    frame = cv2.imread("du8vnh-278ec7e6-5df5-47f1-a25a-4be06da6e45b.jpg")
    if success:
        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        l_h=cv2.getTrackbarPos("l_h", "HSV Converter")
        l_s=cv2.getTrackbarPos("l_s", "HSV Converter")
        l_v=cv2.getTrackbarPos("l_v", "HSV Converter")
        u_h=cv2.getTrackbarPos("u_h", "HSV Converter")
        u_s=cv2.getTrackbarPos("u_s", "HSV Converter")
        u_v=cv2.getTrackbarPos("u_v", "HSV Converter")
        lowerhsv= (l_h,l_s,l_v)
        upperhsv= (u_h,u_s,u_v)
        maskedimg=cv2.inRange(hsv,lowerhsv,upperhsv)
        erodedimg= cv2.erode(maskedimg,None,iterations=2)
        dilatedimg= cv2.dilate(erodedimg,None,iterations=2)
        lastimg=cv2.bitwise_and(frame,frame,mask=dilatedimg)
        cv2.resizeWindow("HSV Converter", 1350,750)
        # cv2.imshow("HSV Window",lastimg)
        cv2.imshow("HSV Converter",lastimg)
        end = cv2.waitKey(1)
        if end == ord("q"):
            cv2.destroyAllWindows()
            camera.release()
            break