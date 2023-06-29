g# 4. Escribe un programa que calcule el promedio final de una materia, basado en 3 notas de parciales, 
# indicando por pantalla si el alumno aprobó o debe recursar la materia (se aprueba con 6).

def promedio():
    nota1 = float(input("Ingrese la nota del primer parcial: "))
    nota2 = float(input("Ingrese la nota del segundo parcial: "))
    nota3 = float(input("Ingrese la nota del tercer parcial: "))
    promedio = (nota1 + nota2 + nota3) / 3
    if promedio >= 3:
        print("El alumno aprobó la materia promedio de", promedio)
    else:
        print("El alumno debe recursar la materia promedio de", promedio)

promedio()