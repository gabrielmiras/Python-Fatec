preco=float(input("Digite o valor do produto:"))
pagamento=(input("Digite o tipo do pagamento:"))

pagamento1="Pix"
pagamento2="Parcelado"

if preco>=2000 and pagamento==pagamento1:
    print("Você tem direito à desconto de 20%")
    if preco<2000 and pagamento==pagamento2:
        print("Sem desconto")
else:
    print("Sem desconto")