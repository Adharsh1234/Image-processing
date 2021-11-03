import cv2
# img= cv2.imread("AlgoExperts\images.jpg")
video = cv2.VideoCapture("videoplayback.mp4")
plate_dectector= cv2.CascadeClassifier("AlgoExperts/number_dec.xml")#used for finding xml files
count=0

while True:
    success,frame=video.read()
    # print(success)
    if success:
        grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        plate= plate_dectector.detectMultiScale(grey,minNeighbors=12)
        for x,y,w,h in plate:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            frame[y:y+h,x:x+w]
            count=count+1
            cv2.imwrite("Edited Image holder\Edited video"+str(count)+".jpeg",frame)

            cv2.imshow("Number Plate Dectector",frame)
        end=cv2.waitKey(1)
        if end == ord("q"):
            cv2.destroyAllWindows()
            video.release()
            break