#Aula 2 - Estruturas com (LIFO) Last in First Out           12/09/2025

# Ao contrário da FIFO a LIFO é o "O último a entrar vai ser o primeiro a sair"
# Ex: em um estoque de uma fábrica de produção de chapas, onde elas são empilhadas uma em cima da outra, a útima a ser armazenada será a primeira a sair

# Outro caso é na logistica de transportes em centros de distribuições ( Amazon, Mercado Livre) onde o abastecimento de carga no caminhão é ótimizado para embarcar os produtos de acordo
#com a ordem de rota de entrega

# ALGORITIMOS de ROTAS 
# Algoritmo de Dijkstra
# A* - (A star)
# Algoritimo colônias de formigas

# %% Ex1. EXEMPLO !
pilha = []

pilha.append("Cliente 1")
pilha.append("Cliente 2")
pilha.append("Cliente 3")

print(pilha)            # Output ['Cliente 1', 'Cliente 2', 'Cliente 3']
pilha.pop()             # 'Cliente 3'


# %% Ex2. Exemplo 2

pilha = [ "Produto 1", "Produto 2", "Produto 3"]

while pilha:
    produto = pilha.pop()
    print(f"O produto {produto} está saindo da pilha")

    # output
    # O produto Produto 3 está saindo da pilha
    # O produto Produto 2 está saindo da pilha
    # O produto Produto 1 está saindo da pilha


# %% Ex3. Exemplo 3

pilha = [ "Produto 1", "Produto 2", "Produto 3"]
i = 0

for i in range(len(pilha)):
    produto = pilha.pop()
    print(f"{produto} retirado da pilha")

    # OUTPUT
    # Produto 3 retirado da pilha
    # Produto 2 retirado da pilha
    # Produto 1 retirado da pilha


# %% Exercício 4

# Ex.1) Um escritório recebe documentos, que precisam ser processados. O último documento adicionado deve ser
#o primeiro a ser processado (LIFO)

# a) Peça o nome dos documentos e os adicione a pilha.
# b) Processe os documentos na ordem a que foram adicionados.
# c) Após processar todos os documentos, exiba a informação de que todos os documentos foram processados 



documentos = []

for i in range(3):
    cpf = int(input("Digite o número do documento a ser procesasdo: "))
    documentos.append(cpf)

i = 0
for i in range(len(documentos)):
    NumeroDocumento = documentos.pop()
    print(f"Processando o {i + 1}° documento de número {NumeroDocumento}")
    i += i

# %% Exercício 5

# Ex. 5 - Desenolva um algoritimo para adicionar e remover clientes em uma lista. O algoritmo deve conter
#as seguintes escolhas para resolver o problema de filas (FIFO)

# Opção 1: Adicionar cliente, em seguida, insira um valor
# Opção 2: Atender cliente
# Opção 3: Mostrar fila
# Opção 4: Sair


def adicionarCliente(fila):
    quantidadeClientes = int(input("Digite a quantidade de clientes que deseja adicionar a fila: "))

    for i in range(quantidadeClientes):
        cliente = input("Digite um cliente para entrar na fila: ")
        fila.append(cliente)
        print(f" Cliente {cliente} adicionado a fila ")

    print(fila)

    return fila


def atenderCliente(fila):
    if not fila:
        return "A fila já está vazia"
    
    else:
        atentimento = fila.pop(0)
        print(f"Cliente {atentimento} foi atendido")
        return fila


def mostrarFila(fila):
    print(fila)

opcao = '0'

fila = []

while opcao[0] != '4':
    print("---- Sistema de atendimento ----")
    opcao = input("\nDigite uma opção:  \n1. Adicionar cliente \n2.Atender Cliente \n3. Mostrar Fila \nSair ")

    match (opcao[0]):
        case '1':
            fila.append(adicionarCliente(fila))

        case '2':
            fila  = atenderCliente(fila)

        case '3':
            mostrarFila(fila)
        case _:
            print("Insira uma opção valida")

print("Encerrando o sistema...")

# %% Exercício 5 (Resolvido pelo Professor) - 

fila = []

while True:
    print("---- Sistema de atendimento ----")
    opcao = input("\nDigite uma opção:  \n1. Adicionar cliente \n2.Atender Cliente \n3. Mostrar Fila \nSair ")

    if opcao == '1':
        cliente = input("Nome do cliente: ")
        fila.append(cliente)

    elif opcao == '2':
        if fila:
            atendimento = fila.pop(0)
            print(f"Atendendo {atendimento} ")
        else:
            print("A fila está vazia")

    elif opcao == '3':
        print(f'Fila atual = {fila} ' if fila else "Fila vazia")      

    elif opcao == '4':
        print("\n Encerrando atendimento")

    else:
        print("Opção inválida")
        break
print("Fim do sistema")

# %% Exercício 6

#EX.6)  Uma impressora recebe pedidos de impressões de diferentes usuários. Cada documento tem um nome e um nível de prioridade (alta ou baixa).
# Os documentos de prioridade alta devem ser impressos antes dos documentos de prioridade baixa.

# Crie um sistema que adicone documentos á fila de impressão e os imprima na ordem correta (FIFO)

pedidos = []

for i in range(3):
    pedido = []
    documento = input("Digite o documento")
    prioridade = input("Digire a priorida 0 ou 1")
    pedido.append(documento)
    pedido.append(prioridade)
    pedidos.append(pedido)

ordemPrioridade = sorted(pedidos, key=lambda X: X[-1])

print("\n--- Documentos na fila de impressão ---")
print(ordemPrioridade)

while ordemPrioridade:
    proximaImpressao, proximaPrioridade = ordemPrioridade.pop(0)

    print(f"Prioridade {proximaPrioridade}: Imprimindo documento: {proximaImpressao}")

    if not ordemPrioridade:
        break

# %%    
"""Exercício 7: Gestão de Tarefas (LIFO)
Crie um programa que simule uma lista de tarefas a serem realizadas por um funcionário. A regra é que a última tarefa adicionada à lista
deve ser a primeira a ser concluída.

a) Peça ao usuário para inserir o nome de 5 tarefas. Adicione-as a uma pilha (lista).
b) Após adicionar as 5 tarefas, processe-as na ordem LIFO, exibindo uma mensagem a cada tarefa concluída.
c) Ao final, exiba a mensagem "Todas as tarefas foram concluídas com sucesso!".
"""
lista_tarefas = []
qtd_tarefas = 5

print("---Lista de tarefas a serem feitas---")
print(f"Olá funcionário, insira as suas {qtd_tarefas} que serão feitas")

for i in range(qtd_tarefas):
    nova_tarefa = input(f"Insira a {i + 1}° tarefa")
    i += 1
    lista_tarefas.append(nova_tarefa)

print(lista_tarefas, "\n")

while lista_tarefas:
    tarefa_concluída = lista_tarefas.pop()
    print(f"Executando a tarefa: {tarefa_concluída}")


print("---Todas as tarefas foram concluídas com sucesso! ---")
