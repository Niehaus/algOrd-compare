from alg_ord import *
import time
import os

if __name__ == '__main__':

    # files = ['random', 'asc', 'desc']
    files = ['teste']
    lista = []
    aux_lista = []
    for file in files:
        filepath = f'entradas/{file}'
        for dir_file in os.listdir(filepath):
            for arquivo in os.listdir(filepath + f'/{dir_file}'):
                f = open(filepath + f'/{dir_file}/{arquivo}', "r")
                numbers = f.read().split('\n')
                for number in range(0, len(numbers) - 1):
                    aux_lista.append(int(number))

                print('Arquivo=', arquivo)
                lista = aux_lista[:]
                start = time.time()
                comp_insert = insertion_sort(lista)
                end = time.time()
                print(f'Insert - Num. de Comparações: {comp_insert}; Tempo: {end - start}')

                lista = aux_lista[:]
                start = time.time()
                comp_merge = merge_sort(lista)
                end = time.time()
                print(f'Merge - Num. de Comparações: {comp_merge}; Tempo: {end - start}')

                lista = aux_lista[:]
                start = time.time()
                comp_tim = tim_sort(lista)
                end = time.time()
                print(f'Tim - Num. de Comparações: {comp_tim}; Tempo: {end - start}')
            print('\n')