"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.

    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]
"""


import glob
import fileinput

def pregunta_06():
    files = glob.glob("files/input/*")

    sequence = []

    with fileinput.input(files=files) as f:
        for line in f:
            line = (line.strip().split("\t"))
            sequence.append(line[4].split(","))
    
    dic_original = []

    for lista in sequence:
        for letras in lista:
            letras = letras.split(":")
            dic_original.append(letras)

    dic_original.sort()

    diccionario = {}
    for key , value in dic_original:
        value = int(value)
        if key not in diccionario:
            diccionario[key] = [value]
        else:
            diccionario[key].append(value)

    resultado = []

    for key , value in diccionario.items():
        minimo = min(value)
        maximo = max(value)
        resultado.append((key,minimo,maximo))

    return resultado

print (pregunta_06())