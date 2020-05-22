from controller import frontController


def register():
    control = True
    while control:
        description = input( 'Digite a informação que quer registrar do  patrimônio : ' )
        try:
            frontController.register_property( description )
            control = False
        except ValueError as er:
            print( f'\033[{er}' )
