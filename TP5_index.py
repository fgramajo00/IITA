from TP5_modulos import redondear, suma, hora_actual, bola_ocho, limpiar_pantalla

# Ejercicio 1:
# nro = float(input("Ingrese un nro: "))
# redondear(nro)

# # Ejercicio 2:
# x = float(input("Ingrese un valor: "))
# b = float(input("Ingrese un valor: "))
# suma(x,b)

# #Ejercicio 3:
# hora_actual()

#Ejercicio 4:
# import random 
# while True:
#     par=random.randrange(2,10)
#     if par % 2 == 0:
#         print(par)
#         break
        
#Ejercicio 5-6:
# import random
# import time
# start_time = time.time()
# limpiar_pantalla()
# print(" ### Soy una magica bola 8 ### ")
# azar = random.randint(1,8)
# bola_ocho(azar)
# end_time = time.time()
# tiempo_de_ejecucion = end_time-start_time
# print("El tiempo de ejecucion: ", tiempo_de_ejecucion, "segundos.")

#opcional

import datetime

def calcular_dias_desde_nacimiento():
    fecha_nacimiento = input("Ingrese su fecha de nacimiento (formato: DD/MM/AAAA): ")
    dia, mes, anio = map(int, fecha_nacimiento.split('/'))

    fecha_actual = datetime.date.today()
    fecha_nacimiento = datetime.date(anio, mes, dia)
    dias_transcurridos = (fecha_actual - fecha_nacimiento).days

    return dias_transcurridos

# Ejemplo de uso
dias_desde_nacimiento = calcular_dias_desde_nacimiento()
print("Han transcurrido", dias_desde_nacimiento, "días desde su nacimiento.")



