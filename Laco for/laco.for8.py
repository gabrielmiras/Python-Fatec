soma = 0

for i in range(5):
    nota = float(input(f"Digite a nota {i + 1}: "))
    soma = soma + nota

media = soma / 5

print(f"Soma total: {soma}")
print(f"Média das 5 notas: {media:.2f}")