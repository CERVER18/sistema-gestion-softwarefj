from logger import registrar_log

class GestorSistema:
    """Clase para manejar las listas internas sin base de datos."""
    def __init__(self):
        self.clientes = []
        self.servicios = []
        self.reservas_historial = []

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)
        registrar_log(f"Cliente añadido a la lista: {cliente.nombre}")

    def registrar_operacion(self, reserva):
        self.reservas_historial.append(reserva)
