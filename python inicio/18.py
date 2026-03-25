custofabrica = float(input("Digite o valor de fábrica do carro: "))

custoconsumidor = custofabrica + (custofabrica * 73 / 100)
print(f"O custo ao consumidor será de R${custoconsumidor:.2f}")