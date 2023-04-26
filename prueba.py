import random
import matplotlib.pyplot as plt

def lee_int():
    """
    Lee un número entero y determina si es par o impar.
    Par: escribe todos los pares de manera descendiente desde sí mismo y hasta el cero.
    Impar: escribe todos los impares de manera descendiente desde si sí mismo hasta el uno.
    """
    numero = int(input("Leer numero: "))
    if numero%2 == 0: # si es par el resto es 0
        print(f"El numero {numero} es par")
        for i in reversed(range(0, numero+1, 2)): print(i) # hacemos loop que vaya al reves de 0 al numero
    else: # impar
        print(f"El numero {numero} es impar")
        for i in reversed(range(1, numero+1, 2)): print(i) # hacemos loop que vaya al reves de 1 al numero


def clasificacion_personas():
    """
    Algoritmo que visualice una clasificación de 50 personas según edad y sexo. 
    
    mayor:          Cantidad de personas mayores de edad (18 años o más).
    menor:          Cantidad de personas menores de edad.
    h_mayor:        Cantidad de personas masculinas mayores de edad.
    m_menor:        Cantidad de personas femeninas menores de edad.
    p_mayor_total:  Porcentaje que representan las personas mayores de edad respecto al total de personas.
    p_m_total:      Porcentaje que representan las mujeres respecto al total de personas.
    """
    personas = leer_personas() # personas = [(sexo0, edad0), (sexo1, edad1), ..., (sexo49, edad49)]
    print(personas) 

    mayor, h_mayor, m_menor, p_mayor_total, mujer = 0, 0, 0, 0, 0
    for persona in personas: # chequeamos las condiciones
        if persona[1] >= 18: mayor += 1
        if persona[0] == "M": mujer += 1
        if (persona[0] == "H" and persona[1] >= 18): h_mayor += 1
        if (persona[0] == "M" and persona[1] < 18): m_menor += 1

    # calculamos lo que nos piden
    menor = 50 - mayor
    p_mayor_total = (mayor/50)*100
    p_m_total = (mujer/50)*100
    
    # lo representamos en un plot para visualizarlo 
    fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(8,7))

    axs[0,0].bar(["Mayor", "Menor", "H mayores", "M menores"], [mayor, menor, h_mayor, m_menor])
    axs[0,0].set_ylabel("# personas")
    axs[0,0].set_title("Clasificación de personas por edad y sexo")

    axs[0,1].set_title("Personas mayores vs menores")
    axs[0,1].pie([p_mayor_total, (100-p_mayor_total)], labels = ["Mayor (%)", "Menor (%)"])

    axs[1,0].set_title("Mujeres vs hombres")
    axs[1,0].pie([p_m_total, (100-p_m_total)], labels = ["Mujeres (%)", "Hombres (%)"])
    
    plt.show() 
  
def leer_personas():
    """
    Cargar los datos de las 50 personas en un variable
    """
    sexo = random.choices(["H","M"], k=50)  # lista de 50 random H: hombre o M: mujer
    edad = random.sample(range(0, 101), 50) # lista de 50 random de la edad de las personas
    return list(zip(sexo, edad)) # lista de 50 tuples


def calcula_salario():
    """
    Cálculo del salario de un trabajador. Calcular el sueldo recibido por el trabajador en base las horas trabajadas y la tarifa. 
    """
    horas_trabajadas = float(input("Leer horas trabajadas: ")) # horas trabajadas
    tarifa = float(input("Leer tarifa: ")) # precio por hora

    salario = tarifa*horas_trabajadas # calculamos salario total
    h_extra = 0
    if horas_trabajadas > 40: # si mayor a 40 h
        h_extra = horas_trabajadas - 40 # conseguimos las h extra
        salario -= h_extra*tarifa # le quitamos las horas extras al salario
        salario = salario + tarifa*2*h_extra # para volver a sumarselas pero con el doble de la tarifa
    
    print(f"El salario que cobraría sería de {salario}€, trabajando {horas_trabajadas}h.")
    if h_extra != 0: print(f"Con {h_extra}h extra.")


choose = int(input("""Qué desea hacer:

                1 - Lee un número entero y determina si es par o impar.
                2 - Visualizar una clasificación de 50 personas según edad y sexo. 
                3 - Cálculo del salario de un trabajador.

                >> """))

if choose == 1: lee_int()
elif choose == 2: clasificacion_personas()
else: calcula_salario()