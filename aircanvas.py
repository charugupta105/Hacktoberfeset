import cv2
import numpy as np

cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,150)

def getcontour(img,count):
    contours, hierarchy=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        # cv2.drawContours(imgsample,cnt,-1,(255,0,0),3)
        area = cv2.contourArea(cnt)
        if(area>250):
            peri=cv2.arcLength(cnt,True)
            approx=cv2.approxPolyDP(cnt,0.02*peri,True)
            x, y, z, w =cv2.boundingRect(approx)
            if(count==1):
                cv2.circle(imgsample,(x+ w//2, y),15,(255,0,0),cv2.FILLED)
            if(count==0):
                cv2.circle(imgsample, (x+ w//2, y), 15, (0, 255, 0), cv2.FILLED)
            if(count==2):
                cv2.circle(imgsample, (x+ w//2, y ), 15, (0, 0, 255), cv2.FILLED)



def drawtheline(mypoints,colorid):
    for points in mypoints:
        cv2.circle(imgsample,(point[0],point[1]),15,colorhai[colorid],cv2.FILLED)



while True:
    success,imgtop=cap.read()
    img=cv2.cvtColor(imgtop,cv2.COLOR_BGR2HSV)
    imggray = cv2.cvtColor(imgtop, cv2.COLOR_BGR2GRAY)
    imgblur = cv2.GaussianBlur(imggray, (7, 7), 1)
    imgcanny = cv2.Canny(imgblur, 50, 50)
    imgsample=imgtop.copy()
    cv2.imshow("live",imgtop)
    lower=np.array([[40,100,50],[110,50,50],[170, 120, 70]])
    upper=np.array([[80,255,255],[130,255,255],[180, 255, 255]])
    maskg=cv2.inRange(img,lower[0],upper[0])
    maskb=cv2.inRange(img,lower[1],upper[1])
    maskr=cv2.inRange(img,lower[2],upper[2])
    getcontour(maskr,2)
    getcontour(maskb,1)
    getcontour(maskg,0)
    # cv2.imshow("greenmask",maskg)
    # cv2.imshow("bluemask",maskb)
    # cv2.imshow("redmask",maskr)
    cv2.imshow("final",imgsample)
    cv2.waitKey(1)