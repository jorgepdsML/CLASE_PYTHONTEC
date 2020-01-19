import os
import time
#crear un archivo de texto
archivo=open("sensor.txt","a")
#metodo write
archivo.write("HOLA A TODOS\nPYTHON\n")
#cerrar el objeto
archivo.close()
time.sleep(2)
os.system("sensor.txt")
contenido=os.listdir()
print(contenido)
if "carpeta" in contenido:
    print("ESTA CARPETA YA EXISTE")
else:
    os.mkdir("carpeta")
