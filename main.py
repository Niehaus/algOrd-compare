from timsort import tim_sort

if __name__ == '__main__':
    # files = ['random', 'asc', 'desc']
    # files = ['teste']
    # lista = []
    # aux_lista = []
    # for file in files:
    #     filepath = f'entradas/{file}'
    #     for dir_file in os.listdir(filepath):
    #         for arquivo in os.listdir(filepath + f'/{dir_file}'):
    #             f = open(filepath + f'/{dir_file}/{arquivo}', "r")
    #             numbers = f.read().split('\n')
    #             for number in range(0, len(numbers) - 1):
    #                 aux_lista.append(int(numbers[number]))
    #             print('Arquivo=', arquivo)
    #             #
    #             # start = time.time()
    #             # comp_insert = insertion_sort(lista=copy.deepcopy(aux_lista))
    #             # end = time.time()
    #             # print(f'Insert - Num. de Comparações: {comp_insert}; Tempo: {end - start}')
    #
    #             lista = copy.deepcopy(aux_lista)
    #             start = time.time()
    #             comp_merge = merge_sort(lista)
    #             end = time.time()
    #             print(f'Merge - Num. de Comparações: {comp_merge}; Tempo: {end - start}')
    #             print(lista)
    #             # start = time.time()
    #             # comp_tim = tim_sort(lista=copy.deepcopy(aux_lista))
    #             # end = time.time()
    #             # print(f'Tim - Num. de Comparações: {comp_tim}; Tempo: {end - start}')
    #             aux_lista = []
    #         print('\n')

    tim_sort(
        lista=[28, 32, 27, 5, 100, 35, 81, 100, 99, 91, 62, 4, 53, 70, 91, 43, 66, 24, 3, 73, 37, 5, 65, 95, 95, 46, 38,
               12, 53, 35, 0, 55, 19, 21, 3, 88, 15, 72, 19, 88, 24, 60, 7, 1, 90, 80, 10, 48, 68, 70, 55, 17, 95, 0,
               83, 34, 51, 9, 58, 80, 63, 1, 50, 20]
    )

