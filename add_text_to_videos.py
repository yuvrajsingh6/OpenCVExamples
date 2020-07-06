import cv2
import datetime
cap  =cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

while True:
    ret,frame = cap.read()
    if ret == True:
        font  = cv2.FONT_HERSHEY_SIMPLEX
        text  = 'width:' + str(cap.get(3))  + 'height:' + str(cap.get(4))
        datet = str(datetime.datetime.now())
        cv2.putText(frame,datet,(10,50),font,1,(0,255,255),2)

        cv2.imshow('frame',frame)

        if cv2.waitKey(5) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()

