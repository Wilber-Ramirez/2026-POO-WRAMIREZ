# Clase que representa un cliente del restaurante

class Cliente:
    """
    Clase que representa un cliente registrado en el sistema del restaurante.
    Almacena información personal y de contacto del cliente.
    """
    
    def __init__(self, cedula: int, nombre: str, correo_electronico: str, telefono: str, es_miembro_frecuente: bool):
        """
        Constructor de la clase Cliente.
        
        Args:
            cedula: Número de cédula del cliente (tipo int)
            nombre: Nombre completo del cliente (tipo str)
            correo_electronico: Correo electrónico del cliente (tipo str)
            telefono: Número de teléfono del cliente (tipo str)
            es_miembro_frecuente: Indica si es cliente frecuente (tipo bool)
        """
        self.cedula: int = cedula
        self.nombre: str = nombre
        self.correo_electronico: str = correo_electronico
        self.telefono: str = telefono
        self.es_miembro_frecuente: bool = es_miembro_frecuente
    
    def __str__(self) -> str:
        """
        Representación en texto de un objeto Cliente.
        
        Returns:
            Cadena de texto con la información del cliente
        """
        estado = "Miembro frecuente" if self.es_miembro_frecuente else "Cliente regular"
        return f"Cliente(Cédula: {self.cedula}, Nombre: {self.nombre}, Estado: {estado})"
    
    def obtener_informacion_contacto(self) -> str:
        """
        Retorna la información de contacto del cliente.
        
        Returns:
            Cadena con correo y teléfono del cliente
        """
        return f"Email: {self.correo_electronico}, Teléfono: {self.telefono}"
    
    def convertir_a_miembro_frecuente(self) -> None:
        """
        Convierte el cliente en miembro frecuente del restaurante.
        """
        self.es_miembro_frecuente = True
