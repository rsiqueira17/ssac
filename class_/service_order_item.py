# classe template para cadastro de itens de ordens de servivo

class Service_Order_Item():
    def __init__(self, codigo_os, codigo, descricao, valor, quantidade, percentual_venda=0):
        self.codigo_os = codigo_os
        self.codigo = codigo
        self.descricao = descricao
        self.valor = valor
        self.quantidade = quantidade
        self.percentual_venda = percentual_venda