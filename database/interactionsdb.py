# interacoes com o banco de dados
from database.run_sql import run_sql
from class_.client import Client
from class_.service_order import Service_Order
from class_.service_order_item import Service_Order_Item


# checar como setar a time zone do brasil para a funcao currente_timestamp
def create_tab_customer():
    create = """
        CREATE TABLE IF NOT EXISTS clientes (
            cpf_cnpj VARCHAR(14) PRIMARY KEY,
            nome VARCHAR(60),
            celular VARCHAR(14),
            email VARCHAR(40),
            cep VARCHAR(9),
            endereco VARCHAR(60),
            endereco_numero VARCHAR(10),
            endereco_complemento VARCHAR(50),
            endereco_bairro VARCHAR(50),
            endereco_cidade VARCHAR(50),
            data_criacao TIMESTAMP,
            data_alteracao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """

    run_sql(create)

    return


def create_tab_os():
    create = """
        CREATE TABLE IF NOT EXISTS ordens_servico (
            codigo INTEGER PRIMARY KEY,
            numero INTEGER UNIQUE NOT NULL,
            data DATE,
            tecnico VARCHAR(40),
            cliente_cpf_cnpj VARCHAR(14),
            veiculo_modelo VARCHAR(30),
            veiculo_placa VARCHAR(7),
            veiculo_versao VARCHAR(30),
            veiculo_fabricante VARCHAR(30),
            veiculo_ano INTEGER,
            veiculo_kilometragem INTEGER,
            aprovada BOOLEAN,
            concluida BOOLEAN,
            valor REAL,
            data_criacao TIMESTAMP,
            data_alteracao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (
                cliente_cpf_cnpj
            ) REFERENCES clientes (
                cpf_cnpj
            ) ON DELETE RESTRICT
        );
    """

    run_sql(create)

    return


def create_tab_os_items():
    create = """
        CREATE TABLE IF NOT EXISTS ordens_servico_itens (
            os_codigo INTEGER,
            codigo INTEGER,
            descricao VARCHAR(60),
            valor REAL,
            quantidade INTEGER,
            percentual_venda REAL,
            PRIMARY KEY (os_codigo, codigo),
            FOREIGN KEY (
                os_codigo
            ) REFERENCES ordens_servico (
                codigo
            ) ON DELETE CASCADE
        );
    """

    run_sql(create)

    return


def create_tab_company():
    create = """
        CREATE TABLE IF NOT EXISTS empresa (
            cnpj VARCHAR(18) PRIMARY KEY,
            razao_social VARCHAR(60),
            telefone VARCHAR(13),
            celular_1 VARCHAR(14),
            celular_2 VARCHAR(14),
            email VARCHAR(40),
            endereco VARCHAR(60),
            endereco_numero VARCHAR(10),
            endereco_complemento VARCHAR(50),
            endereco_bairro VARCHAR(50),
            endereco_cidade VARCHAR(50),
            endereco_uf VARCHAR(2),
            os_numero_inicial INTEGER,
            garantia_km INTEGER,
            garantia_tipo VARCHAR(7),
            garantia_tipo_tempo INTEGER,
            logo_arquivo VARCHAR(60),
            local_exportacao_os VARCHAR(60),
            data_criacao TIMESTAMP,
            data_alteracao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """

    run_sql(create)

    return


def create_tab_supplier():
    create = """
        CREATE TABLE IF NOT EXISTS fornecedores (
            cpf_cnpj VARCHAR(14) PRIMARY KEY,
            nome VARCHAR(60),
            celular VARCHAR(14),
            email VARCHAR(40),
            endereco VARCHAR(60),
            endereco_numero VARCHAR(10),
            endereco_complemento VARCHAR(50),
            endereco_bairro VARCHAR(50),
            endereco_cidade VARCHAR(50),
            endereco_uf VARCHAR(2),
            data_criacao TIMESTAMP,
            data_alteracao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """

    run_sql(create)

    return


def create_tab_smtp():
    create = """
        CREATE TABLE IF NOT EXISTS smtp (
            email VARCHAR(60),
            servidor VARCHAR(60),
            porta INTERGER,
            senha VARCHAR(30),
            SSL BOOLEAN,
            TSL BOOLEAN,
            data_criacao TIMESTAMP,
            data_alteracao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """

    run_sql(create)

    return


def new_customer(cliente):
    create_tab_customer()

    insert = f"""
        INSERT INTO clientes (
            cpf_cnpj, nome, celular, email, cep, endereco, endereco_numero, endereco_complemento, endereco_bairro, endereco_cidade, data_criacao
        ) 
        VALUES (
            '{cliente.cpf_cnpj}', '{cliente.nome}', '{cliente.celular}', '{cliente.email}', '{cliente.cep}', '{cliente.endereco}', '{cliente.endereco_numero}', 
            '{cliente.endereco_complemento}', '{cliente.endereco_bairro}', '{cliente.endereco_cidade}', CURRENT_TIMESTAMP
        ) ON CONFLICT(cpf_cnpj) DO
        UPDATE SET
            nome = '{cliente.nome}',
            celular = '{cliente.celular}',
            email = '{cliente.email}',
            cep = '{cliente.cep}',
            endereco = '{cliente.endereco}',
            endereco_numero = '{cliente.endereco_numero}',
            endereco_complemento = '{cliente.endereco_complemento}',
            endereco_bairro = '{cliente.endereco_bairro}',
            endereco_cidade = '{cliente.endereco_cidade}',
            data_alteracao = CURRENT_TIMESTAMP
        WHERE
            cpf_cnpj = '{cliente.cpf_cnpj}';
    """

    run_sql(insert)

    return


def new_os(os):
    create_tab_os()
    
    insert = f"""
        INSERT INTO ordens_servico (
            numero, data, tecnico, cliente_cpf_cnpj, veiculo_modelo, veiculo_placa, veiculo_versao, veiculo_fabricante, veiculo_ano, veiculo_kilometragem,
            aprovada, concluida, valor, data_criacao
        )
        VALUES (
            {os.numero}, '{os.data}', '{os.tecnico}', '{os.cliente_cpf_cnpj}', '{os.veiculo_modelo}', '{os.veiculo_placa}', '{os.veiculo_versao}', '{os.veiculo_fabricante}',
            {os.veiculo_ano}, {os.veiculo_kilometragem}, {os.aprovada}, {os.concluida}, {os.valor}, CURRENT_TIMESTAMP
        ) ON CONFLICT(numero) DO
        UPDATE SET
            data = '{os.data}',
            tecnico = '{os.tecnico}',
            cliente_cpf_cnpj = '{os.cliente_cpf_cnpj}',
            veiculo_modelo = '{os.veiculo_modelo}',
            veiculo_placa = '{os.veiculo_placa}',
            veiculo_versao = '{os.veiculo_versao}',
            veiculo_fabricante = '{os.veiculo_fabricante}',
            veiculo_ano = {os.veiculo_ano},
            veiculo_kilometragem = {os.veiculo_kilometragem},
            aprovada = {os.aprovada},
            concluida = {os.concluida},
            valor = {os.valor},
            data_alteracao = CURRENT_TIMESTAMP
        WHERE
            numero = {os.numero}
        RETURNING
            codigo;
    """

    data = run_sql(insert)[0][0]

    return data


def new_os_item(os_item):
    create_tab_os_items()

    insert = f"""
        INSERT INTO ordens_servico_itens VALUES (
            {os_item.codigo_os}, {os_item.codigo}, '{os_item.descricao}', {os_item.valor}, {os_item.quantidade}, {os_item.percentual_venda}
        );
    """

    run_sql(insert)

    return


def update_customer(cliente):
    update = f"""
        UPDATE
            clientes
        SET
            nome = {cliente.nome},
            celular = {cliente.celular},
            email = {cliente.email},
            endereco = {cliente.endereco},
            endereco_numero = {cliente.endereco_numero},
            endereco_complemento = {cliente.endereco_complemento},
            endereco_bairro = {cliente.endereco_bairro},
            endereco_cidade = {cliente.endereco_cidade},
            endereco_uf = {cliente.endereco_uf},
            data_alteracao = CURRENT_TIMESTAMP
        WHERE
            cpf_cnpj = {cliente.cpf_cnpj}
    """

    run_sql(update)

    return


def update_os(os):
    update = f"""
        UPDATE
            ordens_servico
        SET
            data = {os.data},
            cliente_cpf_cnpj = {os.cliente_cpf_cnpj},
            veiculo_modelo = {os.veiculo_modelo},
            veiculo_placa = {os.veiculo_placa},
            veiculo_versao = {os.veiculo_versao},
            veiculo_fabricante = {os.veiculo_fabricante},
            veiculo_ano = {os.veiculo_ano},
            veiculo_kilometragem = {os.veiculo_kilometragem},
            orcamento = {os.orcamento},
            valor = {os.valor},
            data_alteracao = CURRENT_TIMESTAMP
        WHERE
            numero = {os.numero}
    """

    run_sql(update)

    return


def update_os_item(os_item):
    update = f"""
        UPDATE
            ordens_servico_itens
        SET
            descricao = {os_item.descricao},
            valor = {os_item.valor},
            quantidade = {os_item.quantidade},
        WHERE
            os_codigo = {os_item.os_codigo},
            codigo = {os_item.codigo}
    """

    run_sql(update)

    return


def get_customer(cpf_cnpj):
    select = f"""
        SELECT
            *
        FROM
            clientes
        WHERE
            cpf_cnpj = {cpf_cnpj}
    """

    data = Client(*run_sql(select))

    return data


def get_customers():
    select = """
        SELECT
            *
        FROM
            clientes
    """
    
    data = []

    for cliente in run_sql(select):
        data.append(Client(*cliente))

    return data


def get_os(numero):
    select = f"""
        SELECT
            *
        FROM
            ordens_servico
        WHERE
            numero = {numero}
    """

    data = Service_Order(*run_sql(select))

    return data


def get_oss():
    select = """
        SELECT
            *
        FROM
            ordens_servico
    """

    data = []
    
    for os in run_sql(select):
        data.append(Service_Order(*os))

    return data


def get_os_item(numero, item):
    select = f"""
        SELECT
            *
        FROM
            ordens_servico_itens
        INNER JOIN (
            SELECT
                *
            FROM
                ordens_servico
            WHERE
                numero = {numero}
        )
        WHERE
            codigo = {item}
    """

    data = Service_Order_Item(*run_sql(select))

    return data


def get_os_items(numero):
    select = f"""
        SELECT
            *
        FROM
            ordens_servico_itens
        INNER JOIN (
            SELECT
                *
            FROM
                ordens_servico
            WHERE
                numero = {numero}
        )
    """

    data = []
    
    for os_itens in run_sql(select):
        data.append(Service_Order_Item(*os_itens))

    return data