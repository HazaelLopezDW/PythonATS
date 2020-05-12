# Operadores Aritmeticos

'''
    Vamos a hacer un programa sencillo en el cual pedieremos al usuario que nos ingrese dos numero enteros
    y luego haremos las operaciones aritmeticas elementales en el
'''

mensaje = "\nOPERACIONES ARITMETICA ELEMENTALES\n"
numeroUno = int(input("Ingrese el primer número entero a operar: "))
numeroDos = int(input("Ingrese el segundo número entero a operar: "))
resultado = 0.0

# Sumar (+)
resultado = numeroUno + numeroDos
mensaje += f"La suma de {numeroUno} + {numeroDos} es: {resultado}\n"

# Resta (-)
resultado = numeroUno - numeroDos
mensaje += f"La resta de {numeroUno} - {numeroDos} es: {resultado}\n"

# Multiplicación (*)
resultado = numeroUno * numeroDos
mensaje += f"La multiplicación de {numeroUno} * {numeroDos} es: {resultado}\n"

# Divición Fraccionaria (/)
resultado = numeroUno / numeroDos
mensaje += f"La divición fraccionaria de {numeroUno} / {numeroDos} es: {resultado}\n"

# Divición Fraccionaria (//)
resultado = numeroUno // numeroDos
mensaje += f"La dvición entera de {numeroUno} // {numeroDos} es: {resultado}\n"

# Operador Modulo (%) -> Este nos devuelve el residuo de una división
resultado = numeroUno % numeroDos
mensaje += f"Operador modulo de {numeroUno} % {numeroDos} es: {resultado}\n"

# Potenciación (**) -> Eleva el primerumero a la potencia del segundo
resultado = numeroUno ** numeroDos
mensaje += f"Operador modulo de {numeroUno} ** {numeroDos} es: {resultado}\n"

print(mensaje)