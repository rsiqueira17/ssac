# classe template para cadastro de  clientes

class SMTP():
    def __init__(self, email, servidor, senha, ssl, tls, porta=587):
        self.email = email
        self.servidor = servidor
        self.porta = porta
        self.senha = senha
        self.ssl = ssl
        self.tls = tls