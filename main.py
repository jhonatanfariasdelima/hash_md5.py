from hashlib import md5


def linhas():
    print('==' * 20)


def cadastrar():
    nome = str(input('digite seu nome: '))
    nomemd5 = md5(nome.encode()).hexdigest()  # hash nome

    cpf = input('digite seu cpf sem pontos: ')
    cpfmd5 = md5(str(cpf).encode()).hexdigest()  # hash cpf

    senha = input('digite sua senha: ')
    senha += nome  # concatena o nome da pessoa a senha
    senhamd5 = md5(str(senha).encode()).hexdigest()  # hash senha 1 = senha
    senhamd5final = md5(str(senhamd5 + cpfmd5).encode()).hexdigest()  # hash senha 2 = hash senha 1 + hash cpf

    total = nomemd5 + '|' + cpfmd5 + '|' + senhamd5final
    with open('../valores.txt', 'w') as arquivo:  # armazena as informações do usuario em um txt
        arquivo.write(str(total) + '\n')
        arquivo.close()
        linhas()


def autenticar():
    autentica_nome = str(input('digite seu nome: '))
    autentica_nomemd5 = md5(autentica_nome.encode()).hexdigest()  # hash nome

    autentica_cpf = input('digite seu cpf sem pontos: ')
    autentica_cpfmd5 = md5(str(autentica_cpf).encode()).hexdigest()  # hash cpf

    autentica_senha = input('digite sua senha: ')
    autentica_senha += autentica_nome  # concatena o nome da pessoa a senha
    autentica_senhamd5 = md5(str(autentica_senha).encode()).hexdigest()  # hash senha 1 = senha
    autentica_senhamd5final = md5(str(autentica_senhamd5 + autentica_cpfmd5).encode()).hexdigest()  # hash senha 2 = hash senha 1 + hash cpf

    autentica_total = autentica_nomemd5 + '|' + autentica_cpfmd5 + '|' + autentica_senhamd5final

    with open('../valores.txt', 'r') as arquivo:  # procura as informações no arquivo txt usado na função cadastrar

        for linha in arquivo:

            if str(autentica_total + '\n') in linha:
                print('\033[1;33m usuario autenticado!\033[m')

            else:
                print('\033[1;31musuario não cadastrado\033[m')
        linhas()


while True:
    # menu de opções
    print('[1] cadastrar\n'
          '[2] autenticar\n'
          '[3] sair\n')
    opcao = str(input('o que você deseja fazer?'))

    if opcao == '1':
        cadastrar()  # cadastrar um usuário, aplicar a função de hash md5 e armazenar em um arquivo de texto 

    if opcao == '2':  # verificar se o usuário em questão esta cadastrado no arquivo de texto 
        autenticar()

    if opcao == '3':  # sair
        break

print('programa encerrado')
