import cv2
camera=cv2.VideoCapture(0)

while True:
    sucess,frame=camera.read()
    if sucess:
        frame=cv2.flip(frame,1)
        # print(frame.shape)
        # frame[250:400,250:400]=(0,255,0)
        # headpost=frame[250:400,250:400]
        # frame[100:250,100:250]=(0,0,255)
        # wallpost=frame[100:250,100:250]
        # headpost=wallpost
        # frame[250:400,250:400]=frame[100:250,100:250]
        cv2.imshow("Test",frame)
        end=cv2.waitKey(1)
        if end == ord("q"):
            camera.release()
            cv2.destroyAllWindows()
            break