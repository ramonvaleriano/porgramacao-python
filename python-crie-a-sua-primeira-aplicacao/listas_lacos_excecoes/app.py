from ..modulos_e_funcoes.utils import (
    mensagem_principal,
    entrada_de_dados,
    mensagem_opcoes,
)

from ..modulos_e_funcoes.validadores import (
    valida_opcoes,
    valida_inteiro
)

from ..modulos_e_funcoes.controllers import (
    controle_de_opcoes
)


def main():
    mensagem_principal()
    mensagem_opcoes()

    opcao_esolhida = entrada_de_dados("Digte a opção desejada: ")
    opcao_esolhida = valida_inteiro(opcao_esolhida)

    opcoes = [1, 2, 3, 4]
    
    validacao_das_opcoes = valida_opcoes(opcoes, opcao_esolhida)

    controle_de_opcoes(opcao_esolhida, validacao_das_opcoes)

if __name__ == '__main__':
    main()