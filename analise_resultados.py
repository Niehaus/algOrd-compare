import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def arrange_plot_vector(df_meth):
    comp_random = []
    time_random = []

    comp_asc = []
    time_asc = []

    comp_desc = []
    time_desc = []

    for n in tam_entradas:
        for tipo in tipo_entradas:
            new_df = df_meth[
                (df_meth['entrada'] == tipo) &
                (df_meth['n'] == n)
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

    data = {
        'comp_asc': comp_asc,
        'time_asc': time_asc,
        'comp_desc': comp_desc,
        'time_desc': time_desc,
        'comp_random': comp_random,
        'time_random': time_random
    }

    return data


def draw_graph(insert, merge, tim, title, ylabel):
    bx = ['32', '64', '1024', '10000', '100000', '1000000']

    x_locations = np.arange(len(bx))
    fig = plt.figure(figsize=(10, 5))
    width = 0.27

    ax = fig.add_subplot(111)
    ax.bar(x_locations, insert, width, color='lightcoral', log=True)
    ax.bar(x_locations + width, merge, width, color='gold', log=True)
    ax.bar(x_locations + width * 2, tim, width, color='paleturquoise', log=True)

    ax.set_xticks(x_locations + width)
    ax.set_xticklabels(bx)

    ax.legend(['Insert', 'Merge', 'Tim'])
    plt.xlabel("Tamanho da Entrada")
    plt.ylabel(ylabel)
    plt.title(title)

    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    df = pd.read_csv('results_teste.csv')

    tam_entradas = sorted(df['n'].unique())
    tipo_entradas = df['entrada'].unique()

    insert_df = df[(df['algoritmo'] == 'insert')]
    merge_df = df[(df['algoritmo'] == 'merge')]
    tim_df = df[(df['algoritmo'] == 'tim')]

    insert_data = arrange_plot_vector(insert_df)
    merge_data = arrange_plot_vector(merge_df)
    tim_data = arrange_plot_vector(tim_df)

    keys = list(tim_data.keys())

    titles = {
        'comp_asc': 'Qtd. de Comparações - Ascendente',
        'time_asc': 'Tempo de Execução - Ascendente',
        'comp_desc': 'Qtd. de Comparações - Descendente',
        'time_desc': 'Tempo de Execução - Descendente',
        'comp_random': 'Qtd. de Comparações - Random',
        'time_random': 'Tempo de Execução - Random'
    }

    yLabels = {
        'comp_asc': 'Nº de Comparações',
        'time_asc': 'Qtd. de Tempo',
        'comp_desc': 'Nº de Comparações',
        'time_desc': 'Qtd. de Tempo',
        'comp_random': 'Nº de Comparações',
        'time_random': 'Qtd. de Tempo'
    }

    for key in keys:
        draw_graph(
            insert_data[key], merge_data[key], tim_data[key],
            titles[key], yLabels[key]
        )
