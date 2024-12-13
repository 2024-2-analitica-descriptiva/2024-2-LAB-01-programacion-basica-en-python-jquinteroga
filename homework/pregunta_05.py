"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]
"""

import glob
import fileinput

def pregunta_05():
    files = glob.glob("files/input/*")

    sequence = []
    with fileinput.input(files=files) as f:
        for line in f:
            line = line.strip().split("\t")
            sequence.append((line[0],line[1]))

    sequence.sort()


    diccionario = {}
    for key,value in sequence:
        if key not in diccionario:
            diccionario[key] = {'max': value, 'min': value}
        else:
            if value > diccionario[key]['max']:
                diccionario[key]['max'] = value
            elif value < diccionario[key]['min']:
                diccionario[key]['min'] = value

    resultado = [(key, int(value['max']), int(value['min'])) for key, value in diccionario.items()]

    return resultado




# def maximo_minimo_por_letra(registros):

#     agrupados = {}

#     # Agrupar valores de la columna 2 por letra de la columna 1
#     for registro in registros:
#         letra = registro[0]
#         valor = int(registro[1])

#         if letra in agrupados:
#             agrupados[letra].append(valor)
#         else:
#             agrupados[letra] = [valor]

#     # Calcular el máximo y mínimo por letra
#     resultado = []
#     for letra, valores in agrupados.items():
#         maximo = max(valores)
#         minimo = min(valores)
#         resultado.append((letra, maximo, minimo))

#     return resultado


# # Ejemplo de datos
# datos = [
#     ["A", "9"],
#     ["B", "1"],
#     ["A", "2"],
#     ["B", "9"],
#     ["C", "0"],
#     ["C", "9"],
#     ["D", "3"],
#     ["D", "8"],
#     ["E", "9"],
#     ["E", "1"],
# ]

# # Llamar a la función
# resultado = maximo_minimo_por_letra(datos)

# # Imprimir el resultado
# print("Rta/")
# print(resultado)
