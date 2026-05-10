from entidad_base import EntidadSistema
from excepciones import ErrorValidacion

class Cliente(EntidadSistema):
    def __init__(self, id_cliente, nombre, email):
        super().__init__(id_cliente)
        # Validación robusta
        if not nombre or len(str(nombre)) < 3:
            raise ErrorValidacion("El nombre del cliente debe tener al menos 3 caracteres.")
        if "@" not in str(email) or "." not in str(email):
            raise ErrorValidacion(f"Formato de correo inválido: {email}")
        
        self.__nombre = nombre  # Encapsulamiento (privado)
        self.__email = email    # Encapsulamiento (privado)

    @property
    def nombre(self): return self.__nombre

    @property
    def email(self): return self.__email

    def __str__(self):
        return f"Cliente: {self.__nombre} (ID: {self.id_entidad})"
