"""
@author: "Barbara Boechat"

@license: "GPL"
@email: "barbs.boechat@gmail.com"
@status: "PAA Assignment"
"""

import time
import copy
import sys

from alg_ord import *
from timsort import tim_sort

if __name__ == '__main__':
    aux_lista = []
    f = open(sys.argv[1], "r")
    numbers = f.read().split('\n')
    for number in range(0, len(numbers) - 1):
        aux_lista.append(int(numbers[number]))
    start = time.time()
    comp_insert = insertion_sort(lista=copy.deepcopy(aux_lista))
    end = time.time()
    print(f'Insert - Num. de Comparações: {comp_insert}; Tempo: {end - start}')

    lista = copy.deepcopy(aux_lista)
    start = time.time()
    comp_merge = merge_sort(lista)
    end = time.time()
    print(f'Merge - Num. de Comparações: {comp_merge}; Tempo: {end - start}')

    start = time.time()
    comp_tim, my_list = tim_sort(lista=copy.deepcopy(aux_lista))
    end = time.time()
    print(f'Tim - Num. de Comparações: {comp_tim}; Tempo: {end - start}')
    print('\n')
