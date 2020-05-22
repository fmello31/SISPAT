from controller import frontController

def register () :


        control = True
        while control:
            employee = input( 'Digite nome do servidor que quer registrar : ' )
            try:
                frontController.register_employee( employee )
                control = False
            except ValueError as er:
                print( f'\033[{er}' )
