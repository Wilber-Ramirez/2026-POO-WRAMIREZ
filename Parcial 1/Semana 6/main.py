
from modelos import Platillo, Bebida
from servicios import Restaurante


def main():
    """Función principal que ejecuta el sistema restaurante_app."""

    restaurante = Restaurante("La Buena Mesa")
    
    print("\n" + "="*50)
    print("  SISTEMA DE GESTIÓN DE RESTAURANTE")
    print("="*50 + "\n")
    
    # Crear platillos
    # Platillo 1: Entrada
    ensalada_cesar = Platillo(
        nombre="Ensalada César",
        precio=12.50,
        tipo_platillo="Entrada",
        calorias=280,
        tiempo_preparacion=10
    )
    
    # Platillo 2: Plato Fuerte
    pechuga_champiñones = Platillo(
        nombre="Pechuga de Pollo con Champiñones",
        precio=18.99,
        tipo_platillo="Plato Fuerte",
        calorias=450,
        tiempo_preparacion=25
    )
    
    # Platillo 3: Postre
    flan_caramelo = Platillo(
        nombre="Flan de Caramelo",
        precio=8.50,
        tipo_platillo="Postre",
        calorias=320,
        tiempo_preparacion=5
    )
    
    # Crear bebidas
    # Bebida 1: Gaseosa
    coca_cola = Bebida(
        nombre="Coca Cola",
        precio=2.99,
        tipo_bebida="Gaseosa",
        volumen_ml=355,
        es_fria=True
    )
    
    # Bebida 2: Bebida Caliente
    cafe_expreso = Bebida(
        nombre="Café Expreso",
        precio=3.50,
        tipo_bebida="Café",
        volumen_ml=30,
        es_fria=False
    )
    
    # Bebida 3: Jugo
    jugo_naranja = Bebida(
        nombre="Jugo Natural de Naranja",
        precio=4.00,
        tipo_bebida="Jugo",
        volumen_ml=250,
        es_fria=True
    )
    
    # Agregar todos los productos al restaurante
    print("Agregando productos al menú:\n")
    restaurante.agregar_producto(ensalada_cesar)
    restaurante.agregar_producto(pechuga_champiñones)
    restaurante.agregar_producto(flan_caramelo)
    restaurante.agregar_producto(coca_cola)
    restaurante.agregar_producto(cafe_expreso)
    restaurante.agregar_producto(jugo_naranja)
    
    # Mostrar el menú completo (demuestra polimorfismo)
    restaurante.mostrar_menu()
    
    # Demostrar encapsulación y validación de precio
    print("\n--- DEMOSTRANDO ENCAPSULACIÓN Y VALIDACIÓN ---")
    try:
        print(f"\nPrecio actual de Ensalada César: ${ensalada_cesar.obtener_precio():.2f}")
        ensalada_cesar.cambiar_precio(14.99)
        print(f"Nuevo precio de Ensalada César: ${ensalada_cesar.obtener_precio():.2f}")
        
        # Intentar establecer un precio inválido
        ensalada_cesar.cambiar_precio(-5)
    except ValueError as e:
        print(f"✗ Error: {e}")
    
    # Mostrar platillos y bebidas por separado
    restaurante.mostrar_platillos()
    restaurante.mostrar_bebidas()
    
    # Demostrar cambio de disponibilidad
    print("\n--- CAMBIO DE DISPONIBILIDAD ---")
    print(f"Estado actual de Café Expreso: {cafe_expreso.obtener_disponibilidad()}")
    cafe_expreso.cambiar_disponibilidad(False)
    print(f"Nuevo estado de Café Expreso: {cafe_expreso.obtener_disponibilidad()}")
    
    print("\n" + "="*50)
    print("  FIN DEL PROGRAMA")
    print("="*50 + "\n")


if __name__ == "__main__":
    main()
