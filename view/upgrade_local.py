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
    else:
        fim = input('DESEJA "VOLTAR" PARA O  MENU PRINCIPAL OU "SAIR" ?').upper()
        if fim == 'Sair':
            sair()