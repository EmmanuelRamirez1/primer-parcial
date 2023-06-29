# 3. Escribe un programa que calcule la equivalencia a pesos de los dólares ingresados por pantalla. El 
# programa debe preguntar el tipo de cambio a convertir (es decir, cuánto cotiza el dólar).

cotizacion = float(input("Ingrese la cotización del dólar: "))
dolares = float(input("Ingrese la cantidad de dólares a convertir: "))
pesos = dolares * cotizacion
print("dolares dólares equivalen a ",str(pesos)," pesos.")