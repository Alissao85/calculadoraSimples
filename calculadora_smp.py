escolha = 0

while escolha != 6:
    print("             =======] Calculadora Simples [=======\n")
    print("Escolha: [1] Para realizar a soma")
    print("Escolha: [2] Para realizar a subtração")
    print("Escolha: [3] Para realizar a multiplicação")
    print("Escolha: [4] Para realizar a divisão")
    print("Escolha: [5] Para elevar um número ao quadrado")
    print("Escolha: [6] Para encerrar o programa")

    escolha = int(input("Escolha a operação que deseja fazer: "))

    match escolha:
        case 1:
            print("Código para Realizar [soma]")
        case 2:
            print("Código para Realizar [subtração]")
        case 3:
            print("Código para Realizar [multiplicação]")
        case 4:
            print("Código para Realizar [divisão]")
        case 5:
            print("Código para Realizar [Elevar ao Quadrado]")
        case 6:
            print("Encerrando o programa. Até mais!")
        case _:
            print("Opção inválida. Tente novamente.\n")