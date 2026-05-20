
matriz= [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]
cont=0
for L in range (3):
    for C in range (3):
        matriz[L][C]= int(input("Digite o valor: "))

    for L in range(3):
        for C in range(3):
            if matriz [L][C] % 2 == 0:
                cont+=1

            else:
                soma = matriz[L][C]

    for i in range(0, len(matriz)):
        print(matriz[i])
     