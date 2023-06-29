# 1. Escribe un programa que calcule la edad que cumplió o debe cumplir este año la persona, basado en el año de nacimiento.

año = int (input("por favor ingrese su año de nancimiento: " )) 
año_actual = int (input("por favor ingrese su año actual: " ))

edad = año_actual - año 
print("en este año tienes:",(edad))