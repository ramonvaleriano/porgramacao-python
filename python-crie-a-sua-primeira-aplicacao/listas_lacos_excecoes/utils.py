
def cadastrar_restaurantes(lista_restaurante, restaurante, status):
    contador = 1
    registro_restaurentes = dict()

    if type(lista_restaurante) != list:
        print('Não é uma lsita de dados.')
        return lista_restaurante

    if len(lista_restaurante) == 0:
        registro_restaurentes = {
            'id': contador,
            'restaurante': restaurante,
            'status': status
        }

        lista_restaurante.append(registro_restaurentes)

    elif len(lista_restaurante) != 0:
        quantidade_restaurantes = len(lista_restaurante)
        contador = quantidade_restaurantes + 1

        registro_restaurentes = {
            'id': contador,
            'restaurante': restaurante,
            'status': status
        }

        lista_restaurante.append(registro_restaurentes)

    return lista_restaurante

def listar_restaurantes(lista_restaurantes):

    if type(lista_restaurantes) != list:
        print('Não é uma lsita de dados.')
        return lista_restaurantes
    
    if len(lista_restaurantes) == 0:
        print('Não há restaurentes cadastrados')
        return lista_restaurantes
    
    for dado in lista_restaurantes:
        print(f"Id: {dado['id']} - Restaurente: {dado['restaurante']} - Status: {dado['status']}")
        return lista_restaurantes
    
def ativar_restaurente(lista_restaurantes, restaurante, status):

    if type(lista_restaurantes) != list:
        print('Não é uma lsita de dados.')
        return lista_restaurantes
    
    if len(lista_restaurantes) == 0:
        print('Não há restaurentes cadastrados')
        return lista_restaurantes
    
    encontrou = False
    for dado in listar_restaurantes:
        if dado['restaurante'].lower() == restaurante.lower():
            encontrou = True

