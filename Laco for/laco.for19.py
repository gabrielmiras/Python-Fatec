"""19. Adivinhação de Número

Tarefa: O computador escolhe um número aleatório de 1 a 10,
e o usuário tem 3 tentativas para adivinhar. Dê dicas se o número é maior ou menor.
"""

import random

print("=== Jogo de Adivinhação ===")

numero_secreto = random.randint(1, 10)
acertou = False

print("Eu escolhi um número entre 1 e 10. Você tem 3 tentativas!")


for tentativa in range(1, 4):
    chute = int(input(f"Tentativa {tentativa}: Qual o seu chute? "))

    if chute == numero_secreto:
        print(f"Parabéns! Você acertou o número {numero_secreto}!")
        acertou = True
        break
    elif chute < numero_secreto:
        print("Dica: O número secreto é MAIOR.")
    else:
        print("Dica: O número secreto é MENOR.")


if not acertou:
    print(f"\nQue pena! Suas tentativas acabaram. O número era {numero_secreto}.")