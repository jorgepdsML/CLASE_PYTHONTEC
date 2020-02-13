import numpy as np
import cv2
#leer o cargar una imagen
#en otro directorio
#img=cv2.imread("C:\\Users\\pdsjo\\Desktop\\imagen2\\imagen.png")
#en mi mismo proyecto o directorio
img=cv2.imread("imagen.png")
print(type(img))
#realizar el cambio de escala de color
grises=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
#---OPERACIÓN PARA ELEVAR EL BRILLO DE UNA IMAGEN-----
gris2=grises+30
#img[:][:][0] accediendo a la capa 0
print("FORMA DE LA IMG: ", np.shape(img))
print("CANTIDAD DE PIXELES IMAGEN RGB",np.size(img))
print("FORMA DE LA IMAGEN GRISES",np.shape(grises))
print("CANTIDAD DE PIXELES IMAGEN GRISES",np.size(grises))
cv2.imshow("IMAGEN EN ESCALA RGB ",img)
cv2.imshow("IMAGEN EN ESCALA GRAY ",grises)
cv2.imshow("IMAGEN EN ESCALA GRAY2 ",gris2)
print(grises)
print(gris2)
cv2.waitKey(0)
print("FIN DEL PROGRAMA")
cv2.destroyAllWindows()
