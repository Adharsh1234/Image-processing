import cv2
global x_value,y_value
x_value = []
y_value = []

def start_draw(frame,x,y):
    global x_value,y_value
    if x<100 and y<50:
        x_value=[]
        y_value=[]
    x_value.append(x)
    y_value.append(y)
    # print (x_value)
    # print (y_value)
    for i in range(len(x_value)):
        # frame[int(x_value[i]),int(y_value[i])]=(255,0,0)
        cv2.line(frame,(int(x_value[i]),int(y_value[i])),(int(x_value[i]),int(y_value[i]+3)),(255,0,0),9)