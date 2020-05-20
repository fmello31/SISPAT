from controller import frontController



def register():
    control = True
    while control:
        local = input('Digite nome do local que quer registrar : ')
        try:
            frontController.register_local( local )
            control = False
        except ValueError as er:
            print(f'\033[{er}')
