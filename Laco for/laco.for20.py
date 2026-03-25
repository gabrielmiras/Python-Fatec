"""20. Números Primos

Tarefa: Crie um programa que solicite ao usuário um número e informe se ele é primo ou não.
Lembre-se de que um número primo é aquele que é divisível apenas por 1 e por ele mesmo.
"""

print("Verificador de Números Primos")
num = int(input("Digite um número inteiro: "))


if num <= 1:
    eh_primo = False
else:
    eh_primo = True


    for i in range(2, num):
        if num % i == 0:

            eh_primo = False
            break


if eh_primo:
    print(f"O número {num} é PRIMO!")
else:
    print(f"O número {num} NÃO é primo.")