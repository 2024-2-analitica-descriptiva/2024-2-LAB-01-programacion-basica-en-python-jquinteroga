"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
Retorne la suma de la segunda columna.
Rta/
214
"""

import glob
import fileinput


def pregunta_01():

    sequences = []
    suma = 0

    files = glob.glob("files/input/*")
    
    with fileinput.input(files=files) as f:
        for line in f:
            line = line.strip().split("\t")
            sequences.append(line)
    
    for line in sequences:
        value = int(line[1])
        suma += value

    return suma


# print(pregunta_01())