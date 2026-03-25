
nota = float(input("Digite a nota do aluno (0 a 100): "))


if nota >= 90:
    print("Classificação: A")
elif nota >= 80:
    print("Classificação: B")
elif nota >= 70:
    print("Classificação: C")
elif nota >= 60:
    print("Classificação: D")
else:
    print("Classificação: F (Reprovado)")