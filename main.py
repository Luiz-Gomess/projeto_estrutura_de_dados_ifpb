from helpers.Jogo import Jogo, JogoException

try:    
    print('Bem Vindo ao Circuito Bomba !!')
    while True:
        jogo = Jogo()
        menuInicial = int(input('Digite 1 para iniciar um jogo manualmente -- Digite 2 para carregar um arquivo de texto.'))
        if menuInicial == 1: 
            numParticipantes = int(input('Digite a quantidade de jogadores: '))
            while True:
                jogador = input('Insira o nome do jogador:')
                jogo.inserirParticipante(jogador)
                if (jogo.quantParticipantes() == numParticipantes):
                    break

        if menuInicial == 2:
            pass

        numVencedores = int(input(f'Para inicar o jogo defina a quantidade de vencedores(1 - {numParticipantes - 1}: '))
        jogo.numVencedores(numVencedores)
        print('Que os jogos começem -_-')

        jogo.iniciarJogo()

        jogarNovamente = input('Deseja rodar novamente o programa (s)im/(n)ão?')
        if jogarNovamente == 'n':
            print('Obrigado por jogar')
            break
    
except JogoException as le:
    print(le)

# except Exception as e:
#     print('Algo inesperado aconteceu...')
