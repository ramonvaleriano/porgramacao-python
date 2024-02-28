"""
    Curso: Python: Crie a sua primeira Aplicação
    Diretório: Modulos e Funções
    Arquivo: exercicio03.py
    Dado: Solicite um nome de usuário e uma senha e use uma estrutura if else para
          verificar se o nome de usuário e a senha fornecidos correspondem aos
          valores esperados determinados por você.
"""

# Desenvolvendo função para resolver esse caso:
def definindo_senha_e_login(senha, login):
    login_completo = {
        'senha': senha,
        'login': login
    }

    print(login_completo)

    return login_completo

def valida_senha_e_login(senha, login, login_completo):
    if senha != login_completo['senha'] and login != login_completo['login']:
        print('Senha o login errados.')
    
    elif senha != login_completo['senha'] and login == login_completo['login']:
        print('Senha incorreta.')

    elif senha == login_completo['senha'] and login != login_completo['login']:
        print('Login incorreta.')

    else:
        print('Senha e login corretos!')

if __name__ == '__main__':
    login = input('Qual o login desejado: ')
    senha = input('Qual a senha desejada: ')

    login_completo = definindo_senha_e_login(senha, login)

    login = input('Qual o login desejado: ')
    senha = input('Qual a senha desejada: ')

    valida_senha_e_login(senha, login, login_completo)
