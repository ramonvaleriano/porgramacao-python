"""
    Curso: Python: Crie a sua primeira Aplicação
    Diretório: Lista, laços e exeções
    Arquivo: exercicio06.py
    Dado: Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos.
          Utilize um bloco try-except para lidar com possíveis exceções.
"""

# Funções para resolver os exercícios:
def validador_de_numero(possivel_numero):
    try:
        numero = float(possivel_numero)
        
        return numero
    
    except:
        print('Não é um número.')
        return False


def soma_todos_numero(lista_numeros):
    soma = 0
    for possivel_numero in lista_numeros:
        numero = validador_de_numero(possivel_numero)
        
        if not numero:
            continue
        
        soma += numero

    return numero

# Testando solução.
lista_numeros = list(range(2, 38, 3))
print(lista_numeros)
soma_total = soma_todos_numero(lista_numeros)
print(soma_total)