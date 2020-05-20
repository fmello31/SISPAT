from . import fileManager


def list_property_type():
    fileManager.list('tipo_patrimonio')

def update_property_type(id,new_property_type,notes):
    columns = {'notes', 'description'}
    values = {notes, new_property_type}
    return fileManager.update('tipo_ptrimonio',id,columns,values)

def consult_property_type(information_search):
    return fileManager.Consult('tipo_patrimonio',information_search)
