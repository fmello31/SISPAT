from controller import frontController


def update():


    control = True
    while control:
        id = int( input( 'Digite o id do  patrimônio que quer atualizar :' ) )
        new_property = input( 'Digite o  patrimônio a ser adicionado' )
        try:
            if frontController.update_property( id, new_property):
                print( 'ATUALIZAÇÃO REALIZADA COM SUCESSO!' )
                control = False
            else:
                print('Estranho! Parece que algo de errado aconteceu com o seu arquivo de  patrimonios. Por favor, contacte o suporte de TI.' )
        except ValueError as er:
            print( f'\033[{er}. Por favor, insira novos valores válidos.' )
