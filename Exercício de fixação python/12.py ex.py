nota = float(input("Digite a nota do aluno: "))
presenca = int(input("Digite a presença do aluno (em %): "))

if nota >= 7:
    if presenca >= 75:
        print("Aluno aprovado com boa nota e presença!")
    else:
        print("Aluno aprovado, mas com presença abaixo do necessário.")
else:
    if presenca >= 75:
        print("Aluno reprovado pela nota, mas com presença boa.")
    else:
        print("Aluno reprovado por nota e presença.")