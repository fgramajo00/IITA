# 1. Escriba una función redondear() que permita redondear un número
# decimal de acuerdo al criterio: Si el número es mayor a 3.50, devolver el
# entero siguiente (en este caso, 4), si no devolver el entero inmediatamente
# anterior (3). 
def limpiar_pantalla():
    import os
    os.system('cls')

def redondear(x):
    return print(round(x))

def suma(x,b):
    resultado = x + b
    print (resultado)
    redondear(resultado)
    return 

def hora_actual():
    from datetime import datetime
    ahora = datetime.now()
    print(ahora)


def bola_ocho(azar):
    pregunta = input("Soy una bola magica, hazme una pregunta: ") 
    while True:
        if azar == 1:
            print("Es seguro que sí")
        elif azar == 2:
            print("Las chances son buenas")
        elif azar == 3:
            print("Puedes contar con ello")
        elif azar == 4:
            print("Pregúntame de nuevo más tarde")
        elif azar == 5:
            print("Concéntrate y pregunta de nuevo")
        elif azar == 6:
            print("No veo con claridad, intenta de nuevo")
        elif azar == 7:
            print("Mi respuesta es no")
        elif azar == 8:
            print("Mis fuentes me dicen que no")
        break
            
    



