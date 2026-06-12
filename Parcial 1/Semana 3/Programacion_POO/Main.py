
from Mascota import Mascota

if __name__ == "__main__":

    mascota1 = Mascota("Max", "Perro", 4)
    mascota2 = Mascota("Luna", "Gato", 2)


    print("=== Mascota 1 ===")
    mascota1.mostrar_informacion()
    mascota1.hacer_sonido()

    print("\n=== Mascota 2 ===")
    mascota2.mostrar_informacion()
    mascota2.hacer_sonido()
