"""17. Verificador de Paridade de Um Número

Tarefa: Solicite ao usuário um número e verifique se ele é par ou ímpar.

Se o número for par, divida-o por 2 e exiba o resultado.

Se o número for ímpar, multiplique-o por 3 e exiba o resultado.
"""
print("Verificador de Paridade Dinâmico")


for i in range(1, 6):
    num = int(input(f"({i}/5) Digite um número inteiro: "))


    if num % 2 == 0:
        resultado = num / 2
        print(f"O número {num} é PAR.")
        print(f"Resultado da divisão por 2: {resultado}")
    else:
        resultado = num * 3
        print(f"O número {num} é ÍMPAR.")
        print(f"Resultado da multiplicação por 3: {resultado}")

print("Processamento finalizado!")