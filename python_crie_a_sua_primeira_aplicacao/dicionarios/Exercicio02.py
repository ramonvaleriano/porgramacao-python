"""
    Curso: Python: Crie a sua primeira Aplicação
    Diretório: Dicionarios
    Arquivo: exercicio01.py
    Dado: Utilizando o dicionário criado no item 1:

            Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
            Adicione um campo de profissão para essa pessoa;
            Remova um item do dicionário.
"""

from Exercicio01 import (
    identidade,
    solicita_dados
)

def retorna_keys(dicinario):
    chaves = list(dicinario.keys())
    return chaves

def modifica_item(qual_item, mudanca, dicionario):
    keys_response = retorna_keys(dicionario)

    if qual_item not in keys_response:
        print('Não há esse tipo de dado!')
        return None
    
    dicionario[qual_item] = mudanca

def adicionar_compo(campo, dado, dicionario):
    dicionario[campo] = dado

def deletar_dado(dicionario, dado):
    keys_response = retorna_keys(dicionario)

    if dado not in keys_response:
        print('Não há esse tipo de dado!')
        return None
    
    dado_deletado = dicionario.pop(dado)

    return dado_deletado

# Resolução da quetão.
nome, idade, cidade = solicita_dados()
identidade_response = identidade(nome, idade, cidade)

print(identidade_response)