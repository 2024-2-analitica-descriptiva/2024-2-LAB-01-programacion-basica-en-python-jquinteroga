"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}
"""

import glob
import fileinput

def pregunta_09():
    files = glob.glob("files/input/*")

    sequence = []
    with fileinput.input(files=files) as f:
        for line in f:
            line = line.strip().split("\t")
            sequence.append(line[4])

    sequence = [aux.split(",") for aux in sequence]
    sequence = [aux2.split(":") for aux in sequence for aux2 in aux]
    sequence.sort()

    diccionario = {}
    for key , _ in sequence:
        if key not in diccionario:
            diccionario[key] = 1
        else:
            diccionario[key] += 1


    return diccionario
print (pregunta_09())