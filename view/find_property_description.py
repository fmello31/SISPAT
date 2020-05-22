from controller import frontController

def find ():

   control = True
   while control:
        description = input('Digite nome do patrimonio que quer consultar : ')
        try:
            frontController.find_property( description )
            control = False
        except ValueError as er:
            print(f'\033[{er}')
