from conductores.conductor import Conductor
from buses.bus import Buses

class Admin:
    def __init__(self,buses,conductores):
        self.buses = []
        self.conductores = []
    
    def agregar_bus(self, numero, ruta):
        bus = Buses(numero, ruta)
        self.buses.append(bus)
        print(f"Bus {numero} con ruta {ruta} agregado.")
    
    def agregar_ruta_a_bus(self, numero_bus, ruta):
        for bus in self.buses:
            if bus.numero == numero_bus:
                bus.ruta = ruta
                print(f"Ruta del bus #{numero_bus} actualizada a {ruta}.")
                return
        print(f"Bus #{numero_bus} no encontrado.")
    
    def registrar_horario_a_bus(self, numero_bus, horario):
        for bus in self.buses:
            if bus.numero == numero_bus:
                bus.agregar_horario(horario)
                print(f"Horario {horario} agregado al bus #{numero_bus}.")
                return
        print(f"Bus #{numero_bus} no encontrado.")
    
    def agregar_conductor(self, nombre, horario):
        conductor = Conductor(nombre, horario)
        self.conductores.append(conductor)
        print(f"Conductor {nombre} con horario {horario} agregado.")
    
    def agregar_horario_a_conductor(self, nombre, horario):
        for conductor in self.conductores:
            if conductor.nombre == nombre:
                conductor.horario = horario
                print(f"Horario de conductor {nombre} actualizado a {horario}.")
                return
        print(f"Conductor {nombre} no encontrado.")
    
    def asignar_bus_a_conductor(self, nombre_conductor, numero_bus):
        conductor = next((c for c in self.conductores if c.nombre == nombre_conductor), None)
        bus = next((b for b in self.buses if b.numero == numero_bus), None)
        
        if conductor is None:
            print(f"Conductor {nombre_conductor} no encontrado.")
            return
        if bus is None:
            print(f"Bus #{numero_bus} no encontrado.")
            return
        bus.asignar_conductor(conductor)
