import numpy as np
import cv2
#realizar la lectura de una imagen
#----BGR----
img=cv2.imread("imagen.png")
#determinar el numero de dimensiones
dimen=img.ndim
#determinar la forma
forma=img.shape
print("dimensiones ",dimen)
print("forma ",forma)
b=img[:,:,0]
g=img[:,:,1]
r=img[:,:,2]
cv2.imshow("IMAGEN1",img)
#eliminando toda la capa rojo
img[:,:,2]=0
cv2.imshow("IMAGEN SIN ROJO",img)
#combinación de capas
ig=0.29*r+0.58*g+0.114*b
#convertir a entero
i2=np.uint8(ig)
#ecualizar el histograma
i2e=cv2.equalizeHist(i2)
cv2.imshow("IMAGEN EN ESCALA GRISES",i2)
cv2.imshow("IMAGEN ECUALIZADA",i2e)
#CALCULAR EL HISTOGRAMA DE UNA IMAGEN A ESCALA DE GRISES
histo=cv2.calcHist([i2],[0],None,[256],[0,256])
histoe=cv2.calcHist([i2e],[0],None,[256],[0,256])
cv2.waitKey(0)
from matplotlib import pyplot as plt
plt.subplot(121)
plt.plot(histo)
plt.title("HISTOGRAMA")
plt.xlabel("NIVEL DE INTENSIDAD")
plt.ylabel("NÚMERO DE PIXELES")
plt.subplot(122)
plt.plot(histoe)
plt.title("HISTOGRAMA ECUALIZADO")
plt.xlabel("NIVEL DE INTENSIDAD")
plt.ylabel("NÚMERO DE PIXELES")
plt.show()

