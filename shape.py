import cv2

lower_range=(0,34,10)
upper_range=(185,255,255)
frame=cv2.imread("du8vnh-278ec7e6-5df5-47f1-a25a-4be06da6e45b.jpg")
# frame = cv2.imread("download.jpg")
hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
mask=cv2.inRange(hsv,lower_range,upper_range)
erodedimg=cv2.erode(mask,None,iterations=2) #iterations is a keyword argument
dilatedimg=cv2.dilate(erodedimg,None,iterations=2)#imgtobedilate,defkenal,iteration or number of times the img process
contours,hierarchy = cv2.findContours(dilatedimg, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
print(len(contours))
arc_length=print(cv2.arcLength(contours[0],True))#list[]
cv2.drawContours(frame,contours,-1,(0,255,0),2)#where to draw contours,where is contours,apperence of contours
approx_contours = cv2.approxPolyDP(contours[0],arc_length,True)#contours,apsilon of contours,closed or open
cv2.drawContours(frame,[approx_contours],-1,(255,0,0),2)
print(len(approx_contours))
cv2.imshow("Shape Dectector",frame)
cv2.waitKey(10000)