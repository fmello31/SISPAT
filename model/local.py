from . import fileManager


def list():
    fileManager.list('local')


def save(new_local):
   return fileManager.register('local', new_local)
