a = float(input("Digite o primeiro A: "))
b = float(input("Digite o segundo B: "))

if a % b == 0 or b % a == 0:
    print(f"Os números {a} e {b} são múltiplos")
else:
    print(f"Os números {a} e {b} não são múltiplos")