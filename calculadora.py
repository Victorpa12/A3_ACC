def calculadora():
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    # Pegando a escolha do usuário
    escolha = input("Digite a operação (1/2/3/4): ")

    # Pegando os números do usuário
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    # Realizando as operações
    if escolha == '1':
        resultado = num1 + num2
        print(f"O resultado de {num1} + {num2} é: {resultado}")
    elif escolha == '2':
        resultado = num1 - num2
        print(f"O resultado de {num1} - {num2} é: {resultado}")
    elif escolha == '3':
        resultado = num1 * num2
        print(f"O resultado de {num1} * {num2} é: {resultado}")
    elif escolha == '4':
        if num2 != 0:
            resultado = num1 / num2
            print(f"O resultado de {num1} / {num2} é: {resultado}")
        else:
            print("Erro: Divisão por zero não é permitida.")
    else:
        print("Opção inválida.")

# Executando a calculadora
calculadora()