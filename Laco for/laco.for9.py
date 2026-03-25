"""
9. Soma dos Dígitos de um Número

Tarefa: Peça um número ao usuário e some seus dígitos (exemplo: 123 → 1+2+3 = 6).
"""

numero = input("Digite um número: ")

soma = 0

for digito in numero:

    if digito.isdigit():
        soma += int(digito)

print(f"A soma dos dígitos de {numero} é: {soma}")
