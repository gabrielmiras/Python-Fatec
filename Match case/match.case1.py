print("Conversor de moedas")
while True:
    moeda=input("Selecione a Moeda, Dólar (USD), Euro (EUR) e Libra (GBP) para reais: ").lower()
    valor=float(input("Coloque o valor a ser convertido:"))

    usd= valor * 5
    eur= valor * 6
    gbp= valor * 7
    match moeda:
        case "usd":
            print(f"Seus USD em reais são R${usd:.2f}")
        case "eur":
            print(f"Seus euros em reais são R${eur:.2f} ")
        case "gbp":
            print(f"Suas Libras em reais são R${gbp:.2f}")
    



