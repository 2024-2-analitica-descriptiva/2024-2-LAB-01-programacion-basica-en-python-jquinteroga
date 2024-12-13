"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]
"""

import glob
import fileinput

def pregunta_08():
    files = glob.glob("files/input/*")

    sequence = []
    with fileinput.input(files=files) as f:
        for line in f:
            line = line.strip().split("\t")
            sequence.append((int(line[1]),line[0]))

    sequence.sort()
    
    diccionario = {}
    for key, value in sequence:
        if key not in diccionario:
            diccionario[key] = [value]
        elif value not in diccionario[key]:
            diccionario[key].append(value)
    
    resultado = sorted(diccionario.items())

    return resultado

print (pregunta_08())
