# classe template para cadastro de  clientes

class Company():
    def __init__(self, cnpj, razao_social, telefone, celular_1, celular_2, email, endereco, endereco_numero, endereco_complemento, endereco_bairro,
                 endereco_cidade, endereco_uf, os_numero_inicial, garantia_km, garantia_tipo, garantia_tempo, logo_arquivo):
        self.cpf_cnpj = cnpj
        self.razao_social = razao_social
        self.telefone = telefone
        self.celular_1 = celular_1
        self.celular_2 = celular_2
        self.email = email
        self.endereco = endereco
        self.endereco_numero = endereco_numero
        self.endereco_complemento = endereco_complemento
        self.endereco_bairro = endereco_bairro
        self.endereco_cidade = endereco_cidade
        self.endereco_uf = endereco_uf
        self.os_numero_inicial = os_numero_inicial
        self.garantia_km = garantia_km
        self.garantia_tipo = garantia_tipo
        self.garantia_tempo = garantia_tempo
        self.logo_arquivo = logo_arquivo