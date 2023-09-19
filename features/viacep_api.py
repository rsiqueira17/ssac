# algoritmo para captura de dos dados de ceps para incremento no array de dados_cep
import requests
import json


# captura do cep
def get(cep):
    cep = str(cep).strip().replace('-','').replace('.','').zfill(8)

    # captura dos dados via API viacep
    endereco = requests.get("https://viacep.com.br/ws/%s/json/" % cep)

    try:
        retorno = json.loads(endereco.text)
    except Exception:
        raise ValueError(f'Formato de cep inválido: "{cep}"' )
        
    if endereco.status_code == requests.codes.ok and 'erro' not in retorno:
        cidade = retorno['localidade']
        bairro = retorno['bairro'] if retorno['bairro'] != '' else None
        complemento = retorno['complemento'] if retorno['complemento'] != '' else None
        endereco_completo = str(retorno['logradouro']).split()

        try:
            logradouro = endereco_completo[0]
            descricao_endereco = ' '.join(endereco_completo[1:])
                
        except IndexError:
            logradouro = None
            descricao_endereco = retorno['logradouro'] if retorno['logradouro'] != '' else None

        dados_cep = [cep, logradouro, descricao_endereco, bairro, cidade, retorno['uf'], complemento]

        return dados_cep

    return 'Cep não encontrado'
