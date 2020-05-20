from controller import frontController


def consult ():
    control = True
    while control:
        tombo = input( 'Digite o tombo do patrimônio  : ' )
        try:
            frontController.consult_property( tombo )
            control = False
        except ValueError as er:
            print( f'\033[{er}' )
    else:
        fim = input( 'DESEJA "VOLTAR" PARA O  MENU PRINCIPAL OU "SAIR" ?' ).upper()
        if fim == 'Sair':
            sair()