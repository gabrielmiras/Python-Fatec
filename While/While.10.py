"""Controle de Votação: Faça um programa que permita cadastrar votos para 3 candidatos.
 Exibe contagem ao final quando for digitado "fim".

"""
print("Sistema de Votação (Limite: 3 votos)")
print("Candidatos: Gabriel, Davi, Joaquim, Rafael Barriga, Joneszão, Wellington")

votos = {
    "gabriel": 0,
    "davi": 0,
    "joaquim": 0,
    "rafael barriga": 0,
    "joneszão": 0,
    "wellington": 0
}

total_votos = 0

while total_votos < 3:
    voto = input(f"Voto nº {total_votos + 1} - Digite o nome: ").lower().strip()

    if voto in votos:
        votos[voto] += 1
        total_votos += 1
        print(f"Voto para {voto.capitalize()} computado!")
    else:
        print("Candidato não encontrado. Tente novamente.")

print(" Resultado Final ")
for candidato, total in votos.items():
    print(f"{candidato.capitalize()}: {total} votos")