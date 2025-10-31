# CP3 - Dynamic Programming                 31/10/2025
# Tema:  Recursão com merge, quick sort e estruras LIFO e FIFO
# Professor: Francisco Elaino

def merge_sort(lista):
    """
        4. Análise o código abaixo para ordenar dados em uma lista e escreva as variáveis que estão faltando para o código funcionar
    """
    if len(lista) <= 1:
        return lista
    
    meio = len(lista) // 2
    esquerda = merge_sort(lista[:meio])
    direita = merge_sort(lista[meio:])

    resultado = []
    i = j = 0
    
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
    return resultado + esquerda[i:] + direita[j:]

lista = [9, 5, 3, 8, 4, 2, 1]
print("Lista ordenada:", merge_sort(lista))



def quick_sort(arr, depth=0):
    """
    6. Crie um algoritmo para ordenar as informações lista = [5, 30, 90, 10, 80, 40, 60, 50, 70] usando o quick sort
    """
    if len(arr) <= 1:
        return arr
    pivo = arr[-1]
    menores_pivo = [x for x in arr[:-1] if x <= pivo]
    maiores_pivo = [x for x in arr[:-1] if x > pivo]
    
    return quick_sort(menores_pivo, depth + 1) + [pivo] + quick_sort(maiores_pivo, depth + 1)

lista = [5, 30, 90, 10, 80, 40, 60, 50, 70]
print(quick_sort(lista))


# 3. Leia as afirmações a respeito da teoria sobre fila, pilha, quick e merge sort e marque apenas as afirmações corretas. (OBS: As respostas foram feitas no formulário)

# O Quick Sort é sempre mais rápido que o Merge Sort em qualquer tipo de entrada.

# O Merge Sort tem complexidade O(n log n) em todos os casos. 

# O Quick Sort, em média, tem complexidade O(n log n), mas no pior caso pode chegar a O(n²). 

# O Merge Sort é mais indicado para listas encadeadas do que o Quick Sort. 

# O Quick Sort precisa criar um vetor auxiliar para realizar as partições. 

# O Merge Sort é um algoritmo recursivo que divide o vetor ao meio até restar um único elemento. 

# O Quick Sort é estável, ou seja, mantém a ordem relativa dos elementos iguais. 

# O Merge Sort realiza a etapa de intercalação (merge) após resolver as sublistas recursivamente. 

# O Quick Sort geralmente é implementado de forma iterativa, pois é mais simples que a recursiva. 

# O Merge Sort é mais eficiente que o Quick Sort em conjuntos de dados muito grandes e armazenados em disco. 

# Tanto o Quick Sort quanto o Merge Sort têm comportamento determinístico e produzem sempre o mesmo número de comparações. 

# Uma pilha segue a regra LIFO (Last In, First Out), onde o último elemento inserido é o primeiro a ser removido. 

# Uma fila segue a regra LIFO (Last In, First Out), pois o último elemento inserido é o primeiro a sair. 

# Em uma fila, as inserções ocorrem no final (traseira) e as remoções no início (frente). 

# O método push() é usado para remover um elemento de uma pilha. 

# Tanto pilhas quanto filas podem ser implementadas usando listas, vetores ou estruturas encadeadas.

# 5. Explique, passo a passo, como o merge e quick sort funcionam para ordenar informações.
# R: O merge ele divide a lista em várias sublistas (sempre cortando ao meio) utilizando recursão, ou seja, separando os valores dentro da memória conforme a função for sendo chamada,
#por exemplo, em uma lista com 4 index [4, 3, 2, 1] o merge ira dividir ao meio a lista até que caiam no caso base de len(lista) == 1 que seria em [4] [3] | [2] [1] e fará isso com comparações entre esquerda e direita para ordenar lado (esquerdo ou direito) 
#e irá juntar/mesclar essas sublistas ordenadas retornando elas em uma nova lista de resultado conforme a condição for acontecendo
#
# R: No quick sort é sempre selecionado um pivô (que seria o ultimo elemento da lista), e baseado nesse valor, é separado em duas metades de valores onde temos valores maiores que o pivô e valores menores do que o pivô separando em listas,
#sendo assim é concatenado esses valores menores conforme eles são separados nessa condição do pivô, então ele chama a própria função recursivamente até que todos os resultados sejam menores do que o último e maior item da lista (pivô)