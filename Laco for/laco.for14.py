"""
14. Maior e Menor Número da Lista

Tarefa: Peça ao usuário para digitar 5 números e exiba o maior e o menor deles.
"""

print("Descubra o Maior e o Menor Número")


maior = 0
menor = 0

for i in range(1, 6):
    num = float(input(f"Digite o {i}º número: "))


    if i == 1:
        maior = num
        menor = num
    else:

        if num > maior:
            maior = num


        if num < menor:
            menor = num


print(f"O maior número digitado foi: {maior}")
print(f"O menor número digitado foi: {menor}")