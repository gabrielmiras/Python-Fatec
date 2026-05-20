def mapear_tabuleiro():
    """Gera um dicionário para o tabuleiro usando posições de 1 a 9."""
    return {str(i): " " for i in range(1, 10)}


def exibir_tabuleiro(tabuleiro):
    """Exibe o tabuleiro formatado no terminal."""
    print(f"\n {tabuleiro['1']} | {tabuleiro['2']} | {tabuleiro['3']} ")
    print("---|---|---")
    print(f" {tabuleiro['4']} | {tabuleiro['5']} | {tabuleiro['6']} ")
    print("---|---|---")
    print(f" {tabuleiro['7']} | {tabuleiro['8']} | {tabuleiro['9']} \n")


def verificar_vencedor(tab, j):
    """Verifica todas as combinações possíveis de vitória para o jogador 'j'."""
    vitorias = [
        ["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"],  # Linhas
        ["1", "4", "7"], ["2", "5", "8"], ["3", "6", "9"],  # Colunas
        ["1", "5", "9"], ["3", "5", "7"]  # Diagonais
    ]
    for combo in vitorias:
        if tab[combo[0]] == tab[combo[1]] == tab[combo[2]] == j:
            return True
    return False


def verificar_empate(tabuleiro):
    """Se não houver espaços vazios, o jogo empatou."""
    return " " not in tabuleiro.values()


def jogar():
    tabuleiro = mapear_tabuleiro()
    jogador_atual = "X"

    print("=" * 30)
    print("      JOGO DA VELHA EM PYTHON  ")
    print("=" * 30)
    print("Instruções: Escolha uma posição de 1 a 9 conforme o esquema:")
    print(" 1 | 2 | 3 \n---|---|---\n 4 | 5 | 6 \n---|---|---\n 7 | 8 | 9 ")
    print("=" * 30)

    while True:
        exibir_tabuleiro(tabuleiro)
        jogada = input(f"Jogador [{jogador_atual}], escolha uma posição (1-9): ").strip()

        # Validação da jogada
        if jogada not in tabuleiro:
            print("❌ Posição inválida! Digite um número de 1 a 9.")
            continue

        if tabuleiro[jogada] != " ":
            print("❌ Essa posição já está ocupada! Tente outra.")
            continue

        # Aplica a jogada
        tabuleiro[jogada] = jogador_atual

        # Verifica se o jogador atual ganhou
        if verificar_vencedor(tabuleiro, jogador_atual):
            exibir_tabuleiro(tabuleiro)
            print(f"🎉 Parabéns! O jogador [{jogador_atual}] venceu o jogo! 🎉\n")
            break

        # Verifica se deu empate (velha)
        if verificar_empate(tabuleiro):
            exibir_tabuleiro(tabuleiro)
            print("🤝 O jogo terminou em empate (DEU VELHA)! 🤝\n")
            break

        # Alterna o jogador
        jogador_atual = "O" if jogador_atual == "X" else "X"


if __name__ == "__main__":
    jogar()