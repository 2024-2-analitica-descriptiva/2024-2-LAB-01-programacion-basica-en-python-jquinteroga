"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
 Retorne la suma de la columna 2 por cada letra de la primera columna como
una lista de tuplas (letra, suma) ordendas alfabeticamente.
Rta/
[('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]
"""

import glob
import fileinput

def pregunta_03():

    files = glob.glob("files/input/*")

    tupla = []

    with fileinput.input(files=files) as f:

        sequence = []
        for line in f:
            line = line.strip().split("\t")
            sequence.append(line)
        
        for _, value in enumerate(sequence):
            tupla.append((value[0],int(value[1])))
    
    tupla.sort()

    diccionario = {}
    for key,value in tupla:
        if key in diccionario:  
            diccionario[key] += value
        else:
            diccionario[key] = value
    
    
    return list(diccionario.items())

print(pregunta_03())