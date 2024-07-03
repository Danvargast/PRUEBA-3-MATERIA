import json
libros = []
def agregar_libro(libros, titulo, autor):
    libro_nuevo = {}
    libro_nuevo["titulo"] = titulo
    libro_nuevo["Autor"] = autor
    libro_nuevo["estado"] = estado
    libros.append(libro_nuevo)
def marcar_prestado(libros,titulo):
    for i in libros:
        if i["titulo"] == titulo: 
            i["estado"] = "prestado"

def listar_libros(libros):
    print(libros)

def guardar_libros(libros, nombre_archivo):
    with open(nombre_archivo, "w") as archivo:
        json.dump(libros, archivo)
def cargar_libros(nombre_archivo):
    global libros
    with open(nombre_archivo, "r") as archivo:
        libros = json.load(archivo)
while True:
    print("Bienvenido a la biblioteca python: ")
    print("¿Qué desea hacer? (Ingrese el número)")
    print("""1.Agregar libros
2.Marcar como prestado un libro
3.Listar libros
4.Guardar libros
5.Cargar libros
6.Salir""")
    opcion = int(input(""))
    if opcion == 1:
        titulo = input("Ingresa el título del nuevo libro: ")
        autor = input("Ingresa el autor del libro: ")
        estado = "Disponible"
        agregar_libro(libros,titulo,autor)
    if opcion == 2:
        titulo = input("Ingrese el título del libro: ")
        marcar_prestado(libros,titulo)
    if opcion == 3:
        listar_libros(libros)
    if opcion == 4:
        nombre_archivo = input("Ingresa el nombre del archivo: ") + ".json"
        guardar_libros(libros, nombre_archivo)
    if opcion == 5:
        nombre_archivo = input("Ingrese el nombre del archivo: ")
        cargar_libros(nombre_archivo)
    if opcion == 6:
        break


