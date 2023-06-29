# 12. Escribe un programa que permita ingresar las edades de las personas, hasta que el usuario decida no 
# hacerlo más, y muestre, al final, un promedio de las edades ingresadas y el total de personas ingresadas

estudiante= int(input("ingreses las edades: "))
suma_general=0
contador=0

while contador < estudiante:
    notas = float(input("el total de la personas ingresadas: ")) 
    suma_general += notas
    contador=contador+1

promedio = suma_general / estudiante 
print("promedio general es:",(promedio))

