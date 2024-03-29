from modulos_e_funcoes.utils import (
    retorna_as_keys_apenas,
    mensagem_principal,
    entrada_de_dados,
    mensagem_opcoes
)

from modulos_e_funcoes.validadores import (
    valida_opcoes,
    valida_inteiro
)

from modulos_e_funcoes.controllers import (
    controle_de_opcoes
)


def main():
    mensagem_principal()
    retorno_opcoes = mensagem_opcoes()
    opcoes = retorna_as_keys_apenas(retorno_opcoes)

    manter_app = True
    while manter_app:
        opcao_esolhida = entrada_de_dados("Digte a opção desejada: ")
        opcao_esolhida = valida_inteiro(opcao_esolhida)
        
        validacao_das_opcoes = valida_opcoes(opcoes, opcao_esolhida)

        lista_restaurantes = list()

        controle_de_opcoes(opcao_esolhida, validacao_das_opcoes, lista_restaurantes)
        
        if opcao_esolhida == 4:
            manter_app = False

if __name__ == '__main__':
    main()