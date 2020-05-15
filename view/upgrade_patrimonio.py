from model import fileManager


def upgrade():
    id = int(input('Digite o id do patrimonio que quer atualizar :'))
    new_patrimonio = input('Digite o novo local a ser adicionado')
    fileManager.upgrade('local', id, new_patrimonio)
