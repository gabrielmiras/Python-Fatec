#O usuário deve informar o tipo de produto (Eletrônico, Roupas, Alimentos, Móveis:),
#e o programa exibirá o percentual de desconto correspondente.

tipo = input("Escolha um tipo de produto: Eletrônico, Roupas, Alimentos e Móveis:  ").lower()

match tipo:
    case "eletrônico" | "eletronicos":
        print("O desconto para eletrônicos é 200 reais")
    case "roupas":
        print("O desconto para roupas é 40 reais")
    case "alimentos":
        print("O desconto para alimentos é 10 reais")
    case "móveis" | "moveis":
        print("O desconto para móveis é 100 reais")
    case _:
        print("C digitou errado")