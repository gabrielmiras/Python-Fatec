valor = float(input("Digite o valor da compra: R$ "))

print("1 - Pix (10% desconto)")
print("2 - Cartão (5% acréscimo)")
opcao = input("Escolha a opção: ")

match opcao:
    case "1":
        total = valor * 0.90
        print(f"Total com desconto: R$ {total:.2f}")
    case "2":
        total = valor * 1.05
        print(f"Total com acréscimo: R$ {total:.2f}")
    case _:
        print("Opção inválida!")