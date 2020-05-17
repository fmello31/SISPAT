from model import fileManager
def consult ():
    information_search = int(input('Digite nº de tombo  do patrimônio :'))
    fileManager.Consult('patrimonios',information_search)
