print("Simulador de Compra em Loja Online")
compras=input("Digite o item a ser comprado.(teclado, mouse , monitor, headset): ").lower()
match compras:
    case "teclado":
        preco = 150.00
        print(f"O teclado custa R$ {preco:.2f}")
    case "mouse":
        preco = 80.00
        print(f"O mouse custa R$ {preco:.2f}")
    case "monitor":
        preco = 900.00
        print(f"O monitor custa R$ {preco:.2f}")
    case "headset":
        preco = 250.00
        print(f"O headset custa R$ {preco:.2f}")
    case _:
        print("Desculpe, não temos esse produto em estoque.")