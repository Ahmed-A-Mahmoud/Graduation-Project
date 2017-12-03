import cv2
import numpy as np  # importing libraries

img = cv2.imread("w.jpg")
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Over the Clouds - gray", gray_image)
eq=cv2.equalizeHist(gray_image)
cv2.imshow("equalize", eq)


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
faces = face_cascade.detectMultiScale(eq, 1.3, 5)
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,0),1)
   # roi_gray = eq[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]

cv2.imshow('img rec',img);
hsvImage=cv2.cvtColor(roi_color,cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsvImage)
meanarrH=np.mean(h, axis=(0, 1))
meanarrS=np.mean(s, axis=(0, 1))
meanarrV=np.mean(v, axis=(0, 1))

minH=meanarrH-55;
maxH=meanarrH+55;
minS=meanarrS-55;
maxS=meanarrS+55;
minV=meanarrV-55;
maxV=meanarrV+55;
hsvImage = cv2.merge([h, s, v])
lower_range = np.array([minH,minS,minV])
upper_range = np.array([maxH,maxS,maxV])

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,0),-1)

cv2.imshow('img rec',img);
hsvFinal=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
binaryImage = cv2.inRange(hsvFinal, lower_range, upper_range)

cv2.imshow('binaryImage',binaryImage);

cv2.waitKey(0)
cv2.destroyAllWindows()
