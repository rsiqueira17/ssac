import webbrowser
import database.interactionsdb as db
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor
#from reportlab.lib.styles import ParagraphStyle
#from reportlab.platypus import Paragraph, Table



class Pdf():
    def __init__(self, nome_arquivo):
        # hyperparametros        
        self.pdfnomearq = nome_arquivo
        self.pdfarq = canvas.Canvas(nome_arquivo)
        
        self.txt = self.pdfarq.beginText()
        self.txt.setCharSpace(1) # define o espaçamento entre as letras da string

        self.offsetx = self.mm2p(10) # variavel que armazena a dimensão da margem rodape em pontos
        self.offsety = self.mm2p(8) # variavel que armazena a dimensão da margem lateral em pontos
        self.largfol = self.mm2p(210) # variavel que armazena a dimensão da folha vertical em pontos
        self.altfol = self.mm2p(287) # variavel que armazena a dimensão da folha horizontal em pontos

        self.largquadro = self.mm2p(194)
        
        self.nextpos = self.mm2p(1) # variavel que armazena a posicao inicial da proxima palavra
        self.posxcent = self.mm2p(207/2) # centro da pagina na vertical
        self.posycent = self.mm2p(293/2) # centro da pagina na horizontal
        
        self.posinicorpo = 187.1


    def layoutOS(self):
        ## layout
        # cabecalho estabelecimento
        self.pdfarq.rect(self.mm2p(70), self.mm2p(248), self.mm2p(70), self.mm2p(15))
        self.pdfarq.rect(self.mm2p(140), self.mm2p(248), self.mm2p(62), self.mm2p(15))
        self.pdfarq.rect(self.offsety, self.mm2p(248), self.largquadro, self.mm2p(40))
        
        self.pdfarq.setFont("Courier-Bold", 15)
        self.pdfarq.drawString(self.mm2p(99), self.mm2p(258), 'Data')
        self.pdfarq.setFont("Courier-Bold", 15)
        self.pdfarq.drawString(self.mm2p(167), self.mm2p(258), 'OS')
        
        # cliente
        self.pdfarq.rect(self.offsety, self.mm2p(202), self.largquadro, self.mm2p(42))
        self.pdfarq.rect(self.offsety, self.mm2p(202), self.largquadro, self.mm2p(16))

        self.pdfarq.setFont("Courier", 10)
        self.pdfarq.drawString(self.offsety + self.mm2p(3), self.mm2p(240), 'Cliente: ')
        self.pdfarq.drawString(self.offsety + self.mm2p(115), self.mm2p(240), 'CPF: ')
        self.pdfarq.drawString(self.offsety + self.mm2p(3), self.mm2p(235), 'Telefone: ')
        self.pdfarq.drawString(self.offsety + self.mm2p(75), self.mm2p(235), 'Telefone: ')
        self.pdfarq.drawString(self.offsety + self.mm2p(3), self.mm2p(230), 'Endereço: ')
        self.pdfarq.drawString(self.offsety + self.mm2p(115), self.mm2p(230), 'n°: ')
        self.pdfarq.drawString(self.offsety + self.mm2p(3), self.mm2p(225), 'Complemento: ')
        self.pdfarq.drawString(self.offsety + self.mm2p(3), self.mm2p(220), 'Bairro: ')
        self.pdfarq.drawString(self.offsety + self.mm2p(75), self.mm2p(220), 'Cidade: ')

        self.pdfarq.setFont("Courier-Bold", 10)
        self.pdfarq.drawString(self.offsety + self.mm2p(3), self.mm2p(214.5), 'Veiculo:')

        self.pdfarq.setFont("Courier", 10)
        self.pdfarq.drawString(self.offsety + self.mm2p(3), self.mm2p(209.5), 'Marca/Modelo:')
        self.pdfarq.drawString(self.offsety + self.mm2p(102), self.mm2p(209.5), 'Placa:')
        self.pdfarq.drawString(self.offsety + self.mm2p(3), self.mm2p(204.5), 'Ano:')
        self.pdfarq.drawString(self.offsety + self.mm2p(102), self.mm2p(204.5), 'Kilometragem:')
        
        # corpo
        self.pdfarq.rect(self.offsety, self.mm2p(191), self.mm2p(20), self.mm2p(7))
        self.pdfarq.rect(self.mm2p(28), self.mm2p(191), self.mm2p(100), self.mm2p(7))
        self.pdfarq.rect(self.mm2p(128), self.mm2p(191), self.mm2p(37), self.mm2p(7))
        self.pdfarq.rect(self.mm2p(165), self.mm2p(191), self.mm2p(37), self.mm2p(7))
        self.pdfarq.rect(self.offsety, self.mm2p(63), self.mm2p(97), self.mm2p(7))
        self.pdfarq.rect(self.mm2p(105), self.mm2p(63), self.mm2p(97), self.mm2p(7))
        self.pdfarq.rect(self.offsety, self.mm2p(56), self.mm2p(157), self.mm2p(7))
        self.pdfarq.rect(self.mm2p(165), self.mm2p(56), self.mm2p(37), self.mm2p(7))
        self.pdfarq.rect(self.offsety, self.mm2p(56), self.largquadro, self.mm2p(142))

        self.pdfarq.setFont("Courier-Bold", 11)
        self.pdfarq.drawString(self.offsety + self.mm2p(6), self.mm2p(193.3), 'Qtd')
        self.pdfarq.drawString(self.offsety + self.mm2p(48), self.mm2p(193.3), 'Produtos / Serviços')
        self.pdfarq.drawString(self.offsety + self.mm2p(123), self.mm2p(193.3), 'Val. Unitário')
        self.pdfarq.drawString(self.offsety + self.mm2p(163), self.mm2p(193.3), 'Valor total')
        self.pdfarq.drawString(self.offsety + self.mm2p(3), self.mm2p(65.5), 'Total produtos: R$ ')
        self.pdfarq.drawString(self.offsety + self.mm2p(100), self.mm2p(65.5), 'Total mão de obra: R$ ')
        self.pdfarq.drawString(self.offsety + self.mm2p(124), self.mm2p(58.3), 'Total geral:')
        self.pdfarq.drawString(self.offsety + self.mm2p(159), self.mm2p(58.3), 'R$ ')

        # executado
        self.pdfarq.rect(self.offsety, self.mm2p(45), self.largquadro, self.mm2p(7))
        
        self.pdfarq.setFont("Courier-Bold", 10)
        self.pdfarq.drawString(self.offsety + self.mm2p(2), self.mm2p(47.5), 'Executado por:')
        self.pdfarq.drawString(self.offsety + self.mm2p(91), self.mm2p(47.5), 'Vistoriado por:')

        # forma de pagamento
        self.pdfarq.rect(self.offsety, self.mm2p(36), self.largquadro, self.mm2p(7))
        self.pdfarq.drawString(self.offsety + self.mm2p(2), self.mm2p(38.5), 'Forma de pagamento:')

        # observacao
        self.pdfarq.rect(self.offsety, self.offsetx, self.largquadro, self.mm2p(23))
        self.pdfarq.drawString(self.offsety + self.mm2p(2), self.mm2p(28.5), 'Observações:')

        # variaveis
        self.os = None


    def layoutOSContinue(self):
        ### layout
        # cabecalho estabelecimento
        self.pdfarq.rect(self.offsety, self.mm2p(280), self.largquadro, self.mm2p(7))
        
        self.pdfarq.setFont("Courier-Bold", 15)
        self.pdfarq.drawString(self.mm2p(162), self.mm2p(282), 'OS:')
        
        # corpo
        self.pdfarq.rect(self.offsety, self.mm2p(273), self.mm2p(20), self.mm2p(7))
        self.pdfarq.rect(self.mm2p(28), self.mm2p(273), self.mm2p(100), self.mm2p(7))
        self.pdfarq.rect(self.mm2p(128), self.mm2p(273), self.mm2p(37), self.mm2p(7))
        self.pdfarq.rect(self.mm2p(165), self.mm2p(273), self.mm2p(37), self.mm2p(7))
        self.pdfarq.rect(self.offsety, self.offsetx, self.largquadro, self.mm2p(263))
        
        self.pdfarq.setFont("Courier-Bold", 11)
        self.pdfarq.drawString(self.offsety + self.mm2p(6), self.mm2p(275), 'Qtd')
        self.pdfarq.drawString(self.offsety + self.mm2p(48), self.mm2p(275), 'Produtos / Serviços')
        self.pdfarq.drawString(self.offsety + self.mm2p(123), self.mm2p(275), 'Val. Unitário')
        self.pdfarq.drawString(self.offsety + self.mm2p(163), self.mm2p(275), 'Valor total')

        # variaveis
        self.os = None


    def writerPdfOS(self):
        #self.pdfarq.drawCentredString(self.offsety + self.mm2p(97), self.mm2p(236), 'Teste: ')

        dadosos = db.consultaGeral(self.os)
        data = str(dadosos[0][17]).split('-')
        somaprod = db.consultaSomaProd(self.os)[0][0]
        somaserv = db.consultaSomaServ(self.os)[0][0]
        totalos = db.consultaSomaItemOS(self.os)[0][0]
        param = db.consultaParam()[0]
        idestab = db.consultaEstabCod(param[0])[0]

        self.layoutOS() # layout da primeira pagina da OS

        self.pdfarq.drawInlineImage(str(idestab[12]), self.offsety + self.mm2p(1), self.mm2p(249), self.mm2p(60), self.mm2p(38)) # cabeçalho

        self.pdfarq.setFont("Courier", 11)
        self.pdfarq.drawString(self.offsety + self.mm2p(63), self.mm2p(283), str(idestab[3]) + ', ' + str(idestab[4]))
        self.pdfarq.drawString(self.offsety + self.mm2p(63), self.mm2p(278), str(idestab[6]) + ' - ' + str(idestab[7]))

        if idestab[9] == '' and idestab[10] == '':
            self.pdfarq.drawString(self.offsety + self.mm2p(63), self.mm2p(273), 'Contato: ' + str(idestab[8]))
        elif idestab[10] == '':
            self.pdfarq.drawString(self.offsety + self.mm2p(63), self.mm2p(273), 'Contato: ' + str(idestab[8]) + ' / ' + str(idestab[9]))
        else:
            self.pdfarq.drawString(self.offsety + self.mm2p(63), self.mm2p(273), 'Contato: ' + str(idestab[8]) + ' / ' + str(idestab[9]) + ' / ' + str(idestab[10]))

        self.pdfarq.drawString(self.offsety + self.mm2p(63), self.mm2p(268), 'E-mail: ' + str(idestab[11]))

        self.pdfarq.setFont("Courier", 15)
        self.pdfarq.drawString(self.mm2p(90), self.mm2p(252), data[2] + '/' + data[1] + '/' + data[0])
        self.pdfarq.drawString(self.mm2p(162), self.mm2p(252), str(dadosos[0][0]).zfill(5))

        self.pdfarq.setFont("Courier", 11)
        self.pdfarq.drawString(self.offsety + self.mm2p(22), self.mm2p(240), str(dadosos[0][2])) # cliente
        self.pdfarq.drawString(self.offsety + self.mm2p(125), self.mm2p(240), str(dadosos[0][3]))
        self.pdfarq.drawString(self.offsety + self.mm2p(23), self.mm2p(235), str(dadosos[0][9]))
        self.pdfarq.drawString(self.offsety + self.mm2p(92), self.mm2p(235), str(dadosos[0][10]))
        self.pdfarq.drawString(self.offsety + self.mm2p(24), self.mm2p(230), str(dadosos[0][4]))
        self.pdfarq.drawString(self.offsety + self.mm2p(123), self.mm2p(230), str(dadosos[0][5]))
        self.pdfarq.drawString(self.offsety + self.mm2p(27), self.mm2p(225), str(dadosos[0][6]))
        self.pdfarq.drawString(self.offsety + self.mm2p(19), self.mm2p(220), str(dadosos[0][7]))
        self.pdfarq.drawString(self.offsety + self.mm2p(92), self.mm2p(220), str(dadosos[0][8]))

        if dadosos[0][15] != '':
            self.pdfarq.drawString(self.offsety + self.mm2p(32), self.mm2p(209.5), str(dadosos[0][15] + ' / ' +  str(dadosos[0][13]))) # veiculo
        else:
            self.pdfarq.drawString(self.offsety + self.mm2p(32), self.mm2p(209.5), str(dadosos[0][13]))
        
        self.pdfarq.drawString(self.offsety + self.mm2p(117), self.mm2p(209.5), str(dadosos[0][12]))
        self.pdfarq.drawString(self.offsety + self.mm2p(13), self.mm2p(204.5), str(dadosos[0][14]))
        self.pdfarq.drawString(self.offsety + self.mm2p(131), self.mm2p(204.5), self.convertKM(str(dadosos[0][16])).rjust(7,' '))

        numitem = 1
        
        for item in dadosos: # imprime ate o 26° item da ordem de serviço
            self.pdfarq.setFont("Courier", 11)
            self.pdfarq.drawString(self.offsety + self.mm2p(8), self.mm2p(self.posinicorpo), str(item[28])) # corpo
            self.pdfarq.drawString(self.offsety + self.mm2p(30), self.mm2p(self.posinicorpo), str(item[26]))
            self.pdfarq.drawString(self.offsety + self.mm2p(133), self.mm2p(self.posinicorpo), str('%.2f' % item[31]).replace('.',',').rjust(8,' '))
            self.pdfarq.drawString(self.offsety + self.mm2p(170), self.mm2p(self.posinicorpo), str('%.2f' % item[29]).replace('.',',').rjust(8,' '))
            
            self.posinicorpo -= 4.5
            numitem += 1

            if self.posinicorpo <= 70.4 and len(dadosos) > 26: # para o loop com a lista de produtos e indica que continua na pagina seguinte
                self.pdfarq.setFont("Courier", 9)
                self.pdfarq.drawString(self.offsety + self.mm2p(170), self.mm2p(70.5), 'Continua...')

                break
    
            elif self.posinicorpo <= 70.4:
                break

        self.pdfarq.setFont("Courier", 11)
        self.pdfarq.drawString(self.offsety + self.mm2p(62), self.mm2p(65.5), str('%.2f' % somaprod).replace('.',',').rjust(8,' ')) # total produtos servico
        self.pdfarq.drawString(self.offsety + self.mm2p(161), self.mm2p(65.5), str('%.2f' % somaserv).replace('.',',').rjust(8,' '))

        self.pdfarq.drawString(self.offsety + self.mm2p(170), self.mm2p(58.3), str('%.2f' % totalos).replace('.',',').rjust(8,' ')) # total geral

        self.pdfarq.drawString(self.offsety + self.mm2p(35), self.mm2p(47.5), str(dadosos[0][21])) # tecnicos
        self.pdfarq.drawString(self.offsety + self.mm2p(126), self.mm2p(47.5), str(dadosos[0][23]))

        self.pdfarq.drawString(self.offsety + self.mm2p(45), self.mm2p(38.5), str(dadosos[0][18])) # forma de pagamento

        self.pdfarq.drawString(self.offsety + self.mm2p(28), self.mm2p(28.5), str('Garantia valida por %s kilometros ou %s dias, o que ocorrer primeiro.' % (param[2], param[1]))) # obs

        # condicoes para preencher o quadro de observações
        fraseobs = str(dadosos[0][19]).replace('\n','').split(' ')
        posinih = 11
        posiniv = 24

        for palavra in fraseobs:
            tamanho = self.mm2p(len(palavra))
            self.pdfarq.drawString(self.mm2p(posinih), self.mm2p(posiniv), palavra)

            if len(palavra) < 3:
                posinih += tamanho + 1
            elif len(palavra) >= 3 and len(palavra) < 7:
                posinih += tamanho
            elif len(palavra) >= 7 and len(palavra) < 11:
                posinih += tamanho - 1
            elif len(palavra) >= 12:
                posinih += tamanho - 2
            else:
                posinih += tamanho - 3

            if posinih >= 190:
                posiniv -= 4.5
                posinih = 11

        self.pdfarq.showPage()

        if len(dadosos) > 27:
            self.posinicorpo = 269

            self.layoutOSContinue()

            self.pdfarq.setFont("Courier", 15)
            self.pdfarq.drawString(self.mm2p(180), self.mm2p(282), str(dadosos[0][0]).zfill(5)) # indicativo da OS
            
            for item in dadosos[numitem:]:
                self.pdfarq.setFont("Courier", 11)
                self.pdfarq.drawString(self.offsety + self.mm2p(8), self.mm2p(self.posinicorpo), str(item[28])) # corpo
                self.pdfarq.drawString(self.offsety + self.mm2p(30), self.mm2p(self.posinicorpo), str(item[26]))
                self.pdfarq.drawString(self.offsety + self.mm2p(133), self.mm2p(self.posinicorpo), str('%.2f' % item[31]).replace('.',',').rjust(8,' '))
                self.pdfarq.drawString(self.offsety + self.mm2p(170), self.mm2p(self.posinicorpo), str('%.2f' % item[29]).replace('.',',').rjust(8,' '))
            
                self.posinicorpo -= 4.5
                
                if self.posinicorpo <= 15: # para o loop com a lista de produtos e indica que continua na pagina seguinte
                    self.pdfarq.setFont("Courier", 9)
                    self.pdfarq.drawString(self.offsety + self.mm2p(1), self.mm2p(self.posinicorpo), 'Continua...')

                    self.pdfarq.showPage()

                    self.posinicorpo = 276

        #self.pdfarq.drawString(self.offsety + self.mm2p(3), self.mm2p(19), str(dadosos[0][19]).replace('\n', ' '))

        self.pdfarq.save()

        self.printPdf()


    def layoutLucroPS(self):
        # titulo
        # (esquerda para direita, baixo para cima, tamanho, altura)
        #self.pdfarq.rect(self.offsety, self.mm2p(278), self.largquadro, self.mm2p(10))

        # (fonte, tamanho)
        self.pdfarq.setFont("Courier-Bold", 15)
        # (esquerda para direira, baixo para cima, texto)
        self.pdfarq.drawString(self.mm2p(70), self.mm2p(281), 'Relatório comparativo')

        self.pdfarq.setFont("Courier", 12)
        self.pdfarq.drawString(self.mm2p(53), self.mm2p(275), 'Custo e faturamento por produto/serviço')
        
        # cabecalho
        self.pdfarq.rect(self.offsety, self.mm2p(244), self.largquadro, self.mm2p(15))
        
        self.pdfarq.setFont("Courier-Bold", 11)
        self.pdfarq.drawString(self.offsety + self.mm2p(3), self.mm2p(253), 'Empresa:')
        self.pdfarq.drawString(self.offsety + self.mm2p(130), self.mm2p(253), 'CNPJ:')
        self.pdfarq.drawString(self.offsety + self.mm2p(3), self.mm2p(248), 'Período:')
        
        # corpo
        self.pdfarq.rect(self.offsety, self.mm2p(231), self.mm2p(80), self.mm2p(7))
        self.pdfarq.rect(self.mm2p(88), self.mm2p(231), self.mm2p(18), self.mm2p(7))
        self.pdfarq.rect(self.mm2p(106), self.mm2p(231), self.mm2p(32), self.mm2p(7))
        self.pdfarq.rect(self.mm2p(138), self.mm2p(231), self.mm2p(32), self.mm2p(7))
        self.pdfarq.rect(self.mm2p(170), self.mm2p(231), self.mm2p(32), self.mm2p(7))
        self.pdfarq.rect(self.offsety, self.offsetx, self.mm2p(98), self.mm2p(7))
        self.pdfarq.rect(self.mm2p(106), self.offsetx, self.mm2p(32), self.mm2p(7))
        self.pdfarq.rect(self.mm2p(138), self.offsetx, self.mm2p(32), self.mm2p(7))
        self.pdfarq.rect(self.mm2p(170), self.offsetx, self.mm2p(32), self.mm2p(7))
        self.pdfarq.rect(self.offsety, self.offsetx, self.largquadro, self.mm2p(224))

        self.pdfarq.setFont("Courier-Bold", 11)
        self.pdfarq.drawString(self.offsety + self.mm2p(2), self.mm2p(233.3), 'Produtos / Serviços')
        self.pdfarq.drawString(self.mm2p(90), self.mm2p(233.3), 'Qtd')
        self.pdfarq.drawString(self.mm2p(108), self.mm2p(233.3), 'Custo')
        self.pdfarq.drawString(self.mm2p(140), self.mm2p(233.3), 'Faturado')
        self.pdfarq.drawString(self.mm2p(172), self.mm2p(233.3), 'Saldo')
        self.pdfarq.drawString(self.mm2p(70), self.mm2p(9.3), 'Total geral:')
        self.pdfarq.drawString(self.mm2p(100), self.mm2p(9.3), 'R$ ')


    def layoutLucroPSContinue(self):        
        # corpo
        self.pdfarq.rect(self.offsety, self.mm2p(231), self.mm2p(80), self.mm2p(7))
        self.pdfarq.rect(self.mm2p(88), self.mm2p(231), self.mm2p(18), self.mm2p(7))
        self.pdfarq.rect(self.mm2p(106), self.mm2p(231), self.mm2p(32), self.mm2p(7))
        self.pdfarq.rect(self.mm2p(138), self.mm2p(231), self.mm2p(32), self.mm2p(7))
        self.pdfarq.rect(self.mm2p(170), self.mm2p(231), self.mm2p(32), self.mm2p(7))
        self.pdfarq.rect(self.offsety, self.offsetx, self.mm2p(98), self.mm2p(7))
        self.pdfarq.rect(self.mm2p(106), self.offsetx, self.mm2p(32), self.mm2p(7))
        self.pdfarq.rect(self.mm2p(138), self.offsetx, self.mm2p(32), self.mm2p(7))
        self.pdfarq.rect(self.mm2p(170), self.offsetx, self.mm2p(32), self.mm2p(7))
        self.pdfarq.rect(self.offsety, self.offsetx, self.largquadro, self.mm2p(224))

        self.pdfarq.setFont("Courier-Bold", 11)
        self.pdfarq.drawString(self.offsety + self.mm2p(2), self.mm2p(233.3), 'Produtos / Serviços')
        self.pdfarq.drawString(self.mm2p(90), self.mm2p(233.3), 'Qtd')
        self.pdfarq.drawString(self.mm2p(108), self.mm2p(233.3), 'Custo')
        self.pdfarq.drawString(self.mm2p(140), self.mm2p(233.3), 'Faturado')
        self.pdfarq.drawString(self.mm2p(172), self.mm2p(233.3), 'Saldo')
        self.pdfarq.drawString(self.mm2p(70), self.mm2p(9.3), 'Total geral:')
        self.pdfarq.drawString(self.mm2p(100), self.mm2p(9.3), 'R$ ')


    def writerLucroPS(self, datainicial, datafinal):
        dadosper = db.consultaLucroPS(datainicial, datafinal)
        total = db.consultaLucro(datainicial, datafinal)[0]
        param = db.consultaParam()[0]
        estab = db.consultaEstabCod(param[0])[0]

        dtini = datainicial.split('-')
        dtfin = datafinal.split('-')

        if len(dadosper) == 0:
            raise KeyboardInterrupt

        # identificacao empresa
        self.pdfarq.setFont("Courier", 11)
        self.pdfarq.drawString(self.offsety + self.mm2p(23), self.mm2p(253), str(estab[2]))
        self.pdfarq.drawString(self.offsety + self.mm2p(143), self.mm2p(253), str(estab[1]))
        self.pdfarq.drawString(self.offsety + self.mm2p(23), self.mm2p(248), str(dtini[2] + '/' + dtini[1] + '/' + dtini[0] + ' a ' + dtfin[2] + '/' + dtfin[1] + '/' + dtfin[0]))

        posinicorpo = 227

        try:
            self.pdfarq.setFont("Courier", 11) # corpo
            for item in dadosper:
                self.pdfarq.drawString(self.mm2p(10), self.mm2p(posinicorpo), str(item[1]))
                self.pdfarq.drawString(self.mm2p(96), self.mm2p(posinicorpo), str(item[2]))
                self.pdfarq.drawString(self.mm2p(117), self.mm2p(posinicorpo), str('%.2f' % item[3]).replace('.',',').rjust(8,' '))
                self.pdfarq.drawString(self.mm2p(149), self.mm2p(posinicorpo), str('%.2f' % item[4]).replace('.',',').rjust(8,' '))
                self.pdfarq.drawString(self.mm2p(181), self.mm2p(posinicorpo), str('%.2f' % item[5]).replace('.',',').rjust(8,' '))
                posinicorpo -= 4.5

                if self.posinicorpo <= 50.4:
                    break

            self.pdfarq.drawString(self.mm2p(117), self.mm2p(9.3), str('%.2f' % total[0]).replace('.',',').rjust(8,' '))
            self.pdfarq.drawString(self.mm2p(149), self.mm2p(9.3), str('%.2f' % total[1]).replace('.',',').rjust(8,' '))
            self.pdfarq.drawString(self.mm2p(181), self.mm2p(9.3), str('%.2f' % total[2]).replace('.',',').rjust(8,' '))

            self.layoutLucroPS()

            self.pdfarq.showPage()

            self.pdfarq.save()

            self.printPdf()

        except TypeError:
            raise ValueError('Período sem movimento.')


    def layoutLucroOS(self):
        # titulo
        # (esquerda para direita, baixo para cima, tamanho, altura)
        #self.pdfarq.rect(self.offsety, self.mm2p(278), self.largquadro, self.mm2p(10))

        # (fonte, tamanho)
        self.pdfarq.setFont("Courier-Bold", 15)
        # (esquerda para direira, baixo para cima, texto)
        self.pdfarq.drawString(self.mm2p(70), self.mm2p(281), 'Relatório comparativo')

        self.pdfarq.setFont("Courier", 12)
        self.pdfarq.drawString(self.mm2p(53), self.mm2p(275), 'Custo e faturamento por ordem de serviço')

        # cabecalho
        self.pdfarq.rect(self.offsety, self.mm2p(244), self.largquadro, self.mm2p(15))
        
        self.pdfarq.setFont("Courier-Bold", 11)
        self.pdfarq.drawString(self.offsety + self.mm2p(3), self.mm2p(253), 'Empresa:')
        self.pdfarq.drawString(self.offsety + self.mm2p(130), self.mm2p(253), 'CNPJ:')
        self.pdfarq.drawString(self.offsety + self.mm2p(3), self.mm2p(248), 'Período:')
        
        # corpo
        self.pdfarq.rect(self.offsety, self.mm2p(231), self.mm2p(66), self.mm2p(7))
        self.pdfarq.rect(self.mm2p(74), self.mm2p(231), self.mm2p(32), self.mm2p(7))
        self.pdfarq.rect(self.mm2p(106), self.mm2p(231), self.mm2p(32), self.mm2p(7))
        self.pdfarq.rect(self.mm2p(138), self.mm2p(231), self.mm2p(32), self.mm2p(7))
        self.pdfarq.rect(self.mm2p(170), self.mm2p(231), self.mm2p(32), self.mm2p(7))
        self.pdfarq.rect(self.offsety, self.offsetx, self.mm2p(98), self.mm2p(7))
        self.pdfarq.rect(self.mm2p(106), self.offsetx, self.mm2p(32), self.mm2p(7))
        self.pdfarq.rect(self.mm2p(138), self.offsetx, self.mm2p(32), self.mm2p(7))
        self.pdfarq.rect(self.mm2p(170), self.offsetx, self.mm2p(32), self.mm2p(7))
        self.pdfarq.rect(self.offsety, self.offsetx, self.largquadro, self.mm2p(224))
        
        self.pdfarq.setFont("Courier-Bold", 11)
        self.pdfarq.drawString(self.offsety + self.mm2p(2), self.mm2p(233.3), 'Ordem de serviço')
        self.pdfarq.drawString(self.mm2p(76), self.mm2p(233.3), 'Data')
        self.pdfarq.drawString(self.mm2p(108), self.mm2p(233.3), 'Custo')
        self.pdfarq.drawString(self.mm2p(140), self.mm2p(233.3), 'Faturado')
        self.pdfarq.drawString(self.mm2p(172), self.mm2p(233.3), 'Saldo')
        self.pdfarq.drawString(self.mm2p(70), self.mm2p(9.3), 'Total geral:')
        self.pdfarq.drawString(self.mm2p(100), self.mm2p(9.3), 'R$ ')


    def layoutLucroOSContinue(self):       
        # corpo
        self.pdfarq.rect(self.offsety, self.mm2p(231), self.mm2p(66), self.mm2p(7))
        self.pdfarq.rect(self.mm2p(74), self.mm2p(231), self.mm2p(32), self.mm2p(7))
        self.pdfarq.rect(self.mm2p(106), self.mm2p(231), self.mm2p(32), self.mm2p(7))
        self.pdfarq.rect(self.mm2p(138), self.mm2p(231), self.mm2p(32), self.mm2p(7))
        self.pdfarq.rect(self.mm2p(170), self.mm2p(231), self.mm2p(32), self.mm2p(7))
        self.pdfarq.rect(self.offsety, self.offsetx, self.mm2p(98), self.mm2p(7))
        self.pdfarq.rect(self.mm2p(106), self.offsetx, self.mm2p(32), self.mm2p(7))
        self.pdfarq.rect(self.mm2p(138), self.offsetx, self.mm2p(32), self.mm2p(7))
        self.pdfarq.rect(self.mm2p(170), self.offsetx, self.mm2p(32), self.mm2p(7))
        self.pdfarq.rect(self.offsety, self.offsetx, self.largquadro, self.mm2p(224))
        
        self.pdfarq.setFont("Courier-Bold", 11)
        self.pdfarq.drawString(self.offsety + self.mm2p(2), self.mm2p(233.3), 'Ordem de serviço')
        self.pdfarq.drawString(self.mm2p(76), self.mm2p(233.3), 'Data')
        self.pdfarq.drawString(self.mm2p(108), self.mm2p(233.3), 'Custo')
        self.pdfarq.drawString(self.mm2p(140), self.mm2p(233.3), 'Faturado')
        self.pdfarq.drawString(self.mm2p(172), self.mm2p(233.3), 'Saldo')
        self.pdfarq.drawString(self.mm2p(70), self.mm2p(9.3), 'Total geral:')
        self.pdfarq.drawString(self.mm2p(100), self.mm2p(9.3), 'R$ ')


    def writerLucroOS(self, datainicial, datafinal):
        dadosper = db.consultaLucroOS(datainicial, datafinal)
        total = db.consultaLucro(datainicial, datafinal)[0]
        param = db.consultaParam()[0]
        estab = db.consultaEstabCod(param[0])[0]

        dtini = datainicial.split('-')
        dtfin = datafinal.split('-')

        assert len(dadosper) < 1, 'Período sem movimento.'

        self.pdfarq.setFont("Courier", 11)
        self.pdfarq.drawString(self.offsety + self.mm2p(23), self.mm2p(253), str(estab[2]))
        self.pdfarq.drawString(self.offsety + self.mm2p(143), self.mm2p(253), str(estab[1]))
        self.pdfarq.drawString(self.offsety + self.mm2p(23), self.mm2p(248), str(dtini[2] + '/' + dtini[1] + '/' + dtini[0] + ' a ' + dtfin[2] + '/' + dtfin[1] + '/' + dtfin[0]))

        posinicorpo = 227
        self.pdfarq.setFont("Courier", 11) # corpo
        for item in dadosper:
            self.pdfarq.drawString(self.mm2p(10), self.mm2p(posinicorpo), str(item[0]).zfill(5))
            self.pdfarq.drawString(self.mm2p(80), self.mm2p(posinicorpo), str(item[1])[8:] + '/' + str(item[1])[5:7] + '/' + str(item[1])[0:4])
            self.pdfarq.drawString(self.mm2p(117), self.mm2p(posinicorpo), str('%.2f' % item[2]).replace('.',',').rjust(8,' '))
            self.pdfarq.drawString(self.mm2p(149), self.mm2p(posinicorpo), str('%.2f' % item[3]).replace('.',',').rjust(8,' '))
            self.pdfarq.drawString(self.mm2p(181), self.mm2p(posinicorpo), str('%.2f' % item[4]).replace('.',',').rjust(8,' '))
            posinicorpo -= 4.5

            if self.posinicorpo <= 50.4:
                break

        self.pdfarq.drawString(self.mm2p(117), self.mm2p(9.3), str('%.2f' % total[0]).replace('.',',').rjust(8,' '))
        self.pdfarq.drawString(self.mm2p(149), self.mm2p(9.3), str('%.2f' % total[1]).replace('.',',').rjust(8,' '))
        self.pdfarq.drawString(self.mm2p(181), self.mm2p(9.3), str('%.2f' % total[2]).replace('.',',').rjust(8,' '))

        self.layoutLucroOS()

        self.pdfarq.showPage()

        self.pdfarq.save()

        self.printPdf()


    def layoutExtrato(self):
        # titulo
        # (esquerda para direita, baixo para cima, tamanho, altura)
        #self.pdfarq.rect(self.offsety, self.mm2p(278), self.largquadro, self.mm2p(10))

        # (fonte, tamanho)
        self.pdfarq.setFont("Courier-Bold", 15)
        # (esquerda para direira, baixo para cima, texto)
        self.pdfarq.drawString(self.mm2p(70), self.mm2p(281), 'Movimentos Financeiro')

        self.pdfarq.setFont("Courier", 12)
        self.pdfarq.drawString(self.mm2p(53), self.mm2p(275), '')

        # cabecalho
        self.pdfarq.rect(self.offsety, self.mm2p(260), self.largquadro, self.mm2p(15))
        
        self.pdfarq.setFont("Courier-Bold", 11)
        self.pdfarq.drawString(self.offsety + self.mm2p(3), self.mm2p(269), 'Empresa:')
        self.pdfarq.drawString(self.offsety + self.mm2p(130), self.mm2p(269), 'CNPJ:')
        self.pdfarq.drawString(self.offsety + self.mm2p(3), self.mm2p(264), 'Período:')

        # corpo
        self.pdfarq.rect(self.offsety, self.mm2p(250), self.mm2p(25), self.mm2p(7))
        self.pdfarq.rect(self.mm2p(33), self.mm2p(250), self.mm2p(80), self.mm2p(7))
        self.pdfarq.rect(self.mm2p(113), self.mm2p(250), self.mm2p(29), self.mm2p(7))
        self.pdfarq.rect(self.mm2p(142), self.mm2p(250), self.mm2p(30), self.mm2p(7))
        self.pdfarq.rect(self.mm2p(172), self.mm2p(250), self.mm2p(30), self.mm2p(7))
        #self.pdfarq.rect(self.offsety, self.offsetx, self.mm2p(162), self.mm2p(7))
        #self.pdfarq.rect(self.mm2p(170), self.offsetx, self.mm2p(32), self.mm2p(7))
        self.pdfarq.rect(self.offsety, self.offsetx + self.mm2p(5), self.largquadro, self.mm2p(235))

        self.pdfarq.setFont("Courier-Bold", 11)
        self.pdfarq.drawString(self.offsety + self.mm2p(2), self.mm2p(252), 'Data')
        self.pdfarq.drawString(self.mm2p(35), self.mm2p(252), 'Cliente/Fornecedor')
        self.pdfarq.drawString(self.mm2p(115), self.mm2p(252), 'Docto')
        self.pdfarq.drawString(self.mm2p(144), self.mm2p(252), 'Valor')
        self.pdfarq.drawString(self.mm2p(173.7), self.mm2p(252), 'Saldo diário')
        #self.pdfarq.drawString(self.mm2p(133), self.mm2p(9.3), 'Total geral:')
        #self.pdfarq.drawString(self.mm2p(163), self.mm2p(9.3), 'R$ ')


    def layoutExtratoContinue(self):
        # corpo
        self.pdfarq.rect(self.offsety, self.mm2p(280), self.mm2p(25), self.mm2p(7))
        self.pdfarq.rect(self.mm2p(33), self.mm2p(280), self.mm2p(80), self.mm2p(7))
        self.pdfarq.rect(self.mm2p(113), self.mm2p(280), self.mm2p(29), self.mm2p(7))
        self.pdfarq.rect(self.mm2p(142), self.mm2p(280), self.mm2p(30), self.mm2p(7))
        self.pdfarq.rect(self.mm2p(172), self.mm2p(280), self.mm2p(30), self.mm2p(7))
        self.pdfarq.rect(self.offsety, self.offsetx + self.mm2p(5), self.largquadro, self.mm2p(265))

        self.pdfarq.setFont("Courier-Bold", 11)
        self.pdfarq.drawString(self.offsety + self.mm2p(2), self.mm2p(282), 'Data')
        self.pdfarq.drawString(self.mm2p(35), self.mm2p(282), 'Cliente/Fornecedor')
        self.pdfarq.drawString(self.mm2p(115), self.mm2p(282), 'Docto')
        self.pdfarq.drawString(self.mm2p(144), self.mm2p(282), 'Valor')
        self.pdfarq.drawString(self.mm2p(173.7), self.mm2p(282), 'Saldo diário')


    def writerExtrato(self, datainicial, datafinal):
        dadosper = db.consultaMovFinanceiro(datainicial, datafinal)

        assert len(dadosper) < 1, 'Período sem movimento.'

        tot = []
        for dado in dadosper:
            if type(dado[3]) == float:
                tot.append(dado[3])

        total = sum(tot)
        param = db.consultaParam()[0]
        estab = db.consultaEstabCod(param[0])[0]

        dtini = datainicial.split('-')
        dtfin = datafinal.split('-')

        self.layoutExtrato()

        # empresa e periodo
        self.pdfarq.setFont("Courier", 11)
        self.pdfarq.drawString(self.offsety + self.mm2p(23), self.mm2p(269), str(estab[2]))
        self.pdfarq.drawString(self.offsety + self.mm2p(143), self.mm2p(269), str(estab[1]))
        self.pdfarq.drawString(self.offsety + self.mm2p(23), self.mm2p(264), str(dtini[2] + '/' + dtini[1] + '/' + dtini[0] + ' a ' + dtfin[2] + '/' + dtfin[1] + '/' + dtfin[0]))

        posinicorpo = 246
        
        self.pdfarq.setFont("Courier", 11) # corpo
        for item in dadosper:
            self.pdfarq.setFillColor(HexColor('#000000'))
            self.pdfarq.drawString(self.mm2p(9), self.mm2p(posinicorpo), str(item[0])[8:] + '/' + str(item[0])[5:7] + '/' + str(item[0])[0:4])
            self.pdfarq.drawString(self.mm2p(35), self.mm2p(posinicorpo), str(item[1]))

            if item[2] == '':
                self.pdfarq.drawString(self.mm2p(110), self.mm2p(posinicorpo), '')
            else:
                self.pdfarq.drawString(self.mm2p(110), self.mm2p(posinicorpo), str(item[2]).zfill(6).rjust(8,' '))

            try:
                if item[3] > 0: # condicao para definir a cor do texto com base no valor positivo ou negativo
                    self.pdfarq.setFillColor(HexColor('#0000FF'))
                    self.pdfarq.drawString(self.mm2p(152), self.mm2p(posinicorpo), str('%.2f' % item[3]).replace('.',',').rjust(8,' '))
                elif item[3] < 0:
                    self.pdfarq.setFillColor(HexColor('#8B0000'))
                    self.pdfarq.drawString(self.mm2p(152), self.mm2p(posinicorpo), str('%.2f' % item[3]).replace('.',',').rjust(8,' '))
                else:
                    self.pdfarq.setFillColor(HexColor('#000000'))
                    self.pdfarq.drawString(self.mm2p(152), self.mm2p(posinicorpo), str('%.2f' % item[3]).replace('.',',').rjust(8,' '))
                    
            except TypeError:
                self.pdfarq.setFillColor(HexColor('#000000'))
                self.pdfarq.drawString(self.mm2p(152), self.mm2p(posinicorpo), '')

            try:
                if item[4] > 0:
                    self.pdfarq.setFillColor(HexColor('#0000FF'))
                    self.pdfarq.drawString(self.mm2p(182), self.mm2p(posinicorpo), str('%.2f' % item[4]).replace('.',',').rjust(8,' '))
                elif item[4] < 0:
                    self.pdfarq.setFillColor(HexColor('#8B0000'))
                    self.pdfarq.drawString(self.mm2p(182), self.mm2p(posinicorpo), str('%.2f' % item[4]).replace('.',',').rjust(8,' '))
                else:
                    self.pdfarq.setFillColor(HexColor('#000000'))
                    self.pdfarq.drawString(self.mm2p(182), self.mm2p(posinicorpo), str('%.2f' % item[4]).replace('.',',').rjust(8,' '))
            except TypeError:
                self.pdfarq.setFillColor(HexColor('#000000'))
                self.pdfarq.drawString(self.mm2p(182), self.mm2p(posinicorpo), '')
            
            posinicorpo -= 4.5

            if posinicorpo <= 15:
                self.pdfarq.setFont("Courier", 9)
                self.pdfarq.drawString(self.offsety + self.mm2p(1), self.mm2p(12), 'Continua...')

                self.pdfarq.showPage()

                # nova pagina
                posinicorpo = 276

                self.layoutExtratoContinue()

                self.pdfarq.setFont("Courier", 11)

        # saldo periodo
        self.pdfarq.setFont("Courier-Bold", 11)
        self.pdfarq.setFillColor(HexColor('#000000'))
        self.pdfarq.rect(self.offsety, self.mm2p(8), self.mm2p(162), self.mm2p(7))
        self.pdfarq.rect(self.mm2p(170), self.mm2p(8), self.mm2p(32), self.mm2p(7))

        self.pdfarq.drawString(self.mm2p(130), self.mm2p(10), 'Saldo período:')
        self.pdfarq.drawString(self.mm2p(163), self.mm2p(10), 'R$ ')

        self.pdfarq.drawString(self.mm2p(181), self.mm2p(10), str('%.2f' % total).replace('.',',').rjust(8,' '))

        # conclusao
        self.pdfarq.save()
        # aprensentar pdf
        self.printPdf()

        return
    

    def printPdf(self):
        webbrowser.open(self.pdfnomearq, new=2)

 
    def mm2p(self, mili):
        return mili / 0.352777


    def dataext(self, data):
        dt = str(data)
        dia, mes, ano = dt.split('/')
        meses = {
            1:'janeiro', 2: 'fevereiro', 3: 'março', 4: 'abril', 5: 'maio', 6: 'junho',
            7:'julho', 8: 'agosto', 9: 'setembro', 10: 'outubto', 11: 'novembro', 12: 'dezembro'
        }

        return dia + ' de ' + meses[int(mes)] + ' de ' + ano


    def convertKM(self, km):
        sizekm = len(km)

        if sizekm == 6:
            formatkm = str(km)[0:3] + '.' + str(km)[3:]
        elif sizekm == 5:
            formatkm = str(km)[0:2] + '.' + str(km)[2:]
        elif sizekm == 4:
            formatkm = str(km)[0:1] + '.' + str(km)[1:]
        else:
            formatkm = sizekm

        return formatkm


if __name__ == '__main__':
    gererate = Pdf('tester.pdf')