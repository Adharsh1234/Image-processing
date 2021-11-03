import cv2
img= cv2.imread("AlgoExperts\images.jpg")
plate_dectector= cv2.CascadeClassifier("AlgoExperts/number_dec.xml")#used for finding xml files


while True:
    # success,frame=img.read()
    grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    plate= plate_dectector.detectMultiScale(grey,minNeighbors=30)
    for x,y,w,h in plate:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        img[y:y+h,x:x+w]
        cv2.imwrite("Edited Image holder\Edited img.jpeg",img[y:y+h,x:x+w])

    cv2.imshow("Number Plate Dectector",img[y:y+h,x:x+w])
    end=cv2.waitKey(0)
    if end == ord("q"):
        cv2.destroyAllWindows()
        break