dp = float(input("Digite a distância a ser percorrida (em km): "))
vm = float(input("Digite a velocidade média do carro (em km/h): "))

tempo = (dp * 100) / (vm * 100)

print(f"O tempo da viagem foi de {tempo:.1f} horas")