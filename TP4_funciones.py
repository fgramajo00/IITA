################################### FUNCIONES #############################################

# 1)  Define una función llamada raiz_cubica que devuelva el valor de 3√x.
# (Nota: recuerda que 3√x es x˄1/3 y ándate con ojo, no sea que utilices 
#  una división entera y eleves x a la potencia 0, que es el resultado de calcular 1/3.) 

# def raiz_cuadrada(valor):
#     return valor ** (1/3)

# numero = float(input("Ingrese un numero: "))
# resultado = raiz_cuadrada(numero)
# print("El resultado del calculo es: " ,resultado)


# 2)  Define una función llamada area_circulo que, a partir del radio de un círculo, devuelva el valor de su área.
# Utiliza el valor 3.1416 como aproximación de π o importa el valor de π que encontrarás en el módulo math. (Recuerda que el área de un círculo es πr**2.)

# def area_circulo(radio):
#     return 3.141516 * radio
# circulo = float(input("Ingrese un valor: "))
# valor_circulo = area_circulo(circulo)
# print("El area del circulo es: ", valor_circulo)

# 3)  Define una función que convierta grados Farenheit en grados centígrados.
# (Para calcular los grados centígrados has de restar 32 a los grados Farenheit y multiplicar el resultado por cinco novenos.)

# def convertidor_de_grados(gradosFht):
#     return ((gradosFht - 32)*5)/9
# grados = int(input("Ingrese grados convertir :"))
# print(convertidor_de_grados(grados), "°F")


# 5)  Y ahora, un problema más complicado. Vamos a diseñar una función que nos diga si 
# un número dado es o no es perfecto. Se dice que un número es perfecto si es igual a la suma de todos sus divisores
# excluido él mismo. Por ejemplo, 28 es un número perfecto, pues sus divisores (excepto él mismo) son 1, 2, 4, 7 y 14, que suman 28.

# def es_perfecto(numero):
#     suma_divisores = 0
#     for divisor in range(1, numero):
#         if numero % divisor == 0:
#             suma_divisores += divisor
#     return suma_divisores == numero

# numero = int(input("Ingrese un nro: "))
# if es_perfecto(numero):
#     print(numero, "es un número perfecto")
# else:
#     print(numero, "no es un número perfecto")


# import os
# def limpiar_pantalla():
#      os.system('cls')
#      return

# def calculos_aritmeticos(dividendo, divisor):
#     while divisor == 0:
#         divisor = float(input("Ingrese un valor mayor: "))
#     else:
#         division = dividendo / divisor
#         division = round(division,2)
#         suma = dividendo + divisor
#         resta = dividendo - divisor
#         multiplicacion = dividendo * divisor
#     return(print(f"El resultado es, suma: {suma}, resta: {resta}, multiplicacion: {multiplicacion}, division: {division}"))
    

# limpiar_pantalla()
# valor1=float(input("Ingrese un valor: "))
# valor2=float(input("Ingrese un valor: "))
# calculos_aritmeticos(valor1, valor2)

##################################### PRACTICO FUNCIONES ###################################

#1.Escriba una función que muestre todos los números primos entre 1 y un número n que es ingresado por parámetro.
# def es_primo(numero):
#     if numero <= 1:
#         return False
#     for i in range(2, int(numero ** 0.5) + 1):
#         if numero % i == 0:
#             return False
#     return True


# numero = 17
# if es_primo(numero):
#     print(f"{numero} es un número primo")
# else:
#     print(f"{numero} no es un número primo")


# 2.Escriba una función que le pida al usuario ingresar condimentos para un sándwich, hasta
# que el usuario ingrese ‘salir’. Cada vez que se ingrese un condimento, muestre un mensaje
# avisando que ya se agregó el condimento al sándwich. Escriba versiones diferentes del
# programa de acuerdo a estos criterios:
# • Use un test condicional en el ciclo while para detener la ejecución.
# • Use un test condicional dentro del ciclo para decidir si continuar la ejecución. 

# def armar_apretao():
#     continuar = True
#     while continuar:
#         condimento = input("Como quiere su milanesa !! (o 'salir' para no colocar aderezos)")
#         if condimento == 'salir':
#             continuar = False
#         else:
#             print(f"La milanesa tiene los {condimento}")
#     print("Pase por caja a pagar su milanesa !!!")
        
# armar_apretao()



# 3. A) Remera: Escriba una función “hacer_remera()” que tome como parámetros un
# tamaño y el mensaje que debería ir impreso en la remera. La función debe mostrar un mensaje
# describiendo el tamaño de la remera y el mensaje impreso en ella. Llame la función una vez
# usando argumentos por posición. Llámela una segunda vez usando argumentos por clave.
# B) Remeras Grandes: Modifique la “funcion hacer_remera()” para que el tamaño por
# defecto sea ‘L’ y el mensaje, ‘Me gusta Python’. Haga un par de remeras, la primera con los
# valores por defecto, y la segunda con valores diferentes. 

# def hacer_remera(tamaño, mensaje):
#     print(f"Se ha creado una remera de tamaño {tamaño} con el mensaje: {mensaje}")

# # Llamada a la función usando argumentos por posición
# hacer_remera('M', 'IITA, Programacion!')

# # Llamada a la función usando argumentos por clave
# hacer_remera(mensaje='Python es lo mas !', tamaño='S')

# def hacer_remera(tamaño='L', mensaje='Python es mi hobby'):
#     print(f"Se ha creado una remera de tamaño {tamaño} con el mensaje: {mensaje}")

# # Remera con valores por defecto
# hacer_remera()

# # Remera con valores diferentes
# hacer_remera(tamaño='XL', mensaje='IITA, Programacion!')


# 4. Serie de Fibonacci: Escriba una función fibonacci(n) que devuelva los n primeros numeros
# de la serie de Fibonacci. En esta serie, los primeros dos números son 0 y 1, y cada sucesivo
# número es la suma de los dos números inmediatamente anteriores (ejemplo: 0,1,1,2,3,5,8, …)

# def fibonacci(n):
#     if n <= 0:
#         return []
#     elif n == 1:
#         return [0]
#     elif n == 2:
#         return [0, 1]
#     else:
#         fib_seq = [0, 1]
#         while len(fib_seq) < n:
#             next_num = fib_seq[-1] + fib_seq[-2]
#             fib_seq.append(next_num)
#         return fib_seq

# n = 10
# fib_nums = fibonacci(n)
# print(f"Los {n} primeros números de la serie de Fibonacci son: {fib_nums}")