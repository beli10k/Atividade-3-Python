opcao = 0

while opcao != 3:
    print("\nMenu:")
    print("[1] Olá")
    print("[2] Ajuda")
    print("[3] Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print("Você escolheu a opção Olá. Seja bem-vindo!")
    elif opcao == 2:
        print("Você escolheu a opção Ajuda. Como posso te ajudar?")
    elif opcao == 3:
        print("Saindo do programa. Até algum dia!")
    else:
        print("Opção errada. Tente novamente.")
