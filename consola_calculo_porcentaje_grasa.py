import calculadora_indices as calc

kilogramers = float(input('Ingrese el peso de la persona (en Kilogramos): '))

height = float(input('Ingrese la altura de la persona (en metros): '))

age = int(input('Ingrese la edad de la persona (en años): '))

genreValue = float(
    input('Ingrese el valor 5 en caso de ser hombre y -161 en caso de ser mujer: '))

print(str(calc.calcular_porcentaje_grasa(kilogramers, height, age, genreValue))+'%')
