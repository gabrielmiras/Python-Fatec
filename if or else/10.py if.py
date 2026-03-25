caixa = int(input("Olá. Seu saldo é de R$1300,00. Você deseja sacar (1) ou depositar (2)? "))
dinheiro = 1300

if caixa == 1:
    saque = int(input("Quanto dinheiro você deseja sacar (R$)? "))
    dinheiro = dinheiro - saque
    if saque > 1300:
        print("Você não tem dinheiro suficiente na conta.")
    else:
        print(f"Você sacou R${saque}. Seu saldo agora é de R${dinheiro}.")
elif caixa == 2:
    depositar = int(input("Quanto dinheiro você deseja depositar (R$)? "))
    dinheiro = dinheiro + depositar
    print(f"Você depositou R${depositar}. Seu saldo agora é de R${dinheiro}")
else:
    print("Digite um número válido e tente novamente.")