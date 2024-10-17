clientes = {}

def cadastrar_cliente(id_cliente, cpf, nome, endereco, telefone, senha):
    if id_cliente in clientes:
        return "Cliente já cadastrado."
    clientes[id_cliente] = {
        "cpf": cpf,
        "nome": nome,
        "endereco": endereco,
        "telefone": telefone,
        "senha": senha
    }
    return "Cliente cadastrado com sucesso."

def alterar_cliente(id_cliente, cpf=None, nome=None, endereco=None, telefone=None):
    if id_cliente not in clientes:
        return "Cliente não encontrado."
    if cpf:
        clientes[id_cliente]["cpf"] = cpf
    if nome:
        clientes[id_cliente]["nome"] = nome
    if endereco:
        clientes[id_cliente]["endereco"] = endereco
    if telefone:
        clientes[id_cliente]["telefone"] = telefone
    return "Cliente alterado com sucesso."

def excluir_cliente(id_cliente):
    if id_cliente in clientes:
        del clientes[id_cliente]
        return "Cliente deletado."
    return "Cliente não encontrado."

def exibir_clientes():
    if not clientes:
        return "Nenhum cliente cadastrado."
    return "\n".join([
        f"ID: {id_}, CPF: {info['cpf']}, Nome: {info['nome']}, Endereço: {info['endereco']}, Telefone: {info['telefone']}"
        for id_, info in clientes.items()
    ])

def login_cliente(id_cliente, senha):
    if id_cliente in clientes and clientes[id_cliente]["senha"] == senha:
        return "Login realizado com sucesso!"
    return "ID ou senha incorretos."
