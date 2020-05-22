from controller import frontController


def update():
    control = True
    while control:
        id = int( input( 'Digite o id do servidor que quer atualizar :' ) )
        new_employee = input( 'Digite o nome do servidor  a ser adicionado' )
        try:
            if frontController.update_employee( id, new_employee ):
                print( 'ATUALIZAÇÃO REALIZADA COM SUCESSO!' )
                control = False
        except ValueError as er:
            print( f'\033[{er}. Por favor, insira novos valores válidos.' )
