import numpy as np
import cv2
camara=cv2.VideoCapture(0)
#----KERNEL PARA LA DETECCIÓN DE BORDES----
kernel1=np.array([[-1,0,1],
                  [0,0,0],
                  [-1,0,1]])
while True:
    #leer las imagenes de la camara
    estado,frame=camara.read()
    #convertir la imagen BGR a grises
    Ig=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #---------ECUALIZACIÓN DEL HISTOGRAMA (RESALTAR EL CONTRASTE)
    Icon=cv2.equalizeHist(Ig)
    #APLICAR UN FILTRO PARA ELIMINAR EL RUIDO
    Isinr=cv2.GaussianBlur(Icon,(3,3),1)
    #------REALIZAR LA CONVOLUCIÓN 2D DE LA IMAGEN Y EL KERNEL
    #img2=cv2.filter2D(Isinr,-1,kernel=kernel1)
    img2=cv2.Canny(Isinr,0,255)
    #CONVERTIR LA IMAGEN EN UNO BINARIO
    imgb=np.where(img2>=20,255,0)
    imgb=np.uint8(imgb)
    #------------------------------------------------------------
    cv2.imshow("IMAGEN ORIGINAL GRISES",Ig)
    cv2.imshow("IMAGEN ECUALIZADA GRISES",Icon)
    cv2.imshow("IMAGEN CONVOLUCIONADA Y BINARIA",imgb)
    #----ESPERAR A PRESIONAR LA TECLA q PARA CERRAR LA APLICACIÓN
    if cv2.waitKey(1)==ord("q"):
        camara.release()
        cv2.destroyAllWindows()
        break