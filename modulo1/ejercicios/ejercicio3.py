## definir si una persona puede acceder a un credito
salario=float(input("ingrese su salario: "))
dependiente=input("es dependiente o independiente:(D/I) ")
factor_riesgo=float(input("Ingrese el factor de riesgo")) # FLOAT CONVIERTE EL VALOR EN FLOTANTE "32.5" => 32.5 | 32



valor_salario=salario>1500
valor_dependiente=dependiente.upper()=="D"
valor_factor_riesgo=factor_riesgo<0.5

# 
prestamo_aceptado=(valor_salario) and (valor_dependiente or valor_factor_riesgo)
print(prestamo_aceptado)