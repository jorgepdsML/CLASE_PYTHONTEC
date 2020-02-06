"""
bloques try-except para manipular errores
"""
"""
try:
    a = float(input("INGRESAR VARIABLE 1: "))
    b = float(input("INGRESAR VARIABLE 2: "))
    c = a + b
    print("SUMA ES : {}".format(c))
    d=a/b
    print("DIVISIÓN ES: {} ".format(d))
except ZeroDivisionError:
    print("DENOMINADOR FUE IGUAL A 0")
except:
    print("HUBO ERROR DENTRO DEL BLOQUE try")
"""
import sys
while True:
    try:
        x1=float(input("DATO 1: "))
        x2=float(input("DATO 2: "))
        print("MULTIPLICACIÓN ES {} ".format(x1*x2))
        break
    except:
        print("SEGUIR INTENTANDO")
    finally:
        print("BLOQUE FINALLY")

