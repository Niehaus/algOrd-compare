<h1 style="text-align:center">Análise de Métodos de Ordenação</h1>
<p style="text-align:center">
<span style="font-weight: bold">Bárbara Boechat</span><br>
Projeto e Análise de Algoritmos <br> Universidade Federal de São João del-Rei<br>
</p>

## 1. Introdução 

Neste trabalho serão realizadas comparações de desempenho entre os algoritmos
`MergeSort`, `InsertionSort` e `TimSort` considerando o tempo e o número de
comparações feitas para ordenar completamente os vetores.

## 2. Especificações

### 2.1 Organização das Entradas:

Toma um vetor aleatório como entrada e o ordena, em seguida este deve servir de
entrada como vetor ordenado acedente e descendente após ser invertido. 
10 arquivos por pasta. 

     ─┬─ "Entradas"
      └─┬─ "Dir": Num. Aleatorios  
        ├─── 32 Núm.
        ├─── 64 Núm.
        ├─── 1024 Núm.
        ├─── 10K Núm.
        ├─── 100K Núm.
        └─── 1M Núm.

## 3. Instruções 

Para rodar este trabalho será preciso executar o arquivo `runme.sh`, entao talvez seja necessário dar a ele permissões, para isso utilize o comando chmod `+x runme.sh`.

Para gerar os gráficos dos resultados gerados utilize `python resultados/analise_resultados.py`
