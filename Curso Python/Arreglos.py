# Arreglos / Lista: Conjuntos de valores de uno o mas tipos de datos
# Sintaxis
'''  nombre_del_arreglo = [elementos o valores]    '''

nombres= ['Alondra','Fernando','Ricardo','Eduardo']
# Indice(Index)= 0 ,1 ,2, 3
edades=[21,25,19,30]
arreglo_lista = [10,15.6,'Hola',True]

# OPERACIONES CON ARREGLOS

nombres[1] = " Fernando Arturo"
edades[0]= 20
arreglo_lista[3]= False
# MODIFICAR UN ELEMENTO DE UN ARREGLO
nombres.append("Veronica")
edades.append(25)
# Ordenar los elementos
edades.sort()
edades.reverse()

#SALIDA DE DATOS
print(nombres)
print(edades)
print(arreglo_lista)
