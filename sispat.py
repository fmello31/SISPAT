from view import menu, register_property, register_employee, register_local, update_local, \
    update_property, update_employee,register_property_type, update_property_type,list_employee,list_local,list_property,find_property_description,find_property_tombo,list_property_type,find_local_description,find_property_type


sysout = False
opcoes = ['Consultar Patrimônio (Por desrição)', 'Consultar Patrimônio (Por tombo)', 'Listagem de Patrimônio',
          'Registro de Patrimônio',
          'Atualização dos Dados do Patrimônio', 'Lançamento de Entrada do Patrimônio (Por Local e Nota)',
          'Lançamento de Baixa do Patrimônio (Por Local e Nota)',
          'Registro de Servidor do ICTI', 'Atualização de Servidor (Por código interno ou Matricula SIAPE)',
          'Listagem dos Servidores do ICTI',
          'Registro de Local', 'Atualização de Local ( Por Código Interno)', 'Listagem de Local',
          'Consulta de Local(Por Descrição)',
          'Registro de Tipo de Patrimônio', 'Atualização do Tipo de Patrimônio (Por Código Interno)',
          'Listagem do Tipo de Patrimônio',
          'Consulta do Tipo de Patrimônio (Por descrição ou Código)', 'Sair']
# list > 3,10,13,17
#register > 4,8,11,15
#update >  5,9,12,16
#find > 1,2,14,18
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
        list_employee.list()
    elif resposta == 3:
        list_property.list()
    elif resposta == 4:
        register_property.register()
    elif resposta == 8:
        register_employee.register()
    elif resposta == 11:
        register_local.register()
    elif resposta == 12:
        update_local.update()
    elif resposta == 5:
        update_property.update()
    elif resposta == 9:
        update_employee.update()
    elif resposta == 16:
        update_property_type.update()
    elif resposta == 1 :
        find_property_description.find()
    elif resposta == 2 :
        find_property_tombo.find()
    elif resposta == 14:
        find_local_description.find()
    elif resposta == 18:
        find_property_type.find()
    elif resposta == 15:
        register_property_type.register()

    if not sysout:
        opcao = input( 'Deseja "sair" ou "voltar" para o menu ?' ).upper()
        if opcao == 'SAIR':
           sysout =True