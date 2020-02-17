"""
REALIZAR LA COMUNICACIÓN ENTRE PYTHON Y ARDUINO
"""
#tener instalado pyserial
import serial
#crear un objeto de la clase Serial del modulo serial
arduino=serial.Serial()
#configurar los atributos de nuestro para la comunicación serial
arduino.baudrate=9600
arduino.port="COM4"
#8,N,1
#INICIALIZAR EL PUERTO COM4
arduino.open()
import time
#LEER LO QUE ARDUINO ESTA ENVIANDO EN EL PUERT COM4
while True:
    #detectar si hay caracteres para leer dentro del buffer
    #de recepción
    if arduino.inWaiting()>0:
        while arduino.inWaiting()>0:
            #leer todos los datos:
            #DATOS EN BYTES
            dato=arduino.read()
            #DECODIFICAR BYTES A VERSION DE STRING
            dato=dato.decode()
            print(dato,end="")
            time.sleep(1)
#CERRAR EL RECURSO DE LA COMUNICACIÓN SERIAL
arduino.close()