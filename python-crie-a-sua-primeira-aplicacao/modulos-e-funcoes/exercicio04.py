"""
    Curso: Python: Crie a sua primeira Aplicação
    Diretório: Modulos e Funções
    Arquivo: exercicio04.py
    Dado: Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma
          estrutura if elif else para determinar em qual quadrante do plano cartesiano
          o ponto se encontra de acordo com as seguintes condições:

            Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
            Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
            Terceiro Quadrante: os valores de x e y devem ser menores que zero;
            Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
Caso contrário: o ponto está localizado no eixo ou origem.
"""

# Desenvolvendo função para resolver esse caso:
def definincdo_quadrante(x, y):
    if x > 0 and y > 0:
        print('1° Quadrante')

    elif x < 0 and y > 0:
        print('2° Quadrante')

    elif x < 0 and y < 0:
        print('3° Quadrante')

    elif x > 0 and y < 0:
        print('4° Quadrante')
    
    else:
        print('Ponto está na origem')

if __name__ == '__main__':
    x = float(input('Digite o x: '))
    y = float(input('Digite o y: '))
    definincdo_quadrante()
