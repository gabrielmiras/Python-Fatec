"""
15. Números Positivos e Negativos

Tarefa: Peça ao usuário 10 números e exiba quantos são positivos, negativos ou zero.
"""
print("Números Positivos e Negativos: ")
npositivo=0
nnegativos=0
zero=0
for i in range(1, 11):
    num = float(input(f"Digite o {i}º número: "))
    if num > 0:
       npositivo += 1
    elif num < 0:
       nnegativos += 1
    else:
        zero += 1
print(f"Quantidade de positivos: {npositivo}")
print(f"Quantidade de negativos: {nnegativos}")
print(f"Quantidade de zeros: {zero}")