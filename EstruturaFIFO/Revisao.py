''' Revisão sobre estruturas com filas e pilhas:
duas listas = alta e baixa
estrutura de repetição infinita (while True)
solicita as duas variáveis (documento e prioridade)
primeira estrutura de condição (1. adicionar documento)
incluir a estrutura para enviar os documentos com alta e baixa prioridade para as listas
segunda estrutura de condição (imprimir os documentos seguindo as estruturas FIFO ( pop(0) )
terceira estrutura de condição (parar estrutura de repetição infinita) '''

# Ex. 1

fila_alta = []
fila_baixa = []

while True:
    print("Selecione uma opção (1-3): ")
    opcao = input("1. Adicionar Documenteo\n2. Imprimir documento \n3. Sair da estrutura\n")

    if opcao == "1":
        tipo = input("Digite um ducumento: ")
        prioridade = input("Digite a prioridade ( alta e baixa )")

        if prioridade == "alta":
            fila_alta.append(tipo)
        else:
            fila_baixa.append(tipo)

    elif opcao == "2":
        if fila_alta:
            print(f"Imprimindo fila alta: \n{fila_alta.pop(0)}")
        elif fila_baixa:
            print(f"Imprimindo fila baixa: \n{fila_baixa.pop(0)}")
        else:
            print("Nenhum documento na fila")

    elif opcao == '3':
        break

# %%

"""
Um hospital recebe pacientes e os coloca em uma filla de atendimento. Cada paciente tem um nível de urgência que varia de 1 (menos urgênte) e
5 (mais urgente).


Exercício: Crie um programa que adicione pacientes à fila e atenda primeiro aqueles em maior nível de urgência. Se houver empate, siga ordem de chegada 
"""
fila = []

while True:
    print("Selecione uma opção (1-3): ")
    opcao = input("1. Adicionar Paciente\n2. Atender todos os pacientes \n3. Sair da estrutura\n")

    if opcao == "1":
        qtd_pacientes = int(input("Digite a quantidade de pacientes a serem atendidos"))
        for i in range(qtd_pacientes):
            paciente = []
            nome_paciente = input(f"Digite o {len(fila) + 1}° paciente a entrar na fila: ")
            prioridade = input("Digite a prioridade entre 1 (menos urgente) e 2 (mais urgente) do paciente: ")
            ordem_chegada = len(fila)

            paciente.append(nome_paciente)
            paciente.append(ordem_chegada)
            paciente.append(prioridade)
            fila.append(paciente)

        ordem_atendimento.sort(reverse=True)
        ordem_atendimento = sorted(fila, key=lambda X: (X[-1], X[1]))
        
    elif opcao == "2":
        print("Atendendo fila")
        print(f"Fila atual {ordem_atendimento}")
        
        while ordem_atendimento:
            proximo_paciente, ordem_chegada ,proxima_prioridade = ordem_atendimento.pop()

            print(f"Atendendo paciente: {proximo_paciente} com prioridade de: {proxima_prioridade}")

    elif opcao == '3':
        break

# Ciência de dados e construções de modelos

# AWS Academy = Da acesso a todos os cursos da AWS onde da a teoria e os labs para ferramentas para se certificar
# %%
