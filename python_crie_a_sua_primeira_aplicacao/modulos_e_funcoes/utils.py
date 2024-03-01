"""
    Curso: Python: Crie a sua primeira Aplicação
    Diretório: Modulos e Funções
    Arquivo: utils.py
    Dado: Função desenvolvidas para auxiliar
"""

def mensagem_principal():
    print("""
        █▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
        ▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█
            
        """)
    
def mensagem_opcoes():
    opcoes = definicao_de_opcoes()
    for key, value in opcoes.items():
        print(f"{key} - {value}")

    print('\n')

    return opcoes

def entrada_de_dados(mensagem):
    opcao_esolhida = input(mensagem)

    return opcao_esolhida

def definicao_de_opcoes():
    opcoes = {
        '1': 'Cadastrar Restaurente',
        '2': 'Listar Restaurentes',
        '3': 'Ativar Restaurante',
        '4': 'Sair do APP.',
    }
    return opcoes

def retorna_as_keys_apenas(opcoes_em_dicionario):
    opcoes = list(opcoes_em_dicionario.keys())
    return opcoes