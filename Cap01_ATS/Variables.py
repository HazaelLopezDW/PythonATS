# Veremos la creacion de variable en el lenguaje de programación Python

numero = 10 # Esta es una variable que tendra un valor de tipo entero
real_flotante = 10.10 # Esta es una variable de tiplo float o Double en Java  Jajajajajaja... esperono se enojen
cadenas = "Hola mundo, mi sufrido mundo" # Esta variable es de tipo texto "String"
booleanos = True # Esta es una variable de tipo boleano estas toman dos valores (verdadero -> 1,2,3) (falso -> 0)

print(f"El valor de la variable es: {type(numero)} -> {numero}")
print(f"El valor de la variable es: {type(real_flotante)} -> {real_flotante}")
print(f"El valor de la variable es: {type(cadenas)} -> {cadenas}")
print(f"El valor de la variable es: {type(booleanos)} -> {booleanos} \n")

# Tipado dinamico de Python
numeroUno = "Esto es un numero"
print(f"El valor de la variable numeroUno es: {type(numeroUno)} Tipado Dinamico ->  {numeroUno}")
numeroUno = 20.1
print(f"El valor de la variable numeroUno es: {type(numeroUno)} Tipado Dinamico ->  {numeroUno}")
