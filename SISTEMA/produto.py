produtos = {}

def cadastrar_produto(id_produto, preco, quantidade):
    if id_produto in produtos:
        return "Produto já esta cadastrado."
    produtos[id_produto] = {
        "preco": preco,
        "quantidade": quantidade
    }
    return "Produto cadastrado com sucesso."

def alterar_produto(id_produto, preco=None, quantidade=None):
    if id_produto not in produtos:
        return "Produto não encontrado."
    if preco is not None:
        produtos[id_produto]["preco"] = preco
    if quantidade is not None:
        produtos[id_produto]["quantidade"] = quantidade
    return "Produto alterado com sucesso."

def excluir_produto(id_produto):
    if id_produto in produtos:
        del produtos[id_produto]
        return "Produto deletado."
    return "Produto não encontrado."

def exibir_produtos():
    if not produtos:
        return "Nenhum produto cadastrado."
    return "\n".join([
        f"ID: {id_}, Preço: R${info['preco']:.2f}, Quantidade: {info['quantidade']}"
        for id_, info in produtos.items()
    ])
