from controller import frontController

def register():
    control = True
    while control:
        local = input( 'Digite a descrição do tipo de patrimônio : ' )
        try:
            frontController.register_property_type( local )
            control = False
        except ValueError as er:
            print( f'\033[{er}' )



