""" Árvore Binária          03/10/2025

- CP3 (24/10/2025)
- NEXT (08/11/2025)
- Próxima aula - Merge e Quick Sort

"""

# Execício

# Para lista [5, 3, 8, 4, 2], crie a estrutura da árvore binária, mostrando a divisão das sublistas até chegar ao respectivo valor unitário.

lista = [5, 3, 8, 4, 2]

esquerda = [5, 3, 8]
direita = [4, 2]

esquerda= [3, 5, 8]
direita = [2, 4]

lista = [2, 3, 4 ,5, 8]

# %% Exemplos


# Comprimento da lista dividido por 2 gerando dois lados sendo um esquerdo e um direito a gente vai repetir esse processo até que cada lado tenha apenas um valor unitário

# def meioLista(lista):
#     return len(lista)/2


lista = [5, 3, 8, 4, 2]

meio1 = len(lista)//2
print(meio1)

esquerdo = [5, 3, 8]
direito = [4, 2]

meio_esquerdo = len(esquerdo) // 2
print(meio_esquerdo)


# %%

# Utilizando a estrutura da árvore binária

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    print("Lista: ", arr)
    meio = len(arr) //2
    print("Meio: ", meio)
    esquerda = merge_sort(arr[:meio])   # Estrutura de função recursiva
    print("Esquerda: ", esquerda)
    direita = merge_sort(arr[meio:])    # Onde 
    print("Direira: ", direita)

    resultado = []
    print("Resultado: ", resultado)
    i = j = 0

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
    
    return resultado + esquerda[i:] + direita[j:]

lista = [5, 3, 8, 4, 2]
print("Resultado final: ", merge_sort(lista))
# %%
