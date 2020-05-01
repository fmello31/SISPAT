from model import local


def local_register(local_description):
    if 3 < len(local_description) <= 60:
        local_description = local_description.upper()
        local_description = [local_description]
        return local.save(new_local=local_description) #retornar o código da sala
    else:
        raise ValueError('O nome da sala deve ter mais que 3 e menos que 60 caracteres.')