"""
    Curso: Python: Crie a sua primeira Aplicação
    Diretório: Manipulação de Strings
    Arquivo: exercicio03.py
    Dado: Imprima a palavra: 'ALURA' de modo que cada letra fique em uma linha, como mostrado a seguir:
"""

# Usando um função para realizar esse processo
def imprime_por_linha(mensagem):
    for n in mensagem:
        print(n)


# Testando o desejado.
imprime_por_linha('ALURA')