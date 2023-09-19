from threading import Thread
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from interface.custom import Custom_GUI


class Reports_Window():
    def __init__(self, master):
        # objeto da janela de configuracao
        self.master = master
        self.window = Toplevel()

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
        window_width = 370
        window_height = 120

        # posicao da janela ao inicializar
        position_x = (screen_width / 2) - (window_width / 2)
        position_y = (screen_height / 2) - (window_height / 2)

        self.window.geometry("%dx%d+%d+%d" % (window_width, window_height, position_x, position_y))

        # blocos de cadastros
        position_block_params = 10

        self.params = Frame(self.window, width=350, height=100, bg=default.bg_color, bd=default.thickness_border_frames, relief='ridge')
        self.params.place(x=10, y=position_block_params)

        self.params_period = Frame(self.params, width=330, height=40, bg=default.bg_color, bd=default.thickness_border_frames, relief='groove')
        self.params_period.place(x=10, y=10)

        # identificacao dos blocos
        self.out_period = Label(self.params, text='Período', bg=default.bg_color)
        self.out_period.place(x=position_block_params + 10, y=position_block_params - 10)

        # campos dos blocos
        # empresa
        position_init_params_x = 10
        position_init_params_y = position_block_params

        self.init_date = StringVar()
        self.end_date = StringVar()

        self.to = Label(self.params_period, text='a', width=2, bg=default.bg_color, anchor=default.label_just)
        self.to.place(x=position_init_params_x + 140, y=position_init_params_y)

        self.in_init_date = Entry(self.params_period, textvariable=self.init_date, width=10, bd=default.thickness_border, justify=default.entry_just)
        self.in_init_date.place(x=position_init_params_x + 60, y=position_init_params_y)
        self.in_end_date = Entry(self.params_period, textvariable=self.end_date, width=10, bd=default.thickness_border, justify=default.entry_just)
        self.in_end_date.place(x=position_init_params_x + 180, y=position_init_params_y)

        self.generate = Button(self.params, text='Gerar', width=12, bg=default.bg_color)
        self.generate.place(x=position_init_params_x + 120, y=position_init_params_y + (default.lines_space * 2))

        # atalhos
        #self.in_company_cnpj.bind('<F9>', lambda e: e * 2)

        # posicao inicial cursor
        self.in_init_date.focus()