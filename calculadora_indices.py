''' 
Calcula el índice de masa corporal de una persona a partir de la ecuación
definida anteriormente.
'''


def calcular_IMC(peso: float, altura: float) -> float:
    return round(peso/(altura**2), 2)


'''
Calcula el porcentaje de grasa de una persona a partir de la ecuación
definida anteriormente.
'''


def calcular_porcentaje_grasa(peso: float, altura: float, edad: int, valor_genero: float) -> float:
    imc = calcular_IMC(peso, altura)
    return round((1.2*imc)+(0.23*edad)-5.4-valor_genero, 2)


'''
Calcula la cantidad de calorías que una persona quema estando en reposo
(esto es, su tasa metabólica basal), a partir de la ecuación definida
anteriormente.
'''


def calcular_calorias_en_reposo(peso: float, altura: float, edad: int, valor_genero: int) -> float:
    heightCentimeters = altura*100
    return (10*peso)+(6.25*heightCentimeters)-(5*edad)+valor_genero


'''
Calcula la cantidad de calorías que una persona quema al realizar algún tipo
de actividad física (esto es, su tasa metabólica basal según actividad física),
a partir de la ecuación definida anteriormente.
'''


def calcular_calorias_en_actividad(peso: float, altura: float, edad: int, valor_genero: float, valor_actividad: float) -> float:
    tmb = calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    return tmb*valor_actividad


'''
Calcula el rango de calorías recomendado, que debe consumir una persona
diariamente en caso de que desee adelgazar, a partir de la ecuación
definida anteriormente.
'''


def consumo_calorias_recomendado_para_adelgazar(peso: float, altura: float, edad: int, valor_genero: float) -> str:
    tmb = calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    suggestedCaloriesGrant = round(tmb-(tmb*0.15), 2)
    suggestedCaloriesLess = round(tmb-(tmb*0.2), 2)
    return 'Para adelgazar es recomendado consumas entre: '+str(suggestedCaloriesLess)+' y '+str(suggestedCaloriesGrant)+' calorías al día.'
