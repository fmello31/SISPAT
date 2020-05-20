from model import fileManager

def register () :
        newServidores = []
        servidor = ''
        while servidor != 'sair':
            servidor = input('Digite novo servidor (nome completo; número de matricula do Siape; tipo de usuário; senha ')
            if servidor != 'sair':
                newServidores.append(servidor)
            else:
                break
        fileManager.register('servidores_icti', newServidores)