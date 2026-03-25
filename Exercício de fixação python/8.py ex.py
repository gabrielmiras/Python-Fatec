mes = int(input("Digite o número do mês (1-12): "))
if mes in [1, 2, 3]:
    estacao = "Verão"
elif mes in [4, 5, 6]:
    estacao = "Outono"
elif mes in [7, 8, 9]:
    estacao = "Inverno"
elif mes in [10, 11, 12]:
    estacao = "Primavera"
else:
    estacao = "Mês inválido! Digite um número entre 1 e 12."

print(f"A estação correspondente é: {estacao}")