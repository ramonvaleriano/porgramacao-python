"""
    Curso: Python: Crie a sua primeira Aplicação
    Diretório: Dicionarios
    Arquivo: exercicio04.py
    Dado: Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.
"""

from Exercicio02 import (
    retorna_keys
)

# Funções para solucionar problemas.
def valida_chave(chave, dicionario):
    lista_keys = retorna_keys(dicionario)
    if chave in lista_keys:
        print('Existe essa chave')
        return None
    
    print('Não existe essa chave')
