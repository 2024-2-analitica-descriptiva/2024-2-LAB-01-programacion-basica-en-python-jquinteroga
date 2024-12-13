"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]
"""

import glob
import fileinput

def pregunta_04():

    files = glob.glob("files/input/*")

    sequence = []
    fecha = []
    with fileinput.input(files=files) as f:
        for line in f:
            line = line.strip().split("\t")
            sequence.append(line[2].split("-"))
    
    for _, date in enumerate(sequence):
        fecha.append((date[1],1))
    
    fecha.sort()


    diccionario = {}
    for key, value in fecha:
        if key in diccionario:
            diccionario[key] += value
        else:
            diccionario[key] = value
    
    return list(diccionario.items())

print(pregunta_04())