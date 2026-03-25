largura = float(input("Digite a largura da parede: "))
altura = float(input("Digite o valor da altura da parede: "))

area = largura * altura
qtd_tinta = area/2

print(f"A área da parede: {area}")
print(f"Quantidade de tinta necessária: {qtd_tinta:.1f} litros")