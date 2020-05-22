from . import fileManager

#TODO list, save, update and find


def list ():
    fileManager.list('servidores')


def save(employee):
   fileManager.register('servidores',employee)


def update(id,nome):
    columns = ['description']
    nome = [nome]
    return fileManager.update( model='servidores', id=id, columns=columns, values=nome )