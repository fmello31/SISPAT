from model import fileManager
def consult ():
    searchType = input('Deseja procurar o tipo de patrimonio por "id" ou "descrição" ? :').upper()
    if searchType == 'DESCRIÇÃO':
        information_search = input('Digite a descrição do tipo de patrimônio :').upper()
    elif searchType == 'ID':
         information_search = int(input('Digite o Id do tipo de patrimonio :'))

    fileManager.Consult('tipo_patrimonio',information_search)
