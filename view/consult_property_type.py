from controller import frontController

def consult():

  control = True
  while control:
    searchType = input('Deseja procurar o tipo de patrimonio por "id" ou "descrição" ? :').upper()
    if searchType == 'DESCRIÇÃO':
        information_search = input( 'Digite a descrição do tipo de patrimônio :' ).upper()
    elif searchType == 'ID' :
        information_search = int(input('Digite o Id do tipo de patrimonio :'))
    try:
        if frontController.consult_property_type(information_search):
            print( 'ATUALIZAÇÃO REALIZADA COM SUCESSO!' )
            control = False
        else:
            print(
                'Estranho! Parece que algo de errado aconteceu com o seu arquivo de tipo de patrimonios. Por favor, contacte o suporte de TI.' )
    except ValueError as er:
        print( f'\033[{er}. Por favor, insira novos valores válidos.' )
    else:
     fim = input( 'DESEJA "VOLTAR" PARA O  MENU PRINCIPAL OU "SAIR" ?' ).upper()
    if fim == 'Sair':
        sair()
