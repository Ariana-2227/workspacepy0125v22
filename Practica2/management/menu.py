from clase3.admin import Admin
def Menu():
        msg="""
        BIENVENIDO 
        1. Agregar bus
        2. Agregar conductor
        3. Agregar ruta a bus 
        4. Registrar horario a bus
        5. Agregar conductor
        6. Agregar horario a conductor 
        7. Asignar bus a conductor
        8. SALIR
        """
        while True:
            print(msg)
            opcion=int(input("Ingrese una opción del menu: "))
            match opcion:
                case 1:
                    numero=int(input("Ingrese el numero del bus:"))
                    ruta=str(input("Ingrese la ruta del bus"))
                    Admin.agregar_bus(numero,ruta)
                    pass
                case 2:
                    numero_bus = input("Ingrese número del bus: ")
                    ruta = input("Ingrese ruta del bus: ")
                    Admin.agregar_ruta_a_bus(numero_bus, ruta)
                    pass
                case 3:
                    numero_bus = input("Número del bus: ")
                    horario = input("Horario del bus (hora): ")
                    Admin.registrar_horario_a_bus(numero_bus, horario)
                    pass
                case 4:
                    nombre = input("Nombre del conductor: ")
                    horario = input("Horario del conductor (hora): ")
                    Admin.agregar_conductor(nombre, horario)
                    pass
                case 5:
                    nombre = input("Nombre del conductor: ")
                    horario = input("Nuevo horario del conductor (hora): ")
                    Admin.agregar_horario_a_conductor(nombre, horario)
                    pass
                case 6:
                    nombre_conductor = input("Nombre del conductor: ")
                    numero_bus = input("Número del bus: ")
                    Admin.asignar_bus_a_conductor(nombre_conductor, numero_bus)
                    pass
                case 7:
                    print("Saliendo del programa")
                    pass
                case 8:
                    print("Nos vemos")
                    break
                case _:
                    print("Ingrese una opción válida")