peso=float(input("Digite o seu peso: "))
altura=float(input("Digite sua altura: "))
IMC= peso / (altura ** 2)
print(f"Seu IMC é: {IMC:.2f}")
if IMC < 18.5:
    print("Abaixo do peso")
elif IMC < 24.9:
    print("Peso normal")
elif IMC < 29:
    print("Sobrepeso")
else:
    print("Obesidade")
