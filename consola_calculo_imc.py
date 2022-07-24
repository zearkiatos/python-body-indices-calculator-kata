import calculadora_indices as calc

kilogramers = float(input('Ingrese el peso de la persona (en Kilogramos): '))

height = float(input('Ingrese la altura de la persona (en metros): '))

print(calc.calcular_IMC(kilogramers, height))