from . import fileManager

#TODO property methods: list, save, update and register


def list_property():
    fileManager.list('patrimonios')


def register(description):
    fileManager.register('patrimonios',description)


def update_property(id,new_property):
     columns = {'description'}
     new_property = [new_property]
     fileManager.update(model='patrimonios',id=id,columns=columns,values=new_property)


def find_property (information_search):
    return fileManager.find('patrimonios', information_search )
