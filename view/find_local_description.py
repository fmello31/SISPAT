from controller import frontController


def find ():
    control = True
    while control:
        description = input( 'Digite a descrição do local :' ).upper()
        try:
            if frontController.find_local_description(description):
                print( 'ATUALIZAÇÃO REALIZADA COM SUCESSO!' )
                control = False
            else:
                print('Estranho! Parece que algo de errado aconteceu com o seu arquivo de locais. Por favor, contacte o suporte de TI.')
        except ValueError as er:
            print(f'\033[{er}. Por favor, insira novos valores válidos.')
