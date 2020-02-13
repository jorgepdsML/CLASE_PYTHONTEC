import numpy as np
import cv2
from matplotlib import pyplot as plt
img=cv2.imread("imagen.png")
#convertir a escala de grises
grises=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
#determinar su histograma
histo=cv2.calcHist([grises],[0],None,[256],[0,256])
gris2=grises+50
histo2=cv2.calcHist([gris2],[0],None,[256],[0,256])
cv2.imshow("IMAGEN GRAY 1",grises)
cv2.imshow("IMAGEN GRAY 2",gris2)
cv2.waitKey(0)
#plotear el histograma
plt.subplot(121)
plt.plot(histo)
plt.title("HISTOGRAMA 1")
plt.xlabel("NIVEL DE INTENSIDAD")
plt.ylabel("NÚMERO DE PIXELES")
#--------------
plt.subplot(122)
plt.plot(histo2)
plt.title("HISTOGRAMA 2")
plt.xlabel("NIVEL DE INTENSIDAD")
plt.ylabel("NÚMERO DE PIXELES")

plt.show()
