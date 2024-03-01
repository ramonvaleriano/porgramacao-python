"""
    Curso: Python: Crie a sua primeira Aplicação
    Diretório: Lista, laços e exeções
    Arquivo: exercicio02.py
    Dado: Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.
"""

# Funções para resolver os exercícios:
def criar_lista(quantidade):
    lista_dados = list()
    if quantidade:
        for i in range(quantidade):
            dado = input('Digite o dado que deseja adicionar: ')
            lista_dados.append(dado)

    return lista_dados

def visualizar_lista(lista):
    for indice, dado in enumerate(lista):
        print(f"{indice+1} - {dado}")

# Rodando Aplicação:
lista_dados = criar_lista(3)
visualizar_lista(lista_dados)