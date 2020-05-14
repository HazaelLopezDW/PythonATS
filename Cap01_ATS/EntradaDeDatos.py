# Entradas de datos

'''
    Veremos las direntes formas de guardar datos ingresados por el usario
    las diferente formas de hacerlo
'''

mensaje = "\nENTRADA DE DATOS EN PYTHON\n"

nombre = input("Ingresa tu nombre: ") # Datos de tipo cadena str -> String
mensaje += f"Datos tipo cadena variable nombre -> {type(nombre)} = {nombre}\n"
entero = int(input("Ingresa tu edad: ")) # Datos de tipo entero int
mensaje += f"Datos tipo entero variable entero -> {type(entero)} = {entero}\n"
flotante = float(input("Ingresa un numero con punto decimal: ")) # Datos de tipo flotantes -> float
mensaje += f"Datos tipo entero variable entero -> {type(flotante)} = {flotante}\n"
booleano = bool(input("Ingresa True o False: ")) # Datos de tipo booleanos -> bool
mensaje += f"Datos tipo entero variable entero -> {type(booleano)} = {booleano}\n"

print(mensaje)

