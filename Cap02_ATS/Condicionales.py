# Condicionales en Python

'''
    Veremos los condicionales en python. Veremos el condicional
    if codicional:
        Sentencias a ejecutar, si condicion se cumple
    else:
        Sente a ejecutar, si condicion no se cumple
'''

# Declaramos nuestras varible y pedimos al usuarios que ingrese su nombre y edad
nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))

# Condicional if
if 0 < edad < 100:
    if edad >= 18:
        print(f"Hola {nombre} Eres mayor de edad: ")
    else:
        print("Aún eres menor de edad: ")
else:
    print("La edad tiene que estar en el rango de 1 a 99:")