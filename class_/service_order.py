# classe template para o cadastro de ordens de servico

class Service_Order():
    def __init__(self, numero, data, tecnico, cliente_cpf_cnpj, veiculo_modelo, veiculo_placa, veiculo_versao, veiculo_fabricante, veiculo_ano, 
                 veiculo_kilometragem, aprovada, concluida, valor):
        self.numero = numero
        self.data = data
        self.tecnico = tecnico
        self.cliente_cpf_cnpj = cliente_cpf_cnpj
        self.veiculo_modelo = veiculo_modelo
        self.veiculo_placa = veiculo_placa
        self.veiculo_versao = veiculo_versao
        self.veiculo_fabricante = veiculo_fabricante
        self.veiculo_ano = veiculo_ano
        self.veiculo_kilometragem = veiculo_kilometragem
        self.aprovada = aprovada
        self.concluida = concluida
        self.valor = valor