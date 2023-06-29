# 8. Escribe un programa solicite y muestre por pantalla el nombre, apellido y edad de 5 personas.

cont=1 
while (cont<=5):
     nombre = input("ingrese su nombre: ")
     apellido = input ("ingrese su apellido: ") 
     edad = input("ingrese su edad: ") 
     print("nombre: ",(nombre),",apellido:",(apellido),",edad:",str(edad))
     cont=cont+1 
     print(cont) 
else: 
     print("ya se cargaron 5 personas")