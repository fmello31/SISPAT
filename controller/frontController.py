from model import local,property_type,property


#LOCAL OPTIONS---------------------------------------------------

def list_locals():
    return local.list()


def register_local(local_description):
    if 3 < len(local_description) <= 60:
        local_description = local_description.upper()
        local_description = [local_description]
        return local.save(new_local=local_description) #retornar o código da sala
    else:
        raise ValueError('O nome da sala deve ter mais que 3 e menos que 60 caracteres.')


def update_local(id, description):
    if type(id) == int and 3 < len(description) <= 60:
        description = description.upper()
        return local.update(id, description)
    else:
        raise ValueError('O id não é um número inteiro ou a descrição do local tem menos que 3 ou mais que 60 caracteres.')


def consult_local_description(description):
    if type(description) == str:
        description = description.upper()
        return local.consult(description)

#TYPE OF PATRIMONY OPTIONS ---------------------------------------------

def list_property_type():
    return property_type.list_property_type()

#def register_property_type():


def update_property_type(id, new_property_type, notes):
    if type(id) == int and 3 < new_property_type <= 60 :
        new_property_type = new_property_type.upper()
        return property_type.update_property_type ( id, new_property_type,notes )
    else:
        raise ValueError('O id não é um número inteiro e o novo tipo de patromônio tem menos de 3 ou mais de 60 caracteres')

def consult_property_type(information_search):
    if type(information_search) == int or str:
        if information_search == str:
            information_search = information_search.upper()
            return property_type.consult_property_type(information_search)
        else :
            return property_type.consult_property_type(information_search)
    else:
        raise ValueError('O id não é um número inteiro e o novo  patromônio tem menos de 3 ou mais de 60 caracteres')


# PATRIMONY OPTIONS

def list_property():
    return property.list_property()

#def register_property()

def update_property(id,new_property):

    if type(id) == int and 3 < new_property <= 60 :
        new_property = new_property.upper()
        return property.update_property ( id, new_property )
    else:
        raise ValueError('O id não é um número inteiro e o novo tipo de patromônio tem menos de 3 ou mais de 60 caracteres')

def consult_property(information_search):
    if information_search == str and 3 < information_search < 60 :
        information_search = information_search.upper()
        return property.consult_property( information_search )
    elif information_search == int:
        return property.consult_property()
    else :
        raise ValueError ('A descrição utilizada para consulta deve ter mais que 3  e menos que 60 caracteres ou o tombo tem que ter o valor de inteiro')

#TODO users stories of local, employees and property type
#TODO local (list, register, update and find or search)
#TODO employees (list, register, update and find or search)
#TODO property type (list, register, update and find or search)

