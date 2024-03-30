print('Olá, seja bem vindo a central telefônica do Natan, como deseja prosseguir?')

while True:

    print("Digite 1 para prosseguir, 2 para atualizar usuário existente, 0 para consultar a lista ou -1 para encerrar o atendimento.\n")
    Prosseguir = int(input())

    if Prosseguir == 1:
        arquivo = open("central.txt", "a")
        arquivo.write("\n\n")
        arquivo.write(input("Digite o nome do usuário novo:") + "\n")
        arquivo.write(input("Digite o CPF do usuário novo:") + "\n")
        arquivo.write(input("Digite o RG do usuário novo:") + "\n")
        arquivo.write(input("Digite o Telefone do usuário novo:") + "\n")
        arquivo.write(input("Digite o email do usuário novo:") + "\n")
        arquivo.write("\n\n")
        print("Obrigado, usuário resitrado!")
        arquivo.close()

    elif Prosseguir == 2:
        break

    elif Prosseguir == 0:
        with open("central.txt", "r") as arquivo:
            print(arquivo.read())
        print("Obrigado, volte sempre!")
        arquivo.close()
        continue

    elif Prosseguir == -1:
        print("Obrigado, volte sempre!")
        break

    else:
        print("Por favor, digite uma opção válida.")
        continue
