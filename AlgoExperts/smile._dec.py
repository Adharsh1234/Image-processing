import cv2
camera = cv2.VideoCapture(0)
smile_dectector = cv2.CascadeClassifier(
    "Algoexperts\Smile.xml")  # used for finding xml files
count = 0

while True:
    success, frame = camera.read()
    frame = cv2.flip(frame, 1)
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    smiles = smile_dectector.detectMultiScale(grey, minNeighbors=400)
    for x, y, w, h in smiles:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        frame[y:y+h, x:x+w]
    if len(smiles):
        count = count+1
        cv2.imwrite("Edited Image holder\smile"+str(count)+".jpg", frame)

    cv2.imshow("Smile Dectector", frame)
    end = cv2.waitKey(1)
    if end == ord("q"):
        cv2.destroyAllWindows()
        camera.release()
        break
# hsv=cv2.cvtColor(frame[y:y+h,x:x+w], cv2.COLOR_BGR2HSV)
# ablurred=cv2.blur(frame[y:y+h,x:x+w],(50,50))
# frame[y:y+h,x:x+w]=blurred
