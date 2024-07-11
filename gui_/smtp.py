from threading import Thread
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from gui_.custom import Custom_GUI
from class_.smtp import SMTP
import database.interactionsdb as db


class SMTP_Window():
    def __init__(self, master):
        # objeto da janela de configuracao
        self.master = master
        self.window = Toplevel()

        self.window.title("Configuração SMTP")

        # objeto de padronizacao do tema
        default = Custom_GUI()

        self.window.configure(bg=default.bg_window_color)
        self.window.transient(self.master) # força a sobreposição, mas permite seleção da tela raiz
        self.window.focus_force() # força o foco e permite seleção da tela raiz
        self.window.grab_set() # bloqueia seleção da tela raiz

        # tamanho da tela
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()

        # tamanho da janela de configucao
        window_width = 680
        window_height = 170

        # posicao da janela ao inicializar
        position_x = (screen_width / 2) - (window_width / 2)
        position_y = (screen_height / 2) - (window_height / 2)

        self.window.geometry("%dx%d+%d+%d" % (window_width, window_height, position_x, position_y))

        # blocos de cadastros
        position_block_config = 10

        self.config = Frame(self.window, width=660, height=150, bg=default.bg_color, bd=default.thickness_border_frames, relief='ridge')
        self.config.place(x=10, y=position_block_config)

        # campos dos blocos
        # empresa
        position_init_config_x = 10
        position_init_config_y = position_block_config

        self.email = StringVar()
        self.server = StringVar()
        self.port = IntVar()
        self.password = StringVar()
        self.ssl = BooleanVar()
        self.tls = BooleanVar()

        self.out_email = Label(self.config, text='E-mail', width=10, bg=default.bg_color, anchor=default.label_just)
        self.out_email.place(x=position_init_config_x, y=position_init_config_y)
        self.out_password = Label(self.config, text='Senha', width=10, bg=default.bg_color, anchor=default.label_just)
        self.out_password.place(x=position_init_config_x + 320, y=position_init_config_y)
        self.out_server = Label(self.config, text='Servidor', width=10, bg=default.bg_color, anchor=default.label_just)
        self.out_server.place(x=position_init_config_x, y=position_init_config_y + default.lines_space)
        self.out_port = Label(self.config, text='Porta', width=10, bg=default.bg_color, anchor=default.label_just)
        self.out_port.place(x=position_init_config_x + 320, y=position_init_config_y + default.lines_space)
        self.out_ssl = Label(self.config, text='SSL', width=10, bg=default.bg_color, anchor=default.label_just)
        self.out_ssl.place(x=position_init_config_x, y=position_init_config_y + (default.lines_space * 2))
        self.out_tls = Label(self.config, text='TLS', width=10, bg=default.bg_color, anchor=default.label_just)
        self.out_tls.place(x=position_init_config_x + 320, y=position_init_config_y + (default.lines_space * 2))

        self.in_email = Entry(self.config, textvariable=self.email, width=40, bd=default.thickness_border, justify=default.entry_just)
        self.in_email.place(x=position_init_config_x + 80, y=position_init_config_y)
        self.in_password = Entry(self.config, textvariable=self.password, width=30, bd=default.thickness_border, justify=default.entry_just, show='*')
        self.in_password.place(x=position_init_config_x + 400, y=position_init_config_y)
        self.in_server = Entry(self.config, textvariable=self.server, width=40, bd=default.thickness_border, justify=default.entry_just)
        self.in_server.place(x=position_init_config_x + 80, y=position_init_config_y + default.lines_space)
        self.in_port= Entry(self.config, textvariable=self.port, width=5, bd=default.thickness_border, justify=default.entry_just)
        self.in_port.place(x=position_init_config_x + 400, y=position_init_config_y + default.lines_space)
        self.in_ssl = Checkbutton(self.config, bd=default.thickness_border, variable=self.ssl, onvalue=True, offvalue=False, bg=default.bg_color)
        self.in_ssl.place(x=position_init_config_x + 80, y=position_init_config_y + (default.lines_space * 2))
        self.in_tls = Checkbutton(self.config, bd=default.thickness_border, variable=self.tls, onvalue=True, offvalue=False, bg=default.bg_color)
        self.in_tls.place(x=position_init_config_x + 400, y=position_init_config_y + (default.lines_space * 2))

        self.record = Button(self.config, text='Gravar', width=12, bg=default.bg_color, command=self.__record)
        self.record.place(x=position_init_config_x + 500, y=position_init_config_y + (default.lines_space * 4))

        # atalhos
        #self.in_company_cnpj.bind('<F9>', lambda e: e * 2)

        # posicao inicial cursor
        self.in_email.focus()

        # carrega os dados para os campos
        self.__load_smtp_fields()


    def __record(self):
        smtp_config = SMTP(
            self.email.get(),
            self.server.get(),
            self.password.get(),
            self.ssl.get(),
            self.tls.get(),
            self.port.get()
        )

        # grava no banco de dados
        db.new_smtp(smtp_config)

        self.in_email.focus()

        return


    def __load_smtp_fields(self):
        smtp = db.get_smtp()

        self.email.set(smtp.email),
        self.server.set(smtp.servidor),
        self.password.set(smtp.senha),
        self.ssl.set(smtp.ssl),
        self.tls.set(smtp.tls),
        self.port.set(smtp.porta)

        self.in_email.focus()

        return