from controller import frontController

def register_property_type():
    control = True
    while control:
        local = input( 'Digite a descrição do tipo de patrimônio : ' )
        try:
            frontController.register_assets_type( local )
            control = False
        except ValueError as er:
            print( f'\033[{er}' )
    else:
        fim = input( 'DESEJA "VOLTAR" PARA O  MENU PRINCIPAL OU "SAIR" ?' ).upper()
        if fim == 'Sair':
            sair()


##DUVIDAS