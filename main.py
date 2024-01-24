import json
from os import name, system
from pathlib import Path

from assets import cpf_checker


class Client:
    def __init__(self, id, name, cpf, password):
        self._id = id
        self._name = name
        self._cpf = cpf
        self._password = password


class System:
    SAVE_TO = Path(__file__).parent / "data" / "data.json"

    @classmethod
    def create_json(cls, clients):
        with open(cls.SAVE_TO, "w") as arquivo:
            json.dump(clients, arquivo, indent=4)

    @classmethod
    def read_json(cls):
        with open(cls.SAVE_TO, "r") as file:
            return json.load(file)

    @classmethod
    def read_id_json(cls):
        try:
            with open(cls.SAVE_TO, "r") as file:
                x = json.load(file)
                for index in x:
                    if index == 1:
                        return int(index)
                    else:
                        return int(index) + 1
        except Exception:
            return 1

    @classmethod
    def update_json(cls, clients):
        try:
            clients.update(System.read_json())
        except FileNotFoundError:
            pass

    @classmethod
    def delete_json(cls, cpf):
        data = System.read_json()

        id_to_delete = None
        for id, valor in data.items():
            if "cpf" in valor and valor["cpf"] == cpf:
                id_to_delete = id
                break

        if id_to_delete is not None:
            del data[id_to_delete]
            System.create_json(data)

    @classmethod
    def clear(cls):
        if name == 'nt':  # Windows
            _ = system('cls')
        else:  # Mac/Linux
            _ = system('clear')

    @classmethod
    def interface(cls, var):
        System.clear()
        print(f'{"=-=" * 10}\n{var.upper(): ^30}\n{"=-=" * 10}')


while True:
    System.interface('Sistema de cadastro de clientes')
    print('1-Login')
    print('2-Cadastrar Usuário')
    print('3-Sair')

    init = input('Escolha uma opção: ')

    if init.isdigit():
        init = int(init)
        if init < 1 or init > 3:
            System.clear()
            print('Escolha uma das opções disponiveis\n')
            input("Pressione ENTER para continuar ")
    else:
        System.clear()
        print('Coloque uma opção válida\n')
        input("Pressione ENTER para continuar ")

    # Checar se o user existe no data e logar, lá dentro poder deletar o user
    if init == 1:
        System.interface('Login')

        cpf_login = input("CPF: ")
        password_login = input("Password: ")

        # Checagem dos dados para efetuar o login
        for chave, valor in System.read_json().items():
            if "cpf" in valor and valor["cpf"] == cpf_login:
                if "password" in valor and valor["password"] == password_login:
                    System.interface("Menu")
                    print('1-Deletar Usuario')

                    menu = input('Escolha uma opção: ')

                    if menu.isdigit():
                        menu = int(menu)
                        if menu != 1:
                            System.clear()
                            print('Escolha uma das opções disponiveis\n')
                            input("Pressione ENTER para continuar ")
                    else:
                        System.clear()
                        print('Coloque uma opção válida\n')
                        input("Pressione ENTER para continuar ")

                    if menu == 1:
                        print("Deletar o user")
                        cpf_delete = input("Qual cpf deseja deletar ")

                        System.delete_json(cpf_delete)
                        input()

    if init == 2:
        System.interface('Cadastrar Usuário')

        client_id = System.read_id_json()
        name_register = input("Nome: ")
        cpf_register = input("CPF: ")
        password_register = input("Password: ")

        # Checagem para ver se existe o CPF que deseja cadastrar
        if cpf_checker.check(cpf_register) is True:
            try:
                for chave, valor in System.read_json().items():
                    if "cpf" in valor and valor["cpf"] == cpf_register:
                        print("CPF Existe")
                        input("Pressione ENTER para continuar ")
                    else:
                        client_dados = Client(
                            client_id, name_register,
                            cpf_register, password_register)

                        clientes_dict = {cliente._id:
                                         {"name": cliente._name,
                                          "cpf": cliente._cpf,
                                          "password": cliente._password}
                                         for cliente in [client_dados]}

                        System.update_json(clientes_dict)
                        System.create_json(clientes_dict)

                        print("Dados cadastrados")
                        input("Pressione ENTER para continuar ")

            except FileNotFoundError:
                client_dados = Client(
                    client_id, name_register, cpf_register, password_register)

                clientes_dict = {cliente._id:
                                 {"name": cliente._name,
                                  "cpf": cliente._cpf,
                                  "password": cliente._password}
                                 for cliente in [client_dados]}

                System.update_json(clientes_dict)
                System.create_json(clientes_dict)

                print("Dados cadastrados")
                input("Pressione ENTER para continuar ")

        else:
            print("CPF Inválido")
            input("Pressione ENTER para continuar ")

    if init == 3:
        print('Saindo!')
        break
