from . import fileManager

#TODO list, save, update, search or find

def list():
    fileManager.list('local')


def save(new_local):
   return fileManager.register('local', new_local)


def update(id, description):
    columns = ['description']
    description = [description]
    return fileManager.update(model='local', id=id, columns=columns, values=description)

def consult (description):
    return fileManager.Consult('local',description)