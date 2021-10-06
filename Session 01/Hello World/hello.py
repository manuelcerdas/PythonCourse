print ("Bienvenido al primer ejemplo de Python")
nombre = input ("¿Cuál es su nombre?: ")
print (f"Hola {nombre} \n")
numero = input ("Por favor digite un número del 1 al 10: ")
numero = int (numero)
while (numero < 1 or numero > 10):
    print ("El numero tiene que estar entre 1 y 10\n")    
    numero = input ("Por favor digite un número del 1 al 10: ")
    numero = int (numero)

print (f"Voy a imprimir las tablas hasta la del {numero}")

for i in range (numero):
    for j in range(10):
        print (f"{i+1} * {j+1} = {(i + 1) * (j+1)}")
    





