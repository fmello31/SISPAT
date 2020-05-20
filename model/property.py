from . import fileManager

#TODO property methods: list, save, update and register


def list_property():
    fileManager.list('patrimonios')


def register():
    fileManager.register('patrimonios')


def update_property(id,new_property):
     columns = {'description'}
     new_property = [new_property]
     fileManager.update('patrimonios',id,columns,new_property)


def consult_property (information_search):
    return fileManager.Consult('patrimonios', information_search )
