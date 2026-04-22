"""Sistema de Vendas com Estoque Reduzido:
O Sistema define um estoque inicial de produtos e a cada venda, retira quantidade do estoque.
O sistema encerra quando não permite vender mais do que o disponível."""
print("Sistema de estsoque reduzido")
lista_produtos = ["Café",10], ["TV", 20],["Mouse", 15]

cafe_on_estoque=10
Tv_on_estoque=20
mouse_on_estoque=15
produtos_carrinho=0
cafecarrinho=0
tvcarrinho=0
mousecarrinho=0
while True:
    compra = input("Qual produto você quer comprar? (Digite 'help' para ver lista de produtos ou 'sair'): ").lower()
    if compra == "sair":
        print(f"você tem {mousecarrinho} mouse no carrinho, {tvcarrinho} Tv's no carrinho e {cafecarrinho} caixas de café no carrinho \n OBRIGADO PELA PREFERÊNCIA  ")
        break
    elif compra == "help":
        print(f"{lista_produtos}")
    elif compra == "café" or compra == "cafe":
        produtos_carrinho+=1
        cafecarrinho+=1
        cafe_on_estoque-=1
        print(f"Café adicionado no carrinho, você tem {produtos_carrinho} de produtos no carrinho e restam {cafe_on_estoque} caixas de café ")
    elif compra == "tv" :
        produtos_carrinho +=1
        tvcarrinho+=1
        Tv_on_estoque -=1
        print(f" TV adicionada no carrinho, você tem {produtos_carrinho} de produtos no carrinho e restam {Tv_on_estoque} TV's no estoque ")
    elif compra == "mouse":
        produtos_carrinho +=1
        mousecarrinho+=1
        mouse_on_estoque -=1
        print(f"Mouse adicionado ao carrinho você tem {produtos_carrinho} de produtos no carrinho e restam {mouse_on_estoque} Mouse's no estoque ")

    else:
        print("Produto não encontrado. Digite 'help' para ver as opções.")



