"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}
"""

import glob
import fileinput

def pregunta_12():
    files = glob.glob("files/input/*")

    sequence = []
    with fileinput.input(files=files) as f:
        for line in f:
            line = line.strip().split("\t")
            column1 = line[0] 
            column5 = line[4]  
            
            values = [int(pair.split(":")[1]) for pair in column5.split(",")]
            
            sequence.append((column1, sum(values)))

    sequence.sort()
    # Generar el diccionario sumando por cada clave de la columna 1
    diccionario = {}
    for key, value in sequence:
        if key not in diccionario:
            diccionario[key] = value
        else:
            diccionario[key] += value

    return diccionario

print(pregunta_12())
