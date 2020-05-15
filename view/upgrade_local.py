from model import fileManager


def upgrade():
    id = int(input('Digite o id do local que quer atualizar :'))
    new_local = input('Digite o novo local a ser adicionado')
    new_line = f'{id};{new_local}'
    fileManager.upgrade('local', id, new_line)

