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
    print("1 - Cadastrar Restaurente")
    print("2 - Listar Restaurente")
    print("3 - Ativar Restaurente")
    print("4 - Sair do Restaurante")

    print('\n')

def entrada_de_dados(mensagem):
    opcao_esolhida = input(mensagem)

    return opcao_esolhida