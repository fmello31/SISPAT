from controller import frontController


def update():

    control = True
    while control:
        id = int( input( 'Digite o id do tipo de patrimônio que quer atualizar :' ) )
        new_property_type = input( 'Digite o tipo de patrimônio a ser adicionado' )
        notes = input( 'Informe as observações para o Tipo de Patrimônio:' )
        try:
            if frontController.update_property_type( id, new_property_type,notes):
                print( 'ATUALIZAÇÃO REALIZADA COM SUCESSO!' )
                control = False
            else:
                print('Estranho! Parece que algo de errado aconteceu com o seu arquivo de tipos de patrimonios. Por favor, contacte o suporte de TI.' )
        except ValueError as er:
            print( f'\033[{er}. Por favor, insira novos valores válidos.' )
