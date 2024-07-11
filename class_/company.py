# classe template para cadastro de  clientes

class Company():
    def __init__(self, cnpj, razao_social, email, telefone, celular_1, celular_2, cep, endereco, endereco_numero, endereco_complemento, endereco_bairro,
                 endereco_cidade, os_numero_inicial, garantia_km, garantia_tipo, garantia_tempo, logo_arquivo, local_os):
        self.cnpj = cnpj
        self.razao_social = razao_social
        self.email = email
        self.telefone = telefone
        self.celular_1 = celular_1
        self.celular_2 = celular_2
        self.cep = cep
        self.endereco = endereco
        self.endereco_numero = endereco_numero
        self.endereco_complemento = endereco_complemento
        self.endereco_bairro = endereco_bairro
        self.endereco_cidade = endereco_cidade
        self.os_numero_inicial = os_numero_inicial
        self.garantia_km = garantia_km
        self.garantia_tipo = garantia_tipo
        self.garantia_tempo = garantia_tempo
        self.logo_arquivo = logo_arquivo
        self.local_os = local_os