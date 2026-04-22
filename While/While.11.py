"""Simulador de Caixa Registradora: O usuário digita o preço e a quantidade de produtos até digitar “sair”.
O Sistema mostra a quantidade de produtos e o valor final da compra."""

print("Caixa Registradora \n")
total_dinheiro=0
total_produtos=0
while True:
    precoproduto=input("Qual o preço do produto?").lower()
    if precoproduto == "sair":
        print("OBRIGADO PELA COMPRA 💸")
        break
    preco=float(precoproduto)
    quantidade=int(input("Qual a quantidade de produto?"))
    total_dinheiro+=preco*quantidade
    total_produtos+=quantidade
    print(f"Você comprou {total_produtos} produtos ")
    print(f"Você gastou {total_dinheiro} reais ")
