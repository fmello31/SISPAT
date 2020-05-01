

def mostraLinhas():
    print('\033[30m-\033[m' * 80)


def gerarMenu(lista):  # GERAR MENU DE OPÇÕES
    mostraLinhas()
    print('               \033[0;34mSISPAT - SISTEMA DE PATRIMÔNIO DO ICTI - UFBA\033[m')
    mostraLinhas()
    c = 1
    for item in lista:
        print(f'\033[0;34m{c}\033[m - {item}')
        c += 1
    mostraLinhas()
    opcao = lerInt('Escolha a funcionalidade do menu que quer acessar: ')
    return opcao


def lerInt(num):  # CRIAR INPUT COM NÚMERO INTEIRO
    while True:
        try:
            n = int(input(num))
        except (ValueError, TypeError):
            print('\033[31mERRO OPÇÃO INVÁLIDA, DiGITE UM NÚMERO INTEIRO VÁLIDO DENTRE AS OPÇÕES DO MENU !!!!!\033[m')
            continue
        except(KeyboardInterrupt):
            print('\n\033[31mO USUÁRIO NÃO DIGITOU NENHUM NÚMERO')
            return 0
        else:
            return n



