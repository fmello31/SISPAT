import model
import sys
def sair():  # FUNCIONALIDADE 19 - SAIR
    desejaSalvar = input('Deseja salvar as informações?(SIM, NÃO): ').upper()
    if desejaSalvar == 'SIM':
        print('Salvando....')

    elif desejaSalvar == 'NÃO':
        return sys.exit()