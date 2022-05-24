# Pedir números enteros en un ciclo mientras sean positivos 

Numero_ciclo = float(input('Escriba los numeros de la lista: '))

Suma=0
Contador=0

while Numero_ciclo >= 0:
    Suma += Numero_ciclo
    Contador += 1
    Promedio = Suma/Contador
    Numero_ciclo= int(input("Escriba otro numero positivo  "))
else:
    print(f'Al introducir un numero negativo se cierra el programa')

# print(f'La suma de los numeros introducidos es { Suma } .' ) 
# print(f'El conteo de los numeros introducidos es { Contador } .' ) 
print(f'El promedio de los numeros es  { Promedio } .' ) 

