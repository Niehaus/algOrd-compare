# Algoritmos de ordenação -> MergeSort // InsertionSort

import copy

comp_tim = 0
run_size = 32


def merge(lista, esq, meio, dir):
    global comp_tim

    esquerda = lista[esq: meio + 1]
    direita = lista[meio + 1: dir + 1]

    i = 0  # Marcador do array da esquerda
    j = 0  # Marcador do array da direita
    k = esq

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            lista[k] = esquerda[i]
            i += 1
        else:
            lista[k] = direita[j]
            j += 1
        comp_tim += 1
        k += 1

    while i < len(esquerda):  # Copia lado esquerdo
        lista[k] = esquerda[i]
        k += 1
        i += 1

    while j < len(direita):  # Copia lado direito
        lista[k] = direita[j]
        k += 1
        j += 1

    return comp_tim


def insertion_sort(lista):
    global comp_tim

    for i in range(1, len(lista)):
        item_atual = lista[i]
        k = i
        while k > 0:
            comp_tim += 1
            if item_atual < lista[k - 1]:
                lista[k] = lista[k - 1]
                k -= 1
            else:
                break
        lista[k] = item_atual
    return lista


def min_run(n):
    """
    Define o tamanho minimo a ser divido
    uma run a partir do valor base 32.
    """
    global run_size

    r = 0
    while n >= run_size:
        r |= n & 1
        n >>= 1
    return n + r


def tim_sort(lista):
    global comp_tim

    tam_lista = len(lista)
    minrun_size = min_run(tam_lista)

    # Sort individual subarrays of size RUN
    aux_lista = []
    for inicio in range(0, tam_lista, minrun_size):  # Ordena lista de RUN(32) em RUN(32)
        final = min(inicio + minrun_size, tam_lista)
        aux_lista += insertion_sort(lista[inicio: final])
    lista = copy.deepcopy(aux_lista)

    merge_size = minrun_size
    while merge_size < tam_lista:
        for esquerda in range(0, tam_lista, 2 * merge_size):
            meio = min(tam_lista - 1, esquerda + merge_size - 1)
            direita = min((esquerda + 2 * merge_size - 1), (tam_lista - 1))
            merge(lista, esquerda, meio, direita)
        merge_size *= 2
    return comp_tim, lista
