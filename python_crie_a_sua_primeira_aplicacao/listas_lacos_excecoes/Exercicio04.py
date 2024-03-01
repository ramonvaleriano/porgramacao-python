"""
    Curso: Python: Crie a sua primeira Aplicação
    Diretório: Lista, laços e exeções
    Arquivo: exercicio04.py
    Dado: Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.
"""

# Funções para resolver os exercícios:
def imprimir_decrescente(lista_de_dados):
    agregador = -1
    for dado in range(len(lista_de_dados), 0, agregador):
        print(f"{dado}")

# Testando solução.
lista_dados = list(range(1,11))
imprimir_decrescente(lista_dados)