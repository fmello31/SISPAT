from controller import frontController


def update():
    control = True
    while control:
        id = int( input( 'Digite o id do local que quer atualizar :' ) )
        new_local = input( 'Digite o novo local a ser adicionado' )
        try:
            if frontController.update_local( id, new_local ):
                print( 'ATUALIZAÇÃO REALIZADA COM SUCESSO!' )
                control = False
            else:
                print('Estranho! Parece que algo de errado aconteceu com o seu arquivo de locais. Por favor, contacte o suporte de TI.')
        except ValueError as er:
            print(f'\033[{er}. Por favor, insira novos valores válidos.')


'''
dois jogadores

Manual
Aleatório

4x4, 6x6, 8x8, 10x10

letras e números

nos tabuleiros de 8x8 e 10x10 - temos 2 caracteres especiais: @ e $ (25% das posições do tabuleiro)

Se um jogador acertar um par: 2 pontos
Se ele achar o par do @: ele ganha 4 pontos (perde 4 pontos)
Se ele achar o par do $: ele ganha 7 pontos (perde 7 pontos)

Se ele encontrar um par: ele ganha mais uma jogada'''