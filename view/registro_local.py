from controller import frontController
from . import sair


def register():

    control = True
    while control:
        local = input('Digite nome do local que quer registrar : ')
        try:
            frontController.local_register(local)
            control = False
        except ValueError as er:
            print(f'\033[{er}')
    else:
        fim = input('DESEJA "VOLTAR" PARA O  MENU PRINCIPAL OU "SAIR" ?').upper()
        if fim == 'Sair':
            sair()