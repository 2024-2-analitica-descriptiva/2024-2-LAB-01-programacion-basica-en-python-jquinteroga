"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]
"""

import glob
import fileinput

def pregunta_10():
    files = glob.glob("files/input/*")

    sequence = []
    with fileinput.input(files=files) as f:
        for line in f:
            line = line.strip().split("\t")
            col_5 = line[4].split(",")
            col_4 = line[3].split(",")
            sequence.append((line[0],len(col_4),len(col_5)))
    
    return sequence

print (pregunta_10())
