class SoftwareFJError(Exception):
    """Clase base para todas las excepciones del sistema."""
    pass

class ErrorValidacion(SoftwareFJError):
    """Se lanza cuando los datos ingresados no cumplen las reglas de negocio."""
    pass

class ErrorOperativo(SoftwareFJError):
    """Se lanza cuando falla una operación en tiempo de ejecución (ej. cálculos)."""
    pass
