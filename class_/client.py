# classe template para cadastro de  clientes

class Client():
    def __init__(self, cpf_cnpj, nome, celular, email, cep, endereco, endereco_numero, endereco_complemento, endereco_bairro, endereco_cidade):
        self.cpf_cnpj = cpf_cnpj
        self.nome = nome
        self.celular = celular
        self.email = email
        self.cep = cep
        self.endereco = endereco
        self.endereco_numero = endereco_numero
        self.endereco_complemento = endereco_complemento
        self.endereco_bairro = endereco_bairro
        self.endereco_cidade = endereco_cidade