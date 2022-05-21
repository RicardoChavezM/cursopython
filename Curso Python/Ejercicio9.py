# Calcular la nomina


# Entradas de datos
print('Para calcular la Nomina se necesitara que introduzcas los datos siguientes: ')
Mes= input('Escribe el mes actual:  ')
Dias_laborales =float(input('Escribe los dias laborales:  ')) 
Pago_por_dia=float(input('Escriba el pago por dia :  ')) 

# Proceso de datos
Pago_Base = Dias_laborales*Pago_por_dia
Iva_tras=Pago_Base*0.16
Sub_total= Iva_tras + Pago_Base
Iva_retenido = 2/3*Iva_tras
Isr_retenido = 0.1*Pago_Base
Pago_Neto= Sub_total-Iva_retenido-Isr_retenido


# Salidas de datos
print(f'El Pago base es = { Pago_Base }')
print(f'El Iva trasladado es = { Iva_tras }')
print(f'El Sub total es = { Sub_total }')
print(f'El Iva retenido es = { Iva_retenido }')
print(f'El Isr retenido es = { Isr_retenido }')
print(f'El Pago de la nomina  es = { Pago_Neto }')








