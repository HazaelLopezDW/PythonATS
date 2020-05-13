# Operadores de Asignacion

'''
    Temos que los valores de asignacion son los siguientes
    += mas igual    -> Suma en asignacion
    -= menos igual  -> Resta en asignacion
    *= multiplica igual -> Multiplicación en signacion
    /= Division igual -> División en asignacion
    **= Potencia igual -> Potencia en asignacion
    %= Modulo igual -> Modulo en asignación
'''

# Pediremos al usuarios que ingrese un numero y haremos la respectiva operaciones de asignacion

numero = int(input("Ingresa el numero a operar. Por favor que este el rago de 1 a 10 "))
asignacion = 3

if numero >= 1 and numero <= 10:
    print("Hicimos las Operaciones De Asignacion con el numero tres")
    numero += asignacion
    print(f"La suma en asiganaciones es: {numero}")
    numero -= asignacion
    print(f"La resta en asiganaciones es: {numero}")
    numero *= asignacion
    print(f"La multiplicación en asiganaciones es: {numero}")
    numero /= asignacion
    print(f"La división en asiganaciones es: {numero}")
    numero %= asignacion
    print(f"La modulo en asiganaciones es: {numero}")
    numero **= asignacion
    print(f"La potencia en asiganaciones es: {numero}")
    numero //= asignacion
    print(f"La división entera en asiganaciones es: {numero}")
else:
    print("No seguistes la instrucciones")
