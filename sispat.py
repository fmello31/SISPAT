from view import menu, register_property, register_employee, register_local, upgrade_local, \
    update_property, update_employee, update_property_type,list_local,list_property,consult_property_description,consult_property_tombo,list_property_type,consult_local_description,consult_property_type
from controller import frontController

sysout = False
opcoes = ['Consultar Patrimônio (Por desrição)', 'Consultar Patrimônio (Por tombo)', 'Listagem de Patrimônio',
          'Registro de Patrimônio',
          'Atualização dos Dados do Patrimônio', 'Lanaçamento de Entrada do Patrimônio (Por Local e Nota)',
          'Lançamento de Baixa do Patrimônio (Por Local e Nota)',
          'Registro de Servidor do ICTI', 'Atualização de Servidor (Por código interno ou Matricula SIAPE)',
          'Listagem dos Servidores do ICTI',
          'Registro de Local', 'Atualização de Local ( Por Código Interno)', 'Listagem de Local',
          'Consulta de Local(Por Descrição)',
          'Registro de Tipo de Patrimônio', 'Atualização do Tipo de Patrimônio (Por Código Interno)',
          'Listagem do Tipo de Patrimônio',
          'Consulta do Tipo de Patrimônio (Por descrição ou Código)', 'Sair']

while not sysout:
    #TODO Sispat > view > frontcontroller > model > filemanager
    resposta = menu.gerarMenu(opcoes)
    if resposta == 19:
        sysout = True
    elif resposta == 13:
        list_local.list()
    elif resposta == 17:
        list_property_type.list()
    elif resposta == 10:
        frontController.list()
    elif resposta == 3:
        list_property.list()
    elif resposta == 4:
        register_property.register()
    elif resposta == 8:
        register_employee.register()
    elif resposta == 11:
        register_local.register()
    elif resposta == 12:
        upgrade_local.update()
    elif resposta == 5:
        update_property.update()
    elif resposta == 9:
        update_employee.update()
    elif resposta == 16:
        update_property_type.update()
    elif resposta == 1 :
        consult_property_description.consult()
    elif resposta == 2 :
        consult_property_tombo.consult()
    elif resposta == 14:
        consult_local_description.consult()
    elif resposta == 18:
        consult_property_type.consult()

    if not sysout:
        opcao = input( 'Deseja "sair" ou "voltar" para o menu ?' ).upper()
        if opcao == 'SAIR':
           sysout =True