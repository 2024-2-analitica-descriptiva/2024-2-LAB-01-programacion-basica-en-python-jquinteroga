"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
Retorne la cantidad de registros por cada letra de la primera columna como
la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

Rta/
[('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]
"""
import glob
import fileinput
import re


def pregunta_02():

    files = glob.glob("files/input/*")

    """Mapper"""
    sequence = []
    with fileinput.input(files=files) as f:
        for fila in f:
            letter = re.match(r"^([A-Z])\t", fila) 
            sequence.append((letter.group(1),1))
        
    """Shuffle and sort"""
    sequence.sort()

    """Reducer"""
    diccionario = {}
    for key, value in sequence:
        if key in diccionario:
            diccionario[key] += value
        else:
            diccionario[key] = value

    return list(diccionario.items())

# print(pregunta_02())