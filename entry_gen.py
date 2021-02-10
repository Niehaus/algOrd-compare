"""
    ## Gerador de Entradas ##
        - Valores Ordenados Decrescente
        - Valores Ordenado Crescente
        - Valores Aleatorios
        - Tam: 32 64 1024 10k 100k 1M
"""
import random


def gen_random(file, size):
    f = open(file, "w+")
    for _ in range(0, size):
        random_number = str(random.randint(0, 100))
        f.write(f'{random_number}\n')
    f.close()


def gen_ordered(order, size, file):
    f = open(file, "w+")
    if order == 2:
        for ordered_number in range(1, size + 1):
            f.write(f'{ordered_number}\n')
    else:
        for ordered_number in range(size, 0, -1):
            f.write(f'{ordered_number}\n')
    f.close()


def gen_entry(n_sizes, dirname, entry_type):
    for size in n_sizes:
        file_path = f'entradas/{dirname}'
        if entry_type == 1:
            for i in range(0, 10):
                file = file_path + f'n{size}/{size}_{i}.txt'
                gen_random(file, size)
        else:
            file = f'{file_path}/n{size}/{size}_0.txt'
            gen_ordered(entry_type, size, file)

    print(f'Entrys written to {dirname}/')


sizes = [32, 64, 1024, 10000, 100000, 1000000]
# params = {
#     'n_sizes': sizes,
#     'dirname': 'random',
#     'entry_type': 1
# }
# gen_entry(**params)

# params = {
#     'n_sizes': sizes,
#     'dirname': 'asc',
#     'entry_type': 2
# }
# gen_entry(**params)

params = {
    'n_sizes': sizes,
    'dirname': 'desc',
    'entry_type': 3
}
gen_entry(**params)
