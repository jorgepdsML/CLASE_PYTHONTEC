import numpy as np
a1=np.array([[200,30],[50,100]])
b1=np.array([[10,10],[1,1]])
#multiplicación elemento a elemento
c1=a1*b1
#multiplicación matricial
d1=np.matmul(a1,b1)
print(c1)
#la función where
a2=np.where(a1>=60,255,0)
print("MATRIZ a1 es : \n",a1)
print("MATRIZ a2 es ; \n ",a2)

import cv2
cam=cv2.VideoCapture(0)
while True:
    ret,frame=cam.read()
    #escala de grises
    gris=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #función where
    bina=np.where(gris>=60,255,0)
    cv2.imshow("IMAGEN BINARIZADA CON FUNCIÓN where",np.uint8(bina))
    if cv2.waitKey(1)==ord("q"):
        break
cam.release()
cv2.destroyAllWindows()
print(type(gris))