from model import fileManager
id = int(input('Digite o id do local que quer atualizar :'))
new_local = input('Digite o novo local a ser adicionado')
fileManager.upgrade('local',id,new_local)

