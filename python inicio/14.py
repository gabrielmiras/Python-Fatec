quantidade = float(input("Digite a quantidade de kWh consumidos: "))
valor = float(input("Digite o valor por kWh: "))

valortotal = quantidade * valor

print(f"O valor a ser pago da conta de energia é de {valortotal:.2f} reais")