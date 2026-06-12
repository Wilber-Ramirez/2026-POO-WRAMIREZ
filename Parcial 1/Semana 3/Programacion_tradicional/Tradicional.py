
def registrar_mascota():
    print("=== Registro de Mascota ===")
    nombre = input("Ingrese el nombre de su mascota: ")
    especie = input("Ingrese la especie de la mascota (ej: perro, gato, ave): ")
    edad = input("Ingrese la edad de la mascota: ")

    return nombre, especie, edad


def mostrar_informacion(datos_mascota):
    print("\n=== Información de la Mascota ===")
    print(f"Nombre: {datos_mascota[0]}")
    print(f"Especie: {datos_mascota[1]}")
    print(f"Edad: {datos_mascota[2]} años")


if __name__ == "__main__":

    datos = registrar_mascota()
    mostrar_informacion(datos)
