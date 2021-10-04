print ("Bienvenido al primer ejemplo de Python")
nombre = input ("¿Cuál es su nombre?: ")
print (f"Hola {nombre}")
print ("")
numero = input ("Por favor digite un número del 1 al 10: ")
numero = int (numero)
while (numero < 1 or numero > 10):
    print ("El numero tiene que estar entre 1 y 10")
    print ("")
    numero = input ("Por favor digite un número del 1 al 10: ")
    numero = int (numero)

print (f"Voy a imprimir las tablas del {numero} al 11")

