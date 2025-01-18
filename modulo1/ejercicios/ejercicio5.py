import sys
# entrada 
#variable = float(input("Introducir un numero"))
#print(type(variable))
### entrada por argumentos

variables=sys.argv
print(variables)
### salidas  || print()

#1. concatenando valores
nombre="gianmarco"
apellido="gutierrez"
curso="python"

print("Iniciamos el curso"+" "+curso+" "+":"+nombre+" "+apellido)
#mejora

print("Iniciamos el curso",curso,":",nombre,apellido)
# 2.
print(f"Iniciamos el curso {curso} : {nombre} {apellido}")
print("Iniciamos el curso {} : {} {}".format(curso,nombre,apellido))