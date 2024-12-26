from typing import List

"""
El problema del índice H (H-index) es un problema común en bibliometría que mide la productividad y el impacto de las publicaciones de un investigador.

Definición del índice H:
El índice H de un investigador es el número máximo H tal que el investigador tiene al menos H publicaciones que han sido citadas al menos H veces cada una.

Por ejemplo, si un investigador tiene las siguientes citas para sus publicaciones:
    [3, 0, 6, 1, 5]

El índice H sería 3, porque el investigador tiene 3 publicaciones que han sido citadas al menos 3 veces cada una.

Objetivo:
Escribir una función que reciba una lista de enteros (citations) donde cada entero representa el número de citas de una publicación, y devuelva el índice H del investigador.

Soluciones:
1. Fuerza Bruta: Iterar sobre todos los posibles valores de H y verificar cuántas publicaciones cumplen con la condición.
2. Optimizada: Ordenar la lista de citas y encontrar el índice H de manera más directa.
"""


def h_index(citations: List[int]) -> int:
    citations.sort()
    n = len(citations)
    for i, c in enumerate(citations):
        if c >= n - i:
            return n - i
    return 0
