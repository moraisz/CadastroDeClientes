user = []
password = []
cpf = []
while True:
    def lin(var):  # def para cabeçalho
        print(f'{"=-=" * 10}\n{var.upper():^30}\n{"=-=" * 10}')


    lin('Sistema de cadastro de clientes')
    print('1-Login')
    print('2-Cadastrar Usuário')
    print('3-Sair')

    init = input('Escolha uma opção: ')

    if init.isdigit():
        init = int(init)
        if init < 1 or init > 4:
            print('Escolha uma das opções disponiveis')
    else:
        print('Coloque uma opção válida')

    if init == 1:
        lin('Login')
        user_temp = input('Usuário: ')
        pass_temp = input('Senha: ')
        if user_temp not in user:
            print('Usuário não cadastrado')
            continue
        for i, valor in enumerate(user):
            if valor == user_temp and pass_temp == password[i]:
                print('Usuário logado')
                u1 = 'verdadero'
            else:
                print('Usuário ou Senha inválidos!')
                break  # não da pra usar continue aqui, e não consegui pensar em nada para reiniciar o loop

        lin('Menu')
        print('1-Deletar Conta')

        menu = input('Escolha uma opção: ')
        if menu.isdigit():
            menu = int(menu)
            if menu != 1:
                print('Escolha uma das opções disponiveis')
        else:
            print('Coloque uma opção válida')

        if menu == 1:

            lin('Deletar Usuário')
            del_cpf = input('Informe seu CPF: ')
            if del_cpf in cpf:
                print('Usuário encontrado')
            else:
                print('Cpf inválido')
                continue
            del_pass = input('Informe sua senha: ')
            del_pass2 = input('Confirme a senha: ')

            if del_pass != del_pass2:
                print('As senhas são diferentes')
                continue

            if del_pass2 and del_pass not in password:
                print('Senha incorreta!')
                continue

            del_confim = input('Tem certeza que deseja deletar a conta? (S/N) ').upper()

            if del_confim == 'S':  # deleta o user, password e cpf
                for i, valor in enumerate(cpf):
                    if valor == del_cpf and password[i] == del_pass:
                        del (user[i])
                        del (password[i])
                        del (cpf[i])
                        print('Usuário deletado!')

            if del_confim == 'N':
                print('Cancelando!')
                continue

            else:
                print('Opção inválida, tente novamente')
                continue

    if init == 2:
        lin('Cadastrar Usuário')
        cpf_cad = input('CPF do usuário (somente números): ')
        if cpf_cad in cpf:  # checar se o CPF já foi cadastrado
            print('CPF já cadastrado')
            continue
        elif cpf_cad.isdigit():
            pass
        else:
            print('Coloque somente números')
            continue

        cpf_new = cpf_cad[:-2]  # checar se o CPF é verdadeiro
        cpf_temp = ''
        multi1 = 10
        multi2 = 11
        result1 = 0
        result2 = 0

        for x in cpf_new:
            k = int(x)
            cpf_temp += x
            if multi1 <= 10:
                num1 = k * multi1
                result1 += num1
                multi1 -= 1
        d1 = (result1 * 10) % 11
        cpf_temp += str(d1)

        for y in cpf_temp:
            o = int(y)
            if multi2 <= 11:
                num2 = o * multi2
                result2 += num2
                multi2 -= 1
        d2 = (result2 * 10) % 11
        cpf_temp += str(d2)

        seq = cpf_cad == (cpf_cad[0]) * len(cpf_cad)  # evita sequências como "11111111111"

        if cpf_cad == cpf_temp and not seq:
            print('CPF válido')
        else:
            print('CPF inválido!')
            continue

        user_cad = input('Usuário para ser cadastrado:(Palavra com 6 caractéres, sem números): ')

        if user_cad in user:  # checar se o user existe
            print('Usuário já existe, tente outro')
            continue

        if any(x.isnumeric() for x in user_cad):  # checar se tem número no user
            print('Escreva um usuário sem número')
            continue

        if any(x == ' ' for x in user_cad):  # checar se tem espaço em branco no user
            print('Há um espaço em branco no usuário')
            continue

        u_cad_len = len(user_cad)  # checar se tem 6 caractéres no user
        if u_cad_len < 6 or u_cad_len > 6:
            print('Formato errado, usuário tem que ter 6 caractéres')
            continue

        pass_cad = input('Senha para ser cadastrada:(Senha tem que conter 6 caractéres): ')

        if any(x == ' ' for x in pass_cad):  # checar se tem espaço em branco na senha
            print('Há um espaço em branco na senha')
            continue

        u_pass_len = len(pass_cad)  # checar se tem 6 caractéres no password
        if u_pass_len < 6 or u_pass_len > 6:
            print('Formato errado, a senha tem que ter 6 caractéres')
            continue
        else:
            cpf.append(cpf_cad)
            user.append(user_cad)
            password.append(pass_cad)
            print('Usuário Cadastrado!')

    if init == 3:
        print('Saindo!')
        break
