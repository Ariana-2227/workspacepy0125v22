class Conductor:
    def __init__(self, nombre, horario):
        self.nombre = nombre
        self.horario = horario
        self.bus_asignado = None
    
    def __str__(self):
        return f"{self.nombre} ({self.horario})"