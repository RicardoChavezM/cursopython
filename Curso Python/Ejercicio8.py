# Calcular numero ascendente y descendente

# Entradas de datos

print('Para calcular los numeros  se necesitara que introduzcas un numero cualquiera: ')
Numero1= int(input('Escribe el numero positivo o negativo '))

if Numero1< 0 and Numero1 > -100:
    for i in range(-1,-100,-2):
        print(f'{i}')
elif Numero1>0 and Numero1 < 100:
    for i in range (2,101,2):
        print(f'{i}')
else:
    print("Numero No Valido")       
