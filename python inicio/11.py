produto = float(input("Digite o valor do produto: "))

desconto = produto * (10 / 100)
valorfinal = produto - desconto

print(f"O valor do produto com 10% de desconto é de {valorfinal:.2f}")