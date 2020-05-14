# Condicionales Anidaddos en Python

'''
    Veremos los condicionales en python. Veremos el condicional anidados
    if codicional:
          if codicional:
            Sentencias a ejecutar, si condicion se cumple
        else:
            Sente a ejecutar, si condicion no se cumple
    else:
        Sente a ejecutar, si condicion no se cumple
'''

# Declaramos nuestras varible y pedimos al usuarios que ingrese su nombre y edad
nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))

# Condicional if
if 0 < edad < 100:
    if 0 < edad < 3:
        print("Primera infancia: ")
    elif 3 < edad < 10:
        print("Segunda infancia: ")
    elif 10 < edad < 15:
        print("Eres un adolecente:")
    elif 15 < edad < 17:
        print("Eres un Joven: ")
    else:
        print("Ya eres adulto: ")
else:
    print("La edad tiene que estar en el rango de 1 a 99:")