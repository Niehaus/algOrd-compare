"""
@author: "Barbara Boechat"

@license: "GPL"
@email: "barbs.boechat@gmail.com"
@status: "PAA Assignment"
"""

import copy
import sys
import time
import csv
import os

from alg_ord import *
from timsort import tim_sort


def sort_with(ordenador, lista):
    if ordenador == 'insert':
        start = time.time()
        comp, lista_ordenada = insertion_sort(lista)
        end = time.time()
        # print(f'Insert - Num. de Comparações: {comp}; Tempo: {end - start}')
    elif ordenador == 'merge':
        start = time.time()
        comp, lista_ordenada = merge_sort(lista)
        end = time.time()
        # print(f'Merge - Num. de Comparações: {comp}; Tempo: {end - start}')
    else:
        start = time.time()
        comp, lista_ordenada = tim_sort(lista)
        end = time.time()
        # print(f'Tim - Num. de Comparações: {comp}; Tempo: {end - start}')

    return lista_ordenada, comp, end - start


if __name__ == '__main__':

    f = open(sys.argv[1], "r")
    numbers = f.read().split('\n')

    random_list = []
    for number in range(0, len(numbers) - 1):
        random_list.append(int(numbers[number]))

    results_file = 'resultados/results.csv'
    file_here = os.path.isfile(results_file)
    csv_file = open(results_file, 'a', newline='', encoding='utf8')
    csv_writer = csv.writer(csv_file)

    headers = ['algoritmo', 'entrada', 'n', 'comp', 'time']
    if not file_here:
        csv_writer.writerow(headers)

    algoritmos = ['insert', 'merge', 'tim']
    for algoritmo in algoritmos:

        ord_random, comp_random, time_random = sort_with(
            algoritmo,
            lista=copy.deepcopy(random_list)
        )
        row = [algoritmo, 'random', len(random_list),
               comp_random, time_random]
        csv_writer.writerow(row)
        
        ord_asc, comp_asc, time_asc = sort_with(
            algoritmo,
            lista=copy.deepcopy(ord_random)
        )
        row = [algoritmo, 'asc', len(random_list),
               comp_asc, time_asc]
        csv_writer.writerow(row)

        ord_desc, comp_desc, time_desc = sort_with(
            algoritmo,
            lista=copy.deepcopy(ord_asc[::-1])
        )
        row = [algoritmo, 'desc', len(random_list),
               comp_desc, time_desc]
        csv_writer.writerow(row)

