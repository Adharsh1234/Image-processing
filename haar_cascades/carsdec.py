import cv2
img=cv2.imread("gettyimages-931423150-170667a.jpg")
# print(img)

car_dectector= cv2.CascadeClassifier("cars.xml")#used for finding xml files
grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cars= car_dectector.detectMultiScale(grey,minNeighbors=7)
for x,y,w,h in cars:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),1)

img = cv2.resize(img, (960, 540))
cv2.namedWindow("output", cv2.WINDOW_NORMAL)
cv2.imshow("output",img)
end=cv2.waitKey(100000)
# print (len(cars))