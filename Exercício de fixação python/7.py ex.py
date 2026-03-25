
idade = int(input("Digite a sua idade: "))

if idade <= 12:
    print("Classificação: Criança")
elif idade <= 18:
    print("Classificação: Adolescente")
elif idade <= 64:
    print("Classificação: Adulto")
else:
    print("Classificação: Idoso")