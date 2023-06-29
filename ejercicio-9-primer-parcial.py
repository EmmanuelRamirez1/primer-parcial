# 9. Escribe un programa que solicite y muestre por pantalla nombre, apellido y edad de una cantidad de 
# personas ingresada por el usuario.

cantidad_personas =int(input("ingrese la cantidad de personas: "))
while(cantidad_personas>=1): 
    nombre=input("ingrese su nombre: ") 
    apellido=input("ingrese su apellido: ") 
    edad=input("ingrese su edad: ") 
    print("nombre: ", (nombre),",apellido:",(apellido),",edad: ",str(edad)) 
    cantidad_personas =cantidad_personas-1 
    
    print("nombre:",(nombre)) 
    print("apellido:",(apellido)) 
    print("edad:",(edad)) 
else: 
    print ("fin del programa")