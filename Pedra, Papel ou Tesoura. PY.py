import random

escolha_jogo = {
    1: 'pedra',
    2: 'papel',
    3: 'tesoura'
}

pontuacao_usuario = 0
pontuacao_pc = 0

partida = 'S'
while partida == 'S':
    
    escolha = int(input("\nfaça sua escolha, 1 para pedra, 2 para papel e 3 para tesoura: "))
    print(f"\nvocê escolheu {escolha_jogo[escolha]}")
        
    escolha_pc = random.randint(1, 3)
    print(f"\no inimigo escolheu {escolha_jogo[escolha_pc]}")
        
    if escolha_pc == 1 and escolha == 2:
        pontuacao_usuario+=1
        print("\nVocê ganhou! Papel mata pedra.")
    elif escolha_pc == 2 and escolha == 3:
        pontuacao_usuario+=1
        print("\nVocê ganhou! Tesoura mata papel.")
    elif escolha_pc == 3 and escolha == 1:
        pontuacao_usuario+=1
        print("\nVocê ganhou! Pedra mata Tesoura.")
    elif escolha == escolha_pc:
        print("\nEmpate!")
    else:
        pontuacao_pc+=1
        print("\nVocê perdeu!")

    partida = input("\nDeseja tentar novamente? [S/N]: ").strip().upper()

print(f"\nPontuação: Você {pontuacao_usuario} x {pontuacao_pc} pc")

