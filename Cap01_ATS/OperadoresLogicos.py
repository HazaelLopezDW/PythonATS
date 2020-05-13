'''
    operadores logicos
    operador And es una multiplicacion logica
    operador Or es una suma logica
    Operador Not falso = verdadero y verdadero = falso

    Prioridad
    1- Not
    2- And
    3- OR
'''

# simplemente mostraremos su tabla de la verdad

mensaje = "TABLAS DE LA VERDADES\n\n"
verdadero = True
falso = False

mensaje += "TABLA DE LA VERDAD DEL OPERADOR LOGICO AND\n"
mensaje += f"True and True -> {verdadero and  verdadero} \n"
mensaje += f"True and False -> {verdadero and  falso} \n"
mensaje += f"False and True -> {falso and  verdadero} \n"
mensaje += f"False and False -> {falso and  falso} \n\n"

mensaje += "TABLA DE LA VERDAD DEL OPERADOR LOGICO OR\n"
mensaje += f"True and True -> {verdadero or  verdadero} \n"
mensaje += f"True and False -> {verdadero or  falso} \n"
mensaje += f"False and True -> {falso or  verdadero} \n"
mensaje += f"False and False -> {falso or  falso} \n\n"

mensaje += "TABLA DE LA VERDAD DEL OPERADOR LOGICO NOT\n"
mensaje += f"not True -> {not verdadero} \n"
mensaje += f"not False -> {not falso}"

print(mensaje)





















