import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


if __name__ == '__main__':
    df = pd.read_csv('results.csv')

    tam_entradas = sorted(df['n'].unique())
    tipo_entradas = df['entrada'].unique()

    # df[(df['algoritmo'] == 'insert') & (df['entrada'] == 'random')]

    insert_df = df[(df['algoritmo'] == 'insert')]
    merge_df = df[(df['algoritmo'] == 'merge')]
    tim_df = df[(df['algoritmo'] == 'tim')]

    comp_random = []
    time_random = []

    comp_asc = []
    time_asc = []

    comp_desc = []
    time_desc = []

    for n in tam_entradas:
        for tipo in tipo_entradas:
            new_df = insert_df[
                        (insert_df['entrada'] == tipo) &
                        (insert_df['n'] == n)
                    ]

            if tipo == 'asc':
                comp_asc.append(np.mean(new_df['comp']))
                time_asc.append(np.mean(new_df['time']))
            elif tipo == 'desc':
                comp_desc.append(np.mean(new_df['comp']))
                time_desc.append(np.mean(new_df['time']))
            else:
                comp_random.append(np.mean(new_df['comp']))
                time_random.append(np.mean(new_df['time']))

            # print(n, tipo)
            # print(np.mean(new_df['comp']), np.mean(new_df['time']), '\n')
    # print(comp_random, time_random)
    print(tam_entradas)

    plt.plot(tam_entradas, comp_random, marker='o', label="Random")
    plt.plot(tam_entradas, comp_asc, marker='o', label="Asc")
    plt.plot(tam_entradas, comp_desc, alpha=0.5, marker='o', label="Desc")
    plt.xticks(tam_entradas, tam_entradas)
    # plt.tight_layout()
    plt.tick_params(axis='x', which='major', labelsize=8.5)
    plt.grid()

    plt.legend()
    plt.show()

    # insert_random = insert_df[(insert_df['entrada'] == 'random') & (insert_df['n'] == 32)]
    # print(insert_random)