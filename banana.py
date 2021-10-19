import cv2

lower_range=(0,2,0)
upper_range=(23,255,255)
frame = cv2.imread("download.jpg")
hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
mask=cv2.inRange(hsv,lower_range,upper_range)
erodedimg=cv2.erode(mask,None,iterations=2) #iterations is a keyword argument
dilatedimg=cv2.dilate(erodedimg,None,iterations=2)#imgtobedilate,defkenal,iteration or number of times the img process
contours,hierarchy = cv2.findContours(dilatedimg, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
print(len(contours))
cv2.drawContours(frame,contours,-1,(0,255,0),2)#where to draw contours,where is contours,apperence of contours
cv2.imshow("Apple Counter",frame)
end=cv2.waitKey(10000)