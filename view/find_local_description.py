from controller import frontController


def find ():
    control = True
    while control:
        description = input( 'Digite a descrição do local :' )
        try:
            local = frontController.find_local_description(description)
            if local:
                print( 'BUSCA REALIZADA COM SUCESSO!' )
                print(local)
                control = False
        except ValueError as er:
            print(f'\033[{er}. Por favor, insira novos valores válidos.')
