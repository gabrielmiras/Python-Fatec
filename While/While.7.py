"""Conversor de Moeda: Crie um programa que converta uma quantia em dólares para euros.
Continue pedindo ao usuário quantias em dólares para converter até que ele insira "0"."""

print("Conversor de Moeda: ")

while True:
    valor = float(input("Coloque o valor a ser convertido:"))
    usd =   valor * 0.85
    if valor > 0:
        print(f"USD em euros são R${usd:.2f}")
    elif valor <= 0:
        print("Valor indefinido")
    else :
        break


