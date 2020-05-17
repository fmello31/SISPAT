from model import fileManager
def consult ():
    information_search = input('Digite a descrição do patrimônio :').upper()
    fileManager.Consult('patrimonios',information_search)

