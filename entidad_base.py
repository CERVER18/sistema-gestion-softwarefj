from abc import ABC

class EntidadSistema(ABC):
    """Clase abstracta que define la identidad de los objetos."""
    def __init__(self, id_entidad):
        self._id_entidad = id_entidad  # Atributo protegido

    @property
    def id_entidad(self):
        return self._id_entidad
