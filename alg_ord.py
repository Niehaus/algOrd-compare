# Algoritmos de ordenação -> TimSort // MergeSort // InsertionSort

def tim_sort():
    ...


comp = 0


def merge_sort(lista):
    if len(lista) > 1:
        global comp
        metade = int(len(lista) / 2)
        direita = lista[:metade]
        esquerda = lista[metade:]

        merge_sort(esquerda)
        merge_sort(direita)

        k_esq = 0
        k_dir = 0
        k_global = 0

        while k_esq < len(esquerda) and k_dir < len(direita):
            if esquerda[k_esq] < direita[k_dir]:
                lista[k_global] = esquerda[k_esq]
                k_esq += 1
            else:
                lista[k_global] = direita[k_dir]
                k_dir += 1
            comp += 1
            k_global += 1

        while k_esq < len(esquerda):
            lista[k_global] = esquerda[k_esq]
            k_esq += 1
            k_global += 1

        while k_dir < len(direita):
            lista[k_global] = direita[k_dir]
            k_dir += 1
            k_global += 1
        return comp


def insertion_sort(lista):
    compare = 0
    for i in range(1, len(lista)):
        item_atual = lista[i]
        k = i
        while k > 0:
            if item_atual < lista[k - 1]:
                lista[k] = lista[k - 1]
                compare += 1
                k -= 1
            else:
                compare += 1
                break
        lista[k] = item_atual
    return compare
