# Entradas de datos
Nivel_Agua = float(input('Escriba el nivel de agua de su cisterna: '))


# Salidas de datos
if Nivel_Agua > 6:
    print ('Desbordamiento de Agua en Cisterna ')
elif Nivel_Agua == 6:
        print ('Apagar Bomba')
elif Nivel_Agua < 6 and Nivel_Agua > 4: 
    print ('Desacelerar Bomba')
elif Nivel_Agua < 4 and Nivel_Agua > 2: 
    print ('Bomba Trabajando')
elif Nivel_Agua < 2 and Nivel_Agua > 0: 
    print ('Acelerar bomba de agua')
elif Nivel_Agua == 0 :
    print ('Encender Bomba de Agua')
elif Nivel_Agua < 0 :
    print ('Fuga de Cisterna')

