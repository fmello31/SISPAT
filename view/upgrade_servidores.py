from model import fileManager
id = int(input('Digite o id do servidor que quer atualizar :'))
new_servidor = input('Digite a informção do servidor  a ser adicionado ')
fileManager.upgrade('local',id,new_servidor)