# calcula el impuesto de una persona
# tasa =0.05 , si gana menos de 10k , sube cada 5k un porcentaje de 0.05

salario=float(input("ingrese el salario:"))
tasa=0.0
if salario<=10000:
    tasa=0.05
elif salario>10000 and salario<=15000:
    tasa=0.1
elif salario>15000 and salario<=20000:
    tasa=0.15
else:
    tasa=0.2
impuesto=salario*tasa
print(f"el impuesto de la persona es {impuesto}, ya que obtuvo una tasa de {tasa}")