aciertos=0 #Para contar aciertos
print("Pregunta1 1. Herramienta de programación, parecido al lenguaje español utilizado para crear código:")
print('a-IDE')
print('b-Pseudocodigo')
print('c-Compilador')
print('d-ANSI/ISO')

Respuesta1=(input("Introduce tu respuesta "))

if(Respuesta1 == "b"):
    print(" Respuesta correcta ")
    aciertos= aciertos + 1
else: 
    print("Respuesta incorrecta")

print("Pregunta2  Conjunto de símbolos, letras, números, imágenes, audio y video organizadas y que son relevantes en un tiempo y forma determinados.")

print('a-Informacion')
print('b-Datos')
print('c-Programa')
print('d-Codigo')

Respuesta2=(input('Introduce tu respuesta '))

if(Respuesta2 == "a"):
    print(" Respuesta correcta ")
    aciertos= aciertos + 1
else: 
    print("Respuesta incorrecta")


print("Pregunta 3  Instituciones encargadas de estandarizar reglas y simbología de los Diagramas de Flujo.")

print('a-IEEE')
print('b-IDE')
print('c-ANSI/ISO')
print('d-VSCode')

Respuesta3=(input('Introduce tu respuesta '))

if(Respuesta3 == "c"):
    print(" Respuesta correcta ")
    aciertos= aciertos + 1
else: 
    print("Respuesta incorrecta")

print("Pregunta 4  Serie de pasos consecutivos, ordenados y finitos que se siguen para resolver un problema.")

print('a-Proceso')
print('b-Solucion')
print('c-Funcion')
print('d-Algoritmo')

Respuesta4=(input('Introduce tu respuesta '))

if(Respuesta4 == "d"):
    print(" Respuesta correcta ")
    aciertos= aciertos + 1
else: 
    print("Respuesta incorrecta")

print("Pregunta 5  Conjunto de elementos que se relacionan para cumplir una función determinada")

print('a-Estructura')
print('b-Datos')
print('c-Operacion')
print('d-Sistema')

Respuesta5=(input('Introduce tu respuesta '))

if(Respuesta5 == "d"):
    print(" Respuesta correcta ")
    aciertos= aciertos + 1
else: 
    print("Respuesta incorrecta")

print("Pregunta 6  Componente de un IDE que se encarga de traducir el código fuente a código máquina.")

print('a-Depurador')
print('b-Editor de Texto')
print('c-Terminal de Salida')
print('d-Compilador/Interprete')

Respuesta6 =(input('Introduce tu respuesta '))

if(Respuesta6 == "d"):
    print(" Respuesta correcta ")
    aciertos= aciertos + 1
else: 
    print("Respuesta incorrecta")

print("Pregunta 7   Elemento que se usa para almacenar una cantidad donde cambia su valor.")

print('a-Constante')
print('b-Variable')
print('c-Libreria')
print('d-Tipo de dato')

Respuesta7 =(input('Introduce tu respuesta '))

if(Respuesta7 == "b"):
    print(" Respuesta correcta ")
    aciertos= aciertos + 1
else: 
    print("Respuesta incorrecta")

print("Pregunta 8   Conjunto de símbolos, letras, números que no tienen un significado.")

print('a-Datos')
print('b-Estructura')
print('c-Informacion')
print('d-Sistema')

Respuesta8 =(input('Introduce tu respuesta '))

if(Respuesta8 == "a"):
    print(" Respuesta correcta ")
    aciertos= aciertos + 1
else: 
    print("Respuesta incorrecta")

print("Pregunta 9  Disciplina que argumenta conclusiones a partir de premisas mediante un razonamiento.")

print('a-Filosofia')
print('b-Sociologia')
print('c-Logica')
print('d-Argumentacion')

Respuesta9 =(input('Introduce tu respuesta '))

if(Respuesta9 == "c"):
    print(" Respuesta correcta ")
    aciertos= aciertos + 1
else: 
    print("Respuesta incorrecta")

print("Pregunta 10 Medida, patrón, modelo o norma universal para realizar una actividad o producir un objeto.")

print('a-Evento')
print('b-Estandar')
print('c-Calidad')
print('d-Productividad')

Respuesta10 =(input('Introduce tu respuesta '))

if(Respuesta10 == "b"):
    print(" Respuesta correcta ")
    aciertos= aciertos + 1
else: 
    print("Respuesta incorrecta")

print("Pregunta 11 Conjunto de elementos ordenados que componen y son la base de algo físico o no físico..")

print('a-Estructura')
print('b-Sistema')
print('c-Objeto')
print('d-Virtual')

Respuesta11 =(input('Introduce tu respuesta '))

if(Respuesta11 == "a"):
    print(" Respuesta correcta ")
    aciertos= aciertos + 1
else: 
    print("Respuesta incorrecta")


print("Pregunta 12 Conjunto de instrucciones (código) que indican a la computadora tareas a realizar.")

print('a-Operaciones/Calculos')
print('b-Sintaxis')
print('c-Programa de Computadora')
print('d-Comando')

Respuesta12 =(input('Introduce tu respuesta '))

if(Respuesta12 == "c"):
    print(" Respuesta correcta ")
    aciertos= aciertos + 1
else: 
    print("Respuesta incorrecta")

Promedio= (aciertos/12)*10

print (f'Tu total de aciertos fue = { aciertos  } ' )
print (f'Tu promedio en este examen fue = {Promedio}')
