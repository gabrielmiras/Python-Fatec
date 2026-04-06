"""Média de Notas: Escreva um programa que continue pedindo ao usuário para inserir notas (0 a 10) e calcule a média dessas notas.
O programa deve parar quando o usuário digitar uma nota negativa.
"""

print("Média de notas")

somanota = 0
numnota = 0
while True:
    num = float(input("Digite uma nota (1 a 10) ou digite sair para encerrar:"))
    if num > 0 and num < 11:
        numnota += 1
        somanota += num
    elif str(num) == 'sair':
        break
    else:
        break
    print(f"A média até agora é {somanota / numnota}.")