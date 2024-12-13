"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}
"""

import glob
import fileinput

def pregunta_11():
    files = glob.glob("files/input/*")

    sequence = []
    with fileinput.input(files=files) as f:
        for line in f:
            line = line.strip().split("\t")
            sequence.append((line[3].split(","),int(line[1])))

    sequence.sort()

    diccionario = {}
    for tupla in sequence:
        letras = tupla[0]
        valor = tupla[1]
        for letra in letras:
            if letra not in diccionario:
                diccionario[letra] = valor
            else:
                diccionario[letra] += valor

    return diccionario

print (pregunta_11())