# Algoritmos de ordenação -> MergeSort // InsertionSort
import sys

comp_tim = 0
run_size = 32


def busca_binaria(lista, item, inicio, final):
    global comp_tim
    if inicio == final:
        comp_tim += 1
        if lista[inicio] > item:
            return inicio
        else:
            return inicio + 1
    if inicio > final:
        return inicio

    meio = round((inicio + final) / 2)

    comp_tim += 1
    if lista[meio] < item:
        return busca_binaria(lista, item, meio + 1, final)
    elif lista[meio] > item:
        return busca_binaria(lista, item, inicio, meio - 1)
    else:
        return meio


def optimized_insert(lista):
    for i in range(1, len(lista)):
        item_atual = lista[i]
        pos = busca_binaria(lista, item_atual, 0, i - 1)
        lista = lista[:pos] + [item_atual] + lista[pos:i] + lista[i + 1:]
    return lista


def max_size_of_run(n):
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


def merge_me(lista, esq, meio, dir):
    global comp_tim
    # print('lista aqui', lista)
    esquerda = lista[esq: meio + 1]
    direita = lista[meio + 1: dir + 1]

    # print(esquerda, direita)
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


def merge(left, right):
    """Takes two sorted lists and returns a single sorted list by comparing the
    elements one at a time.
    [1, 2, 3, 4, 5, 6]
    """
    if not left:
        # print(right)
        return right
    if not right:
        # print(left)
        return left
    if left[0] < right[0]:
        # print([left[0]] + merge(left[1:], right))
        return [left[0]] + merge(left[1:], right)
    # print([right[0]] + merge(left, right[1:]))
    return [right[0]] + merge(left, right[1:])


def tim_sort(lista):
    global comp_tim
    length = len(lista)
    sys.setrecursionlimit(max(sys.getrecursionlimit(), length))

    esq_run = []
    dir_run = []

    # run_max_size = max_size_of_run(length)
    run_max_size = 32
    new_run = [lista[0]]
    runs = []
    sorted_array = []
    # for inicio in range(0, length, run_max_size):  # Ordena lista de RUN(32) em RUN(32)
    #     final = min(inicio + run_max_size, length)
    #     mid_run = round((inicio + final) / 2)
    #     for i in range(inicio, final):
    #         if lista[i] >= lista[mid_run]:
    #             dir_run.append(lista[i])
    #         else:
    #             esq_run.append(lista[i])
    #     print(esq_run + dir_run)
    #     sorted_array += optimized_insert(esq_run + dir_run)
    #     esq_run = []
    #     dir_run = []

    # for every i in the range of 1 to length of array
    # for i in range(1, length):
    #     # if i is at the end of the list
    #     if i == length - 1:
    #         new_run.append(lista[i])
    #         runs.append(new_run)
    #         break
    #     # if the i'th element of the array is less than the one before it
    #     if lista[i] < lista[i - 1]:
    #         # if new_run is set to None (NULL)
    #         if not new_run:
    #             runs.append([lista[i]])
    #             new_run.append(lista[i])
    #         else:
    #             runs.append(new_run)
    #             new_run = []
    #             i -= 1
    #     # else if its equal to or more than
    #     else:
    #         new_run.append(lista[i])
    print('minrun size', run_max_size)
    i = 1
    while i != length:
        if i == length - 1:
            new_run.append(lista[i])
            runs.append(new_run)
            break
        # if the i'th element of the array is less than the one before it
        if lista[i] < lista[i - 1]:
            # if new_run is set to None (NULL)
            if not new_run:
                runs.append([lista[i]])
                new_run.append(lista[i])
            else:
                runs.append(new_run)
                new_run = [lista[i]]
                # i -= 1
        # else if its equal to or more than
        else:
            if len(new_run) < run_max_size:
                new_run.append(lista[i])
            else:
                runs.append(new_run)
                new_run = [lista[i]]
        i += 1

    print(len(runs))
    # for every run in sorted_runs, merge them
    for run in runs:
        print(sorted_array)
        sorted_array = merge(sorted_array, optimized_insert(run))
    # print(runs)
    # print(max(runs))
    # max_len = max([len(i) for i in runs])
    # print(max_len)
    # print(merge(runs[0], runs[1]))

    # for run in runs:
    #     sorted_array += optimized_insert(run)
    #
    # merge_size = run_max_size
    # while merge_size < length:
    #     for esquerda in range(0, length, 2 * merge_size):
    #         meio = min(length - 1, esquerda + merge_size - 1)
    #         direita = min((esquerda + 2 * merge_size - 1), (length - 1))
    #         merge_me(sorted_array, esquerda, meio, direita)
    #     merge_size *= 2
    #

    return comp_tim, sorted_array

#
tim_sort(
    lista=[28, 32, 27, 5, 100, 35, 81, 100, 99, 91, 62, 4, 53, 70, 91, 43, 66, 24, 3, 73, 37, 5, 65, 95, 95, 46, 38,
           12, 53, 35, 0, 55, 19, 21, 3, 88, 15, 72, 19, 88, 24, 60, 7, 1, 90, 80, 10, 48, 68, 70, 55, 17, 95, 0,
           83, 34, 51, 9, 58, 80, 63, 1, 50, 20]
)

# tim_sort(lista=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
# 61, 62, 63]
# )
