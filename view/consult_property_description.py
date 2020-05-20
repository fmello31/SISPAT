from controller import frontController

def consult ():
   description = input('Digite a descrição do patrimônio :').upper()
   control = True
   while control:
        local = input('Digite nome do patrimonio que quer registrar : ')
        try:
            frontController.consult_property( description )
            control = False
        except ValueError as er:
            print(f'\033[{er}')
