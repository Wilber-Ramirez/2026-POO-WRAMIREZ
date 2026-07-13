# Clase Cliente - representa un cliente del restaurante
class Cliente:
    """
    Clase que representa un cliente registrado en el restaurante.
    Encapsula únicamente la información del cliente.
    """
    
    def __init__(self, identificacion: str, nombre: str, correo: str) -> None:
        """
        Constructor de la clase Cliente.
        
        Args:
            identificacion: Identificación única del cliente (cédula, pasaporte, etc.)
            nombre: Nombre completo del cliente
            correo: Correo electrónico del cliente
            
        Raises:
            ValueError: Si los datos no cumplen con las validaciones
        """
        if not identificacion or not identificacion.strip():
            raise ValueError("La identificación del cliente no puede estar vacía.")
        if not nombre or not nombre.strip():
            raise ValueError("El nombre del cliente no puede estar vacío.")
        if not correo or not correo.strip():
            raise ValueError("El correo del cliente no puede estar vacío.")
        
        self.identificacion: str = identificacion.strip()
        self.nombre: str = nombre.strip()
        self.correo: str = correo.strip()
    
    def mostrar_informacion(self) -> str:
        """Retorna la información del cliente en formato legible."""
        return (
            f"[CLIENTE] Identificación: {self.identificacion} | "
            f"Nombre: {self.nombre} | Correo: {self.correo}"
        )
    
    def __repr__(self) -> str:
        """Representación en string del objeto Cliente."""
        return (
            f"Cliente(identificacion='{self.identificacion}', "
            f"nombre='{self.nombre}', correo='{self.correo}')"
        )
