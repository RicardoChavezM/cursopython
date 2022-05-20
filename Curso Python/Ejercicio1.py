
# Entradas de datos
Calificacion1 = float(input('Escribe tu primera calificacion:'))
Calificacion2 = float(input('Escribe tu segunda calificacion:'))
Calificacion3 = float(input('Escribe tu tercera calificacion:'))

# Proceso de datos
Promedio_Calificacion= (Calificacion1+Calificacion2+Calificacion3)/3


# Salidas de datos
print (f'Tu promedio es = { Promedio_Calificacion }')
if Promedio_Calificacion < 6:
    print ('Usted esta reprobado')
else:
        print ('Usted esta aprobado')


