"""
    Curso: Python: Crie a sua primeira Aplicação
    Diretório: Dicionarios
    Arquivo: exercicio05.py
    Dado: Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.
"""

# Funções para solucionar problemas.
def retorna_valores(dicionario):
    list_valores = list(dicionario.values())
    return list_valores

def filtrando_valores(list_dados):
    lista_filtrada = set(list_dados)
    return lista_filtrada

def quantos_cada(dicionario):
    lista_total = retorna_valores(dicionario)
    lista_filtrada = filtrando_valores(lista_total)
    dict_quantidade_nomeado = dict()

    for dado in lista_filtrada:
        quantidade = lista_total.count(dado)
        
        dict_quantidade_nomeado[dado] = quantidade

    return dict_quantidade_nomeado
    