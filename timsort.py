# Algoritmos de ordenação -> MergeSort // InsertionSort
from alg_ord import merge_sort as merge

comp_tim = 0


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


def tim_sort(lista):
    global comp_tim
    length = len(lista)
    run_size = 32

    new_run = [lista[0]]
    runs, sorted_array = [], []

    i = 1
    while i != length:
        if i == length - 1:
            new_run.append(lista[i])
            runs.append(new_run)
            break
        if lista[i] < lista[i - 1]:  # verifica se o item i é parte ordenada ou não
            if not new_run:  # se uma new_run é None (NULL)
                runs.append([lista[i]])
                new_run.append(lista[i])
            else:
                runs.append(new_run)
                new_run = [lista[i]]
        else:  # se não for parte ordenada começa nova run
            if len(new_run) < run_size:
                new_run.append(lista[i])
            else:
                runs.append(new_run)
                new_run = [lista[i]]
        i += 1

    # transforma as mini runs em runs de tamanho minimo = 32
    new_run = []
    for run in runs:
        if len(new_run) < run_size:
            new_run += run
        else:
            sorted_array += optimized_insert(new_run)
            new_run = run
    sorted_array += optimized_insert(new_run)

    comp, lista = merge(sorted_array)
    comp_tim += comp

    return comp_tim, sorted_array
