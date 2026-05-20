"""Crie uma matriz 3x3 com valores digitados pelo usuário."""

matriz= [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

for L in range (3):
    for C in range (3):
        matriz[L][C]= int(input("Digite o valor: "))
    for i in range(0, len(matriz)):
        print(matriz[i])