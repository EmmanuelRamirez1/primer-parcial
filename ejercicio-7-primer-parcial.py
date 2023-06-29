# 7. Del punto anterior, y considerando que durante 12 meses el empleado trabajó las mismas cantidades de 
# horas, escribe un programa que calcule el descuento anual a realizarse, considerando: 
# a. Si el sueldo anual es mayor a $2.000.000, el descuento es del %5.
# b. Si el sueldo anual esta entre $1.000.000 y $2.000.000, debe aplicarse un descuento del %3.
# c. Si el sueldo anual es menor a $1.000.000, debe aplicarse un descuento del %1. 
# d. El programa debe mostrar elsalario anual bruto, el monto anual de bonificaciones, el monto anual 
# a descontarse y las horas trabajadas en todo el año. 

horas_trabajadas_mensuales =120
sueldo_hora = 1500
sueldo_anual = horas_trabajadas_mensuales * sueldo_hora * 12

monto_bonificaciones = 0

if sueldo_anual > 2000000:
    descuento = sueldo_anual * 0.05
elif sueldo_anual >= 1000000:
    descuento = sueldo_anual * 0.03
else:
    descuento = sueldo_anual * 0.01

salario_bruto_anual = sueldo_anual + monto_bonificaciones
monto_a_descontar = descuento

print("Salario anual bruto:", salario_bruto_anual)
print("Monto anual de bonificaciones:", monto_bonificaciones)
print("Monto anual a descontar:", monto_a_descontar)
print("Horas trabajadas en el año:", horas_trabajadas_mensuales * 12)