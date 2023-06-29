# 11. Escribe un programa que muestre los números del 1 al 10. Además, el programa debe mostrar:
# a. Si es número es par o impar.
# b. Cuanto es la suma total de todos los números mostrados.
# c. Cuanto es la suma total de todos los números pares mostrados.
# d. Cuanto es la suma total de todos los números impares mostrados.

numero = 1
suma_total = 0
suma_pares = 0
suma_impares = 0

while numero <= 10:
    print(numero)
    
    # Verificar si el número es par o impar
    if numero % 2 == 0:
        print("Es un número par.")
        suma_pares += numero
    else:
        print("Es un número impar.")
        suma_impares += numero
    
    # Calcular la suma total
    suma_total += numero
    
    numero += 1

print("La suma total es:", suma_total)
print("La suma de los números pares es:", suma_pares)
print("La suma de los números impares es:", suma_impares)