import calculadora_indices as calc

kilogramers = float(input('Ingrese el peso de la persona (en Kilogramos): '))

height = float(input('Ingrese la altura de la persona (en centimetros): '))/100

age = int(input('Ingrese la edad de la persona (en años): '))

genreValue = float(
    input('Ingrese el valor 5 en caso de ser hombre y -161 en caso de ser mujer: '))

print(calc.consumo_calorias_recomendado_para_adelgazar(
    kilogramers, height, age, genreValue))
