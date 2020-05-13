# Operadores relacionales

'''
    Veremos los operadores relacionales en Python
    Los operadores relacionales tiene menos prioridad que los operadores Aritmeticos
    <   mayor que
    >   menor que
    <=  mayor o igual que
    >=  menor o igual que
    !=  distinto de
    =   asignacion
    ==  igualdad
'''

# Haremos un programa que pida al usuario dos numero y los compararemos

primerNumero = int(input("Ingrese el primer numero a comparar "))    # Primer entero introducido por el usuario
segundoNumero = int(input("Ingrese el segundo numero a comparar "))  # Segundo numero introducido por el usuario

# Hacemos nuestra compracion
if primerNumero == segundoNumero:
    print(f"{primerNumero} y {segundoNumero} son iguales")
if primerNumero > segundoNumero:
    print(f"{primerNumero} es mayor que {segundoNumero}")
if primerNumero >= segundoNumero:
    print(f"{primerNumero} es mayor o igual que {segundoNumero}")
if primerNumero < segundoNumero:
    print(f"{primerNumero} es menor que {segundoNumero}")
if primerNumero <= segundoNumero:
    print(f"{primerNumero} es menor o igual que {segundoNumero}")
if primerNumero != segundoNumero:
    print(f"{primerNumero} y {segundoNumero} son distintos")



