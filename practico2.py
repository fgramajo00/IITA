import json

# Función para cargar la base de datos desde un archivo JSON
def cargar_base_de_datos_json(archivo):
    try:
        with open(archivo, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Función para guardar la base de datos en un archivo JSON
def guardar_base_de_datos_json(usuarios, archivo):
    with open(archivo, 'w') as f:
        json.dump(usuarios, f, indent=4)

# Función para agregar un nuevo usuario
def agregar_usuario(usuarios, nuevo_usuario):
    usuarios.append(nuevo_usuario)

# Función para buscar un usuario por correo electrónico
def buscar_usuario_por_correo(usuarios, correo):
    return next((usuario for usuario in usuarios if usuario["correo"] == correo), None)

# Función para actualizar información de un usuario
def actualizar_usuario(usuarios, usuario_actualizado):
    for i, usuario in enumerate(usuarios):
        if usuario["correo"] == usuario_actualizado["correo"]:
            usuarios[i] = usuario_actualizado
            break

# Función para eliminar un usuario
def eliminar_usuario(usuarios, correo):
    usuarios[:] = [usuario for usuario in usuarios if usuario["correo"] != correo]

# Función principal
def main():
    archivo_json = "usuarios.json"
    
    usuarios = cargar_base_de_datos_json(archivo_json)

    # Operaciones CRUD
    # Agregar un nuevo usuario
    nuevo_usuario = {
        "nombre": "Laura",
        "apellido": "Perez",
        "correo": "laura.perez@abccorp.com",
        "departamento": "Marketing",
        "cargo": "Analista de Marketing",
        "fecha_contratacion": "2021-02-10"
    }
    agregar_usuario(usuarios, nuevo_usuario)
    
    # Leer información de un usuario
    correo_buscar = "maria.lopez@abccorp.com"
    usuario_encontrado = buscar_usuario_por_correo(usuarios, correo_buscar)
    if usuario_encontrado:
        print("Información del usuario encontrado:")
        print(usuario_encontrado)
    else:
        print("Usuario no encontrado.")
    
    # Actualizar información de un usuario
    usuario_a_actualizar = {
        "nombre": "Juan",
        "apellido": "Gomez",
        "correo": "juan.gomez@abccorp.com",
        "departamento": "Ventas",
        "cargo": "Gerente de Ventas",
        "fecha_contratacion": "2020-05-15"
    }
    actualizar_usuario(usuarios, usuario_a_actualizar)
    
    # Eliminar un usuario
    correo_a_eliminar = "laura.perez@abccorp.com"
    eliminar_usuario(usuarios, correo_a_eliminar)
    
    # Guardar la base de datos actualizada en formato JSON
    guardar_base_de_datos_json(usuarios, archivo_json)
    
    # Imprimir la base de datos actualizada en JSON
    print("Base de datos actualizada en JSON:")
    for usuario in usuarios:
        print(usuario)

if __name__ == "__main__":
    main()
