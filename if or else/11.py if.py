idade = int(input("Digite sua idade: "))

if idade < 16:
    print(f"Sua categoria é Juvenil")
elif idade < 30:
    print(f"Sua categoria é Profissional")
else:
    print(f"Sua categoria é Veterano")