import calculadora_indices as calc

kilogramers = float(input('Ingrese el peso de la persona (en Kilogramos): '))

height = float(input('Ingrese la altura de la persona (en centimetros): '))/100

age = int(input('Ingrese la edad de la persona (en años): '))

genreValue = float(
    input('Ingrese el valor 5 en caso de ser hombre y -161 en caso de ser mujer: '))

activityValue = float(input('Ingrese valor de actividad física 1.2: Poco o ningún ejercicio, 1.375: ejercicio ligero (1 a 3 días a la semana), 1.55: ejercicio moderado (3 a 5 días a la semana), 1.72: deportista (6-7 días a la semana), 1.9: atleta (entrenamientos mañana y tarde) '))

print(str(round(calc.calcular_calorias_en_actividad(
    kilogramers, height, age, genreValue, activityValue), 2))+' calc')
