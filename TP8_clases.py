#ej N1
# class rectangulo:
#     def __init__(self, base, altura):
#         self.base = base
#         self.altura = altura
#     def calcular_area(self):
#         return self.base * self.altura

# base = float(input("ingrese la base de su rectangulo: "))
# altura = float(input("ingrese la base de rectangulo: "))
# mi_rectangulo = rectangulo(base, altura)
# area_rectangulo = mi_rectangulo.calcular_area()
# print(area_rectangulo)

#ej N2
# class Mate:
#     def __init__(self, n):
#         self.n = n
#         self.cebadas_restantes = 0
#         self.lleno = False

#     def cebar(self):
#         try:
#             if self.lleno:
#                 raise Exception("¡Cuidado! ¡Te quemaste!")
#             else:
#                 self.lleno = True
#                 self.cebadas_restantes = self.n
#         except Exception as e:
#             print(e)

#     def beber(self):
#         if self.cebadas_restantes > 0:
#             print("Tomando una cebada...")
#             self.cebadas_restantes -= 1
#             if self.cebadas_restantes == 0:
#                 print("Advertencia: el mate está lavado.")
#         else:
#             raise Exception("¡El mate está vacío!")
# #Proban funcionamiento
# mate = Mate(10)
# mate.cebar()
# mate.beber()
# mate.cebar()
# mate.beber()
# mate.beber()

#ej N3
# class Corcho:
#     def __init__(self, bodega):
#         self.bodega = bodega

# class Botella:
#     def __init__(self):
#         self.corcho = None

# class Sacacorchos:
#     def __init__(self):
#         self.corcho_extraido = None

#     def destapar(self, botella):
#         if botella.corcho is None:
#             raise Exception("La botella ya está destapada.")
#         if self.corcho_extraido is not None:
#             raise Exception("El sacacorchos ya contiene un corcho.")
        
#         self.corcho_extraido = botella.corcho
#         botella.corcho = None

#     def limpiar(self):
#         if self.corcho_extraido is None:
#             raise Exception("El sacacorchos no tiene un corcho.")
        
#         corcho = self.corcho_extraido
#         self.corcho_extraido = None
#         return corcho

# # Ejemplo de uso:
# corcho1 = Corcho("Bodega A")
# corcho2 = Corcho("Bodega B")

# botella1 = Botella()
# botella1.corcho = corcho1

# botella2 = Botella()
# botella2.corcho = corcho2

# sacacorchos = Sacacorchos()

# try:
#     sacacorchos.destapar(botella1)
#     print("Se destapó la botella 1 con corcho de la bodega:", botella1.corcho.bodega)
# except Exception as e:
#     print(e)

# try:
#     sacacorchos.destapar(botella2)
#     print("Se destapó la botella 2 con corcho de la bodega:", botella2.corcho.bodega)
# except Exception as e:
#     print(e)

# try:
#     sacacorchos.destapar(botella2)
# except Exception as e:
#     print(e)

# try:
#     corcho_extraido = sacacorchos.limpiar()
#     print("Se limpió el corcho de la bodega:", corcho_extraido.bodega)
# except Exception as e:
#     print(e)

#ej N4

# class Restaurante:
#     def __init__(self, restaurante_nombre, tipo_comida):
#         self.restaurante_nombre = restaurante_nombre
#         self.tipo_comida = tipo_comida

#     def describir_restaurante(self):
#         print(f"Nombre del restaurante: {self.restaurante_nombre}")
#         print(f"Tipo de comida: {self.tipo_comida}")

#     def abrir_restaurante(self):
#         print(f"El restaurante {self.restaurante_nombre} está abierto.")

# class Heladeria(Restaurante):
#     def __init__(self, restaurante_nombre, tipo_comida, sabores):
#         super().__init__(restaurante_nombre, tipo_comida)
#         self.sabores = sabores

#     def mostrar_sabores(self):
#         print(f"Sabores de helado disponibles en {self.restaurante_nombre}:")
#         for sabor in self.sabores:
#             print("- " + sabor)


# sabores_heladeria = ["Vainilla", "Chocolate", "Fresa", "Mango"]

# heladeria = Heladeria("La Heladería Delicioso", "Heladería", sabores_heladeria)
# heladeria.describir_restaurante()
# heladeria.abrir_restaurante()
# heladeria.mostrar_sabores()

#ej N5
# class Personaje:
#     def __init__(self, vida, posicion, velocidad):
#         self.vida = vida
#         self.posicion = posicion
#         self.velocidad = velocidad

#     def recibir_ataque(self, cantidad_ataque):
#         self.vida -= cantidad_ataque
#         if self.vida <= 0:
#             raise Exception("El personaje ha sido derrotado.")

#     def mover(self, direccion):
#         if direccion not in ["arriba", "abajo", "izquierda", "derecha"]:
#             raise ValueError("Dirección no válida. Use 'arriba', 'abajo', 'izquierda' o 'derecha'.")
        
#         if direccion == "arriba":
#             self.posicion[1] += self.velocidad
#         elif direccion == "abajo":
#             self.posicion[1] -= self.velocidad
#         elif direccion == "izquierda":
#             self.posicion[0] -= self.velocidad
#         elif direccion == "derecha":
#             self.posicion[0] += self.velocidad

# class Soldado(Personaje):
#     def __init__(self, vida, posicion, velocidad, ataque):
#         super().__init__(vida, posicion, velocidad)
#         self.ataque = ataque

#     def atacar(self, otro_personaje):
#         otro_personaje.recibir_ataque(self.ataque)

# class Campesino(Personaje):
#     def __init__(self, vida, posicion, velocidad, cosecha):
#         super().__init__(vida, posicion, velocidad)
#         self.cosecha = cosecha

#     def cosechar(self):
#         return self.cosecha

# soldado1 = Soldado(100, [0, 0], 5, 20)
# campesino1 = Campesino(50, [10, 10], 3, 30)

# print("Posición inicial del soldado:", soldado1.posicion)
# soldado1.mover("arriba")
# print("Posición después de mover hacia arriba:", soldado1.posicion)

# print("Vida del campesino:", campesino1.vida)
# soldado1.atacar(campesino1)
# print("Vida del campesino después de ser atacado:", campesino1.vida)

# print("Cantidad cosechada por el campesino:", campesino1.cosechar())

#ej N6
# class Usuario:
#     def __init__(self, nombre, apellido, edad, correo, pais):
#         self.nombre = nombre
#         self.apellido = apellido
#         self.edad = edad
#         self.correo = correo
#         self.pais = pais

#     def describir_usuario(self):
#         print("Información del usuario:")
#         print(f"Nombre: {self.nombre}")
#         print(f"Apellido: {self.apellido}")
#         print(f"Edad: {self.edad}")
#         print(f"Correo: {self.correo}")
#         print(f"País: {self.pais}")

#     def saludar_usuario(self):
#         print(f"Hola, {self.nombre} {self.apellido}. ¡Bienvenido!")


# usuario1 = Usuario("Federico", "Gramajo", 45, "fedegramajo@example.com", "Tucuman")
# usuario2 = Usuario("María", "Gómez", 25, "maria@example.com", "Salta")

# usuario1.describir_usuario()
# usuario1.saludar_usuario()

# print("\n") #Salto de Linea

# usuario2.describir_usuario()
# usuario2.saludar_usuario()





#ej N7
# class Usuario:
#     def __init__(self, nombre, correo):
#         self.nombre = nombre
#         self.correo = correo

#     def mostrar_informacion(self):
#         print(f"Nombre: {self.nombre}")
#         print(f"Correo: {self.correo}")

# class Admin(Usuario):
#     def __init__(self, nombre, correo, privilegios):
#         super().__init__(nombre, correo)
#         self.privilegios = privilegios

#     def mostrar_privilegios(self):
#         print(f"Privilegios del administrador {self.nombre}:")
#         for privilegio in self.privilegios:
#             print("- " + privilegio)


# privilegios_admin = ["puede postear en el foro", "puede borrar un post", "puede banear usuario"]
# administrador = Admin("Admin123", "admin@example.com", privilegios_admin)

# administrador.mostrar_informacion()
# administrador.mostrar_privilegios()

