from model import fileManager
def consult ():
    information_search = input('Digite a descrição do local :')
    fileManager.Consult('local',information_search)
