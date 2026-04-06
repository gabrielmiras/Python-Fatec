"""Simulador de Caixa Eletrônico: Crie um programa que simule um caixa eletrônico,
que continue pedindo ao usuário para inserir um valor de saque até que o saldo da conta seja zero ou negativo.
"""
print(" Caixa Eletrônico")

saldo_conta = 2000

while True:
    print(f"Saldo atual: R${saldo_conta}")
    opcao = input("Você deseja [sacar], [depositar] ou [sair]? ").lower()

    match opcao:
        case "sacar":
            valor = int(input("Digite o valor de saque: "))

            if valor <= 0:
                print("Valor inválido! Digite um número positivo.")
            elif valor > saldo_conta:
                print("Saldo insuficiente para este saque.")
            else:
                saldo_conta -= valor
                print(f"Saque de R${valor} realizado com sucesso!")

        case "depositar":
            valor = int(input("Digite o valor do depósito: "))
            if valor > 0:
                saldo_conta += valor
                print(f"R${valor} depositado com sucesso!")
            else:
                print("Valor de depósito inválido.")

        case "sair":
            print("Encerrando operação...")
            break

        case _:
            print("Opção inválida. Tente novamente.")


    if saldo_conta <= 0:
        print("Seu saldo chegou a zero.Você ficou pobre.")


print("Obrigado por usar nosso banco!")