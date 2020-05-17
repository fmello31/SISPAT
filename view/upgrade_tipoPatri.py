from model import fileManager


def upgrade():
    id = int(input('Informe o id do Tipo de Patrimonio:\n'))
    new_tipPatrimonio = input('Informe o novo nome Tipo de Patrimônio:')
    notes = input( 'Informe as observações para o Tipo de Patrimônio:' )
    columns = {'notes', 'description'}
    values = {notes, new_tipPatrimonio}
    fileManager.upgrade('tipo_patrimonio', id, columns, values)
