"""
    Curso: Python: Crie a sua primeira Aplicação
    Diretório: Lista, laços e exeções
    Arquivo: exercicio07.py
    Dado: Construa um código que calcule a média dos valores em uma lista.
          Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.
"""

from Exercicio06 import (
    soma_todos_numero
)

# Funções para resolver os exercícios:
def media(soma, lista_numeros):
    media = 0

    if soma == 0 and len(lista_numeros) == 0:
        return media

    quantidade = len(lista_numeros)

    if soma > 0:
        try:
            media = soma / quantidade
        except:
            print('Não foi possivel fazer essa média')
            return None
    
    return media
            

# Testando solução.
lista_numeros = list(range(2, 38, 3))
print(lista_numeros)
soma_total = soma_todos_numero(lista_numeros)
print(soma_total)
media_numeros = media(soma_total, lista_numeros)
print(f"{media_numeros:.2f}")