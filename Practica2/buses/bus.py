class Buses:
    def __init__(self, numero, ruta):
        self.numero = numero
        self.ruta = ruta
        self.horarios = []
        self.conductores_asignados = []
    
    def agregar_horario(self, horario):
        self.horarios.append(horario)
    
    def asignar_conductor(self, conductor):
        if conductor.horario not in self.horarios:
            print(f"El conductor {conductor.nombre} no tiene horario para este bus.")
        else:
            self.conductores_asignados.append(conductor)
            conductor.bus_asignado = self
            print(f"Conductor {conductor.nombre} asignado al bus {self.numero}.")
    
    def __str__(self):
        return f"Bus #{self.numero} - Ruta: {self.ruta}"
