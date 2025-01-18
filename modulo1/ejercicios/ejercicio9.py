# pedir notas
nota1=float(input("ingrese la nota1: "))
nota2=float(input("ingrese la nota2: "))
nota3=float(input("ingrese la nota3: "))
nota4=float(input("ingrese la nota4: "))

promedio=(nota1+nota2+nota3+nota4)/4

if promedio >=10:
    print(f"aprobado:{promedio}")
else:
    print(f"reprobado:{promedio}")