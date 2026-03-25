qtdpercorrida = float(input("Digite a quantidade de KM percorridos: "))
qtddias = float(input("Digite a quantidade de dias em que o carro foi alugado: "))

precototal = (qtddias * 90) + (qtdpercorrida * 0.20)

print(f"O preço total a pagar será de R${precototal:.2f}")