"""
    Curso: Python: Crie a sua primeira Aplicação
    Diretório: Modulos e Funções
    Arquivo: exercicio01.py
    Dado: Solicite ao usuário que insira um número e,
          em seguida, use uma estrutura if else para determinar se o número é par
          ou ímpar.
"""

# Desenvolvendo função para resolver esse caso:
def par_ou_impar(numero):
    if type(numero) == int or type(numero) == float:
        if numero % 2 == 0:
            print('É um número Par!')
        else:
            print('É um número impar!')

    else:
        print('Não é um número!')

if __name__ == '__main__':
    numero = int(input('Digite um número: '))
    par_ou_impar(numero)