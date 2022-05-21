import math

# Entradas de datos
print('Para calcular la formula general se necesitara que introduzcas los valores a, b y c')
Valor_a= float(input('Escribe el valor de A :'))
Valor_b= float(input('Escribe el valor de B :'))
Valor_c= float(input('Escribe el valor de C :'))


# Proceso de datos
Formula_General1=(-(Valor_b)-pow((Valor_b*Valor_b) - 4*Valor_a*Valor_c,1/2)) / 2*Valor_a
Formula_General2=(-(Valor_b)+pow((Valor_b*Valor_b) - 4*Valor_a*Valor_c,1/2)) / 2*Valor_a


# Salidas de datos
print(f'El resultado de la Formula General 1 es = { Formula_General1 }')
print(f'El resultado de la Formula General 2 es = { Formula_General2 }')