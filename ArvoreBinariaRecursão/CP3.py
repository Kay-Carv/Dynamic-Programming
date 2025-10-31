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