from cliente import  cadastrar_cliente, alterar_cliente, excluir_cliente, exibir_clientes, login_cliente
from vendedor import cadastrar_vendedor, alterar_vendedor, excluir_vendedor, exibir_vendedores, login_vendedor
from produto import cadastrar_produto, alterar_produto, excluir_produto, exibir_produtos

def menu():
    while True:
        print("\nMenu Principal:")
        print("1 - Gerenciar Clientes")
        print("2 - Gerenciar Vendedores")
        print("3 - Gerenciar Produtos")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_clientes()
        elif opcao == "2":
            menu_vendedores()
        elif opcao == "3":
            menu_produtos()
        elif opcao == "4":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_clientes():
    while True:
        print("\nMenu Clientes:")
        print("1 - Cadastrar cliente")
        print("2 - Alterar cliente")
        print("3 - Excluir cliente")
        print("4 - Exibir clientes")
        print("5 - Login de cliente")
        print("6 - Voltar ao menu principal")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            id_cliente = input("Digite o ID do cliente: ")
            cpf = input("Digite o CPF do cliente: ")
            nome = input("Digite o nome do cliente: ")
            endereco = input("Digite o endereço do cliente: ")
            telefone = input("Digite o telefone do cliente: ")
            senha = input("Digite a senha do cliente: ")
            print(cadastrar_cliente(id_cliente, cpf, nome, endereco, telefone, senha))
        elif opcao == "2":
            id_cliente = input("Digite o ID do cliente para alterar: ")
            cpf = input("Digite o novo CPF (repita o valor caso não queira alterar): ")
            nome = input("Digite o novo nome (repita o valor caso não queira alterar): ")
            endereco = input("Digite o novo endereço (repita o valor caso não queira alterar): ")
            telefone = input("Digite o novo telefone (repita o valor caso não queira alterar): ")
            print(alterar_cliente(id_cliente, cpf or None, nome or None, endereco or None, telefone or None))
        elif opcao == "3":
            id_cliente = input("Digite o ID do cliente para excluir: ")
            print(excluir_cliente(id_cliente))
        elif opcao == "4":
            print(exibir_clientes())
        elif opcao == "5":
            id_cliente = input("Digite o ID do cliente: ")
            senha = input("Digite a senha: ")
            print(login_cliente(id_cliente, senha))
        elif opcao == "6":
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_vendedores():
    while True:
        print("\nMenu Vendedores:")
        print("1 - Cadastrar vendedor")
        print("2 - Alterar vendedor")
        print("3 - Excluir vendedor")
        print("4 - Exibir vendedores")
        print("5 - Login de vendedor")
        print("6 - Voltar ao menu principal")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            id_vendedor = input("Digite o ID do vendedor: ")
            cpf = input("Digite o CPF do vendedor: ")
            nome = input("Digite o nome do vendedor: ")
            endereco = input("Digite o endereço do vendedor: ")
            telefone = input("Digite o telefone do vendedor: ")
            senha = input("Digite a senha do vendedor: ")
            print(cadastrar_vendedor(id_vendedor, cpf, nome, endereco, telefone, senha))
        elif opcao == "2":
            id_vendedor = input("Digite o ID do vendedor para alterar: ")
            cpf = input("Digite o novo CPF (repita o valor caso não queira alterar): ")
            nome = input("Digite o novo nome (repita o valor caso não queira alterar): ")
            endereco = input("Digite o novo endereço (repita o valor caso não queira alterar): ")
            telefone = input("Digite o novo telefone (repita o valor caso não queira alterar): ")
            print(alterar_vendedor(id_vendedor, cpf or None, nome or None, endereco or None, telefone or None))
        elif opcao == "3":
            id_vendedor = input("Digite o ID do vendedor para excluir: ")
            print(excluir_vendedor(id_vendedor))
        elif opcao == "4":
            print(exibir_vendedores())
        elif opcao == "5":
            id_vendedor = input("Digite o ID do vendedor: ")
            senha = input("Digite a senha: ")
            print(login_vendedor(id_vendedor, senha))
        elif opcao == "6":
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_produtos():
    while True:
        print("\nMenu Produtos:")
        print("1 - Cadastrar produto")
        print("2 - Alterar produto")
        print("3 - Excluir produto")
        print("4 - Exibir produtos")
        print("5 - Voltar ao menu principal")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            id_produto = input("Digite o ID do produto: ")
            preco = float(input("Digite o preço do produto: R$ "))
            quantidade = int(input("Digite a quantidade do produto: "))
            print(cadastrar_produto(id_produto, preco, quantidade))
        elif opcao == "2":
            id_produto = input("Digite o ID do produto para alterar: ")
            preco = input("Digite o novo preço (repita o valor caso não queira alterar): ")
            quantidade = input("Digite a nova quantidade (repita o valor caso não queira alterar): ")
            print(alterar_produto(id_produto, float(preco) if preco else None, int(quantidade) if quantidade else None))
        elif opcao == "3":
            id_produto = input("Digite o ID do produto para excluir: ")
            print(excluir_produto(id_produto))
        elif opcao == "4":
            print(exibir_produtos())
        elif opcao == "5":
            break
        else:
            print("Opção inválida. Tente novamente.")

