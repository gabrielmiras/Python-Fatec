peso=float(input("Qual o seu peso?:"))
altura=float(input("Qual a sua altura?:"))
IMC = peso/(altura*altura)
if IMC < 18.5:
    print("Abaixo do peso")
elif IMC < 24.9:
    print("Peso normal")
elif (IMC < 29):
    print("Sobrepeso")
else:
    print("Obesidade")
