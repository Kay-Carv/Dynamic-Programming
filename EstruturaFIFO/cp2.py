"""
Segunda avaliação de Dynamic Programming    -   26/09/2025
Tema:  Estruturas LIFO e FIFO

"""

# %%    Exercício 1
"""Você precisa desenvolver um sistema para simular o histórico de navegação de um navegador de internet. 
Cada vez que o usuário acessa uma nova página, ela é adicionada ao topo da pilha. O topo da pilha representa a página atual.
Quando o usuário aperta o botão voltar, a última página acessada é removida da pilha. Crie uma 
estrutura a qual 1. Seja possível inserir as informações, 2. Deletar o histórico de navegação de acordo com a estrutura da pilha,
 3. Mostrar que todo histórico foi apagado."""

historico_sites = []

print("Selecione uma opção de 1 a 3")

while True:

    opcao = input("1 - Navegar em novo site\n2 - Voltar \n3 - Limpar histórico de navegação")

    if opcao == '1':
        site = input("Digite o site que deseja acessar:")
        historico_sites.append(site)
        
        print(f"Site atual: {historico_sites[-1]}")
        print(f"Histórico de sites: {historico_sites}")

    elif opcao == '2':
        if historico_sites:
            voltar = historico_sites.pop()
            print(f"Você saiu do site: {voltar}", f'\nSite atual: {historico_sites[-1]}' if historico_sites else "Sem histórico disponível")
            print(f"Histórico atual: {historico_sites}")
        
        else:
            print("Ainda sem histórico disponível, não foi possível voltar")
    
    elif opcao == '3':
        if historico_sites:
            print("Limpando histórico")
            while historico_sites:
                limpar_site = historico_sites.pop()
                print(f"Removendo {limpar_site} do histórico")

            print("Todo o Histórico foi apagado")
            break

        else:
            print("Sem sites no histórico de navegação")

    else:
        print("Opção inválida")
# %%    Exercício 2

"""
 Você está desenvolvendo um sistema para organizar os chamados de suporte de uma empresa,
a qual envolve o Gerenciamento de Chamados com Fila e Histórico. Os clientes ligam e entram 
em uma fila de espera. O primeiro da fila deve ser sempre o próximo a ser atendido. 
 Cada cliente atendido vai para uma lista de atendidos (histórico). 
 Entretanto, às vezes é necessário refazer um atendimento. 
 Então, vamos identificar o 5º cliente atendido e colocá-lo de volta no final da fila original.
 Crie toda estrutura em python e explique o código desenvolvido. (5,0)

"""

fila_espera = []
historico_atendidos = []

print("Bem-vindo ao Sistema de Gerenciamento de Chamados")

while True:
    print("\n--- MENU ---")
    print("1 - Adicionar novo chamado para entrar na fila")
    print("2 - Atender próximo chamado")
    print("3 - Reencaminhar 5º cliente atendido para o final da fila")
    print("4 - Mostrar status da Fila e Histórico")
    print("5 - Sair")
    
    opcao = input("Opção: ")
    
    if opcao == '1':
        nome = input("Digite o nome do cliente que pediu o chamado: ")
        fila_espera.append(nome)
        print(f"\n Chamado do cliente '{nome}' adicionado à fila. Posição: {len(fila_espera)}")

    elif opcao == '2':
        if fila_espera:
            cliente_atendido = fila_espera.pop(0)
            historico_atendidos.append(cliente_atendido)
            
            print(f"\nCliente atendido: {cliente_atendido}")
            print(f"Total de chamados atendidos: {len(historico_atendidos)}")
            if fila_espera:
                print(f"Fila restante: {fila_espera}")
        else:
            print("\nA fila de espera está vazia.")

    elif opcao == '3':
        
        if len(historico_atendidos) >= 5:
            cliente_reatendimento = historico_atendidos[4]
            
            fila_espera.append(cliente_reatendimento)
            
            print(f"\n O 5º cliente atendido '{cliente_reatendimento}' foi posto no final da fila.")
            print(f"Nova posição na fila: {len(fila_espera)}")
        else:
            print(f"\nApenas {len(historico_atendidos)} clientes foram atendidos.")

    elif opcao == '4':
        print("\n--- STATUS ATUAL DO SISTEMA ---")
        print(f"Temos {len(fila_espera)} na fila de espera: {fila_espera}")
        print(f"Quantidade de atendimentos: {len(historico_atendidos)} \nHistórico de Atendidos: {historico_atendidos}")

    elif opcao == '5':
        print("Saindo do sistema")
        break

    else:
        print("\nOpção inválida")