from controller import frontController


def find ():
    control = True
    while control:
        tombo = int(input( 'Digite o tombo do patrimônio  : ' ))
        try:
            frontController.find_property( tombo )
            control = False
        except ValueError as er:
            print( f'\033[{er}' )
