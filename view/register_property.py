from model import fileManager

###DUVIDAS

def register():
    newpatrimoniolist = []
    patrimonio = []
    pessoa = ''
    while pessoa != 'sair':
        pessoa = input('Digite novo patrimonio (nome patrimonio; número de tombo; descrição; preço médio):')

        patrimonio.append(pessoa)
        if pessoa != 'sair':
            newpatrimoniolist.append(patrimonio)
        else:
            break
    print(newpatrimoniolist)
    fileManager.register('patrimonios', newpatrimoniolist)
