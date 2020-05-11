from view import menu, registro_patrimonio, registro_servidor_icti, registro_local, sair,upgrade_local,upgrade_patrimonio,upgrade_servidores,upgrade_tipoPatri
from model import local, tipo_patrimonio,servidores_icti,patrimonios

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

resposta = menu.gerarMenu(opcoes)

if resposta == 19:
    sair.sair()
elif resposta == 13:
    local.list()
elif resposta == 17:
    tipo_patrimonio.list()
elif resposta == 10:
    servidores_icti.list()
elif resposta == 3:
    patrimonios.list()
elif resposta == 4:
    registro_patrimonio.register()
elif resposta == 8:
    registro_servidor_icti.register()
elif resposta == 11:
    registro_local.register()
elif resposta == 12:
    upgrade_local.upgrade()
elif resposta == 5:
    upgrade_patrimonio.upgrade()
elif resposta == 9 :
    upgrade_servidores.upgrade()
elif resposta == 16:
   upgrade_tipoPatri.upgrade()