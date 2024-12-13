"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla
    contiene un valor posible de la columna 2 y una lista con todas las letras
    asociadas (columna 1) a dicho valor de la columna 2.

    Rta/
    [(0, ['C']),
     (1, ['E', 'B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E', 'E', 'D']),
     (4, ['E', 'B']),
     (5, ['B', 'C', 'D', 'D', 'E', 'E', 'E']),
     (6, ['C', 'E', 'A', 'B']),
     (7, ['A', 'C', 'E', 'D']),
     (8, ['E', 'D', 'E', 'A', 'B']),
     (9, ['A', 'B', 'E', 'A', 'A', 'C'])]
"""

import glob 
import fileinput

def pregunta_07():
    files = glob.glob("files/input/*")

    sequence = []
    with fileinput.input(files=files) as f:
        for line in f:
            line = line.strip().split("\t")
            sequence.append((int(line[1]),line[0]))

    diccionario = {}
    for key, value in sequence:
        if key not in diccionario:
            diccionario[key] = [value]
        else:
            diccionario[key].append(value)

    resultado = sorted(diccionario.items())

    return resultado

print(pregunta_07())