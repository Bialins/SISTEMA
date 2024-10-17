vendedores = {}

def cadastrar_vendedor(id_vendedor, cpf, nome, endereco, telefone, senha):
    if id_vendedor in vendedores:
        return "Vendedor já cadastrado."
    vendedores[id_vendedor] = {
        "cpf": cpf,
        "nome": nome,
        "endereco": endereco,
        "telefone": telefone,
        "senha": senha
    }
    return "Vendedor caddastrado com sucesso."

def alterar_vendedor(id_vendedor, cpf=None, nome=None, endereco=None, telefone=None):
    if id_vendedor not in vendedores:
        return "Vendedor não encontrado."
    if cpf:
        vendedores[id_vendedor]["cpf"] = cpf
    if nome:
        vendedores[id_vendedor]["nome"] = nome
    if endereco:
        vendedores[id_vendedor]["endereco"] = endereco
    if telefone:
        vendedores[id_vendedor]["telefone"] = telefone
    return "Vendedor alterado com sucesso."

def excluir_vendedor(id_vendedor):
    if id_vendedor in vendedores:
        del vendedores[id_vendedor]
        return "Vendedor deletado."
    return "Vendedor não encontrado."

def exibir_vendedores():
    if not vendedores:
        return "Nenhum vendedor cadastrado."
    return "\n".join([
        f"ID: {id_}, CPF: {info['cpf']}, Nome: {info['nome']}, Endereço: {info['endereco']}, Telefone: {info['telefone']}"
        for id_, info in vendedores.items()
    ])

def login_vendedor(id_vendedor, senha):
    if id_vendedor in vendedores and vendedores[id_vendedor]["senha"] == senha:
        return "Login realizado com sucesso!"
    return "ID ou senha incorretos."
