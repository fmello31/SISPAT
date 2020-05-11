from model import fileManager
id = int(input('Digite o id do tipo de  patrimonio que quer atualizar :'))
new_tipPatrimonio = input('Digite a nova informação a ser a ser adicionado')
fileManager.upgrade('local',id,new_tipPatrimonio)
