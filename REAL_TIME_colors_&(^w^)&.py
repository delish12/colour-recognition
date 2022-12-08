import cv2
import numpy as np


cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)

while True:
    _,frame = cap.read()
    
    hsv_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    height,width,_ = frame.shape

    cx = int(width/2)
    cy = int(height/2)
    pixel_center = hsv_frame[cy,cx]
    hue_value = pixel_center[0]
    value_value = pixel_center[2]

    color = 'Undefined'
    if value_value > 170:
        color = 'WHITE'
    elif value_value < 60:
        color = 'BLACK'
    elif hue_value < 5:
        color = 'RED'
    elif hue_value < 22:
        color = 'ORANGE'
    elif hue_value < 33:
        color = 'YELLOW'
    elif hue_value < 78:
        color = 'GREEN'
    elif hue_value < 131:
        color = 'BLUE'
    elif hue_value < 170:
        color = 'VIOLET'
    else:
        color = 'some shit color'
        
    print(pixel_center)

    frame = cv2.flip(frame,1)

    cv2.rectangle(frame, pt1=(0,615), pt2=(1280,665), color=(255,255,255), thickness= -1)

    cv2.putText(frame,color,(cx-30,int(cy*1.8)),0,1,(0,0,0),2)

    cv2.circle(frame,(cx,cy),5,(255,0,0),3)
    
    cv2.imshow("Frame",frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
    
