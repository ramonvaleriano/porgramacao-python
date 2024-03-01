"""
    Curso: Python: Crie a sua primeira Aplicação
    Diretório: Dicionarios
    Arquivo: exercicio03.py
    Dado: Crie um dicionário utilizando para representar números e seus quadrados de 1 a 5.
"""

# Funções para solucionar problemas.
def numero_ao_quadrado(inicio, fim):
    lista_dados = list(range(inicio, fim+1))

    dict_response = dict()

    for dado in lista_dados:
        dict_response[dado] = dado ** 2

    return dict_response

# Resolução da quetão.
quadrados = numero_ao_quadrado(1, 5)
print(quadrados)
