from . import fileManager


def list_property_type():
    fileManager.list('tipo_patrimonio')

def update_property_type(id,new_property_type,notes):
    columns = {'notes', 'description'}
    values = {notes, new_property_type}
    return fileManager.update(model='tipo_patrimonio',id=id,columns=columns,values=values)

def find_property_type(information_search):
    return fileManager.find('tipo_patrimonio',information_search)

def save_propert_type(description):
    return fileManager.register('tipo_patrimonio',description)