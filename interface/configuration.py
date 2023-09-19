from threading import Thread
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from interface.custom import Custom_GUI


class Company_Window():
    def __init__(self, master):
        # objeto da janela de configuracao
        self.master = master
        self.window = Toplevel()

        self.window.title("Configuração empresa")

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
        window_width = 800
        window_height = 400

        # posicao da janela ao inicializar
        position_x = (screen_width / 2) - (window_width / 2)
        position_y = (screen_height / 2) - (window_height / 2)

        self.window.geometry("%dx%d+%d+%d" % (window_width, window_height, position_x, position_y))

        # blocos de cadastros
        position_block_config = 10
        position_block_company = position_block_config
        position_block_guarantee = position_block_company + 180 # 50
        position_block_params = position_block_guarantee + 60 # 80

        self.config = Frame(self.window, width=780, height=380, bg=default.bg_color, bd=default.thickness_border_frames, relief='ridge')
        self.config.place(x=10, y=position_block_config)
        self.company = Frame(self.config, width=760, height=170, bg=default.bg_color, bd=default.thickness_border, relief='groove')
        self.company.place(x=10, y=position_block_company)
        self.guarantee = Frame(self.config, width=760, height=50, bg=default.bg_color, bd=default.thickness_border, relief='groove')
        self.guarantee.place(x=10, y=position_block_guarantee)
        self.params = Frame(self.config, width=760, height=120, bg=default.bg_color, bd=default.thickness_border, relief='groove')
        self.params.place(x=10, y=position_block_params)

        # identificacao dos blocos
        self.out_company = Label(self.config, text='Empresa', bg=default.bg_color)
        self.out_company.place(x=25, y=position_block_company - 10)
        self.out_ganrantee = Label(self.config, text='Garantia', bg=default.bg_color)
        self.out_ganrantee.place(x=25, y=position_block_guarantee - 10)
        self.out_params = Label(self.config, text='Parâmetros gerais', bg=default.bg_color)
        self.out_params.place(x=25, y=position_block_params - 10)

        self.record = Button(self.config, text='Gravar', width=12, bg=default.bg_color, command='')
        self.record.place(x=position_block_config + 650, y=position_block_config + (default.lines_space * 13))

        # campos dos blocos
        # empresa
        position_init_company_x = 5
        position_init_company_y = position_block_company

        self.company_cnpj = StringVar()
        self.company_name = StringVar()
        self.company_email = StringVar()
        self.company_phone = StringVar()
        self.company_cellphone1 = StringVar()
        self.company_cellphone2 = StringVar()
        self.company_address = StringVar()
        self.company_number = StringVar()
        self.company_compl = StringVar()
        self.company_neigh = StringVar()
        self.company_city = StringVar()
        self.company_uf = StringVar()

        self.out_company_cnpj = Label(self.company, text='CNPJ', width=default.label_size, bg=default.bg_color, anchor=default.label_just)
        self.out_company_cnpj.place(x=position_init_company_x, y=position_init_company_y)
        self.out_company_name = Label(self.company, text='Razão social', width=default.label_size, bg=default.bg_color, anchor=default.label_just)
        self.out_company_name.place(x=position_init_company_x + 350, y=position_init_company_y)
        self.out_company_email = Label(self.company, text='E-mail', width=default.label_size, bg=default.bg_color, anchor=default.label_just)
        self.out_company_email.place(x=position_init_company_x, y=position_init_company_y + default.lines_space)
        self.out_company_phone = Label(self.company, text='Telefone', width=default.label_size, bg=default.bg_color, anchor=default.label_just)
        self.out_company_phone.place(x=position_init_company_x + 350, y=position_init_company_y + default.lines_space)
        self.out_company_cellphone1 = Label(self.company, text='Celular', width=default.label_size, bg=default.bg_color, anchor=default.label_just)
        self.out_company_cellphone1.place(x=position_init_company_x, y=position_init_company_y + (default.lines_space * 2))
        self.out_company_cellphone2 = Label(self.company, text='Celular', width=default.label_size, bg=default.bg_color, anchor=default.label_just)
        self.out_company_cellphone2.place(x=position_init_company_x + 350, y=position_init_company_y + (default.lines_space * 2))
        self.out_company_address = Label(self.company, text='Endereço', width=default.label_size, bg=default.bg_color, anchor=default.label_just)
        self.out_company_address.place(x=position_init_company_x, y=position_init_company_y + (default.lines_space * 3))
        self.out_company_number = Label(self.company, text='Número', width=default.label_size, bg=default.bg_color, anchor=default.label_just)
        self.out_company_number.place(x=position_init_company_x + 350, y=position_init_company_y + (default.lines_space * 3))
        self.out_company_compl = Label(self.company, text='Complemento', width=default.label_size, bg=default.bg_color, anchor=default.label_just)
        self.out_company_compl.place(x=position_init_company_x, y=position_init_company_y + (default.lines_space * 4))
        self.out_company_neigh = Label(self.company, text='Bairro', width=default.label_size, bg=default.bg_color, anchor=default.label_just)
        self.out_company_neigh.place(x=position_init_company_x + 350, y=position_init_company_y + (default.lines_space * 4))
        self.out_company_city = Label(self.company, text='Cidade', width=default.label_size, bg=default.bg_color, anchor=default.label_just)
        self.out_company_city.place(x=position_init_company_x, y=position_init_company_y + (default.lines_space * 5))
        self.out_company_uf = Label(self.company, text='UF', width=default.label_size, bg=default.bg_color, anchor=default.label_just)
        self.out_company_uf.place(x=position_init_company_x + 350, y=position_init_company_y + (default.lines_space * 5))

        self.in_company_cnpj = Entry(self.company, textvariable=self.company_cnpj, width=18, bd=default.thickness_border, justify=default.entry_just)
        self.in_company_cnpj.place(x=position_init_company_x + 115, y=position_init_company_y)
        self.in_company_name = Entry(self.company, textvariable=self.company_name, width=40, bd=default.thickness_border, justify=default.entry_just)
        self.in_company_name.place(x=position_init_company_x + 465, y=position_init_company_y)
        self.in_company_email = Entry(self.company, textvariable=self.company_email, width=30, bd=default.thickness_border, justify=default.entry_just)
        self.in_company_email.place(x=position_init_company_x + 115, y=position_init_company_y + default.lines_space)
        self.in_company_phone = Entry(self.company, textvariable=self.company_phone, width=13, bd=default.thickness_border, justify=default.entry_just)
        self.in_company_phone.place(x=position_init_company_x + 465, y=position_init_company_y + default.lines_space)
        self.in_company_cellphone1 = Entry(self.company, textvariable=self.company_cellphone1, width=14, bd=default.thickness_border, justify=default.entry_just)
        self.in_company_cellphone1.place(x=position_init_company_x + 115, y=position_init_company_y + (default.lines_space * 2))
        self.in_company_cellphone2 = Entry(self.company, textvariable=self.company_cellphone2, width=14, bd=default.thickness_border, justify=default.entry_just)
        self.in_company_cellphone2.place(x=position_init_company_x + 465, y=position_init_company_y + (default.lines_space * 2))
        self.in_company_address = Entry(self.company, textvariable=self.company_address, width=40, bd=default.thickness_border, justify=default.entry_just)
        self.in_company_address.place(x=position_init_company_x + 115, y=position_init_company_y + (default.lines_space * 3))
        self.in_company_number = Entry(self.company, textvariable=self.company_number, width=10, bd=default.thickness_border, justify=default.entry_just)
        self.in_company_number.place(x=position_init_company_x + 465, y=position_init_company_y + (default.lines_space * 3))
        self.in_company_compl = Entry(self.company, textvariable=self.company_compl, width=30, bd=default.thickness_border, justify=default.entry_just)
        self.in_company_compl.place(x=position_init_company_x + 115, y=position_init_company_y + (default.lines_space * 4))
        self.in_company_neigh = Entry(self.company, textvariable=self.company_neigh, width=30, bd=default.thickness_border, justify=default.entry_just)
        self.in_company_neigh.place(x=position_init_company_x + 465, y=position_init_company_y + (default.lines_space * 4))
        self.in_company_city = Entry(self.company, textvariable=self.company_city, width=30, bd=default.thickness_border, justify=default.entry_just)
        self.in_company_city.place(x=position_init_company_x + 115, y=position_init_company_y + (default.lines_space * 5))
        self.in_company_uf = Entry(self.company, textvariable=self.company_uf, width=2, bd=default.thickness_border, justify=default.entry_just)
        self.in_company_uf.place(x=position_init_company_x + 465, y=position_init_company_y + (default.lines_space * 5))

        # soma-se 115 na posicao x da entry em relacao a posicao do label
        # garantia
        position_init_guarantee_x = 5
        position_init_guarantee_y = 10

        self.km = StringVar()
        self.time = IntVar()
        self.type = StringVar()
        self.type_box = ('Dias', 'Semanas', 'Meses', 'Anos')

        self.out_km = Label(self.guarantee, text='Kilometragem', bg=default.bg_color, width=default.label_size, anchor=default.label_just)
        self.out_km.place(x=position_init_guarantee_x, y=position_init_guarantee_y)
        self.out_time = Label(self.guarantee, text='Tempo', bg=default.bg_color, width=default.label_size, anchor=default.label_just)
        self.out_time.place(x=position_init_guarantee_x + 350, y=position_init_guarantee_y)

        self.in_km = Entry(self.guarantee, textvariable=self.km, width=7, bd=default.thickness_border, justify=default.entry_just_number)
        self.in_km.place(x=position_init_guarantee_x + 115, y=position_init_guarantee_y)
        self.in_time = Entry(self.guarantee, textvariable=self.time, width=4, bd=default.thickness_border, justify=default.entry_just_number)
        self.in_time.place(x=position_init_guarantee_x + 465, y=position_init_guarantee_y)
        self.in_type = ttk.Combobox(self.guarantee, values=self.type_box, textvariable=self.type, width=8)
        self.in_type.place(x=position_init_guarantee_x + 505, y=position_init_guarantee_y)

        # parametro gerais
        position_init_params_x = 5
        position_init_params_y = 10

        self.number_init = IntVar()
        self.logo_file = StringVar()
        self.local_os = StringVar()
        self.extensions = [
            ('JPG', '.jpg'),
            ('JPG', '.jpeg'),
            ('PNG', '.png'),
            ('Bitmap', '.bmp'),
        ]
        
        self.out_number_init = Label(self.params, text='Número OS inicial', bg=default.bg_color, width=default.label_size, anchor=default.label_just)
        self.out_number_init.place(x=position_init_params_x, y=position_init_params_y)

        self.out_local_os = Label(self.params, text='Local geração OS', bg=default.bg_color, width=default.label_size, anchor=default.label_just)
        self.out_local_os.place(x=position_init_params_x + 350, y=position_init_params_y)

        self.out_logo_file= Label(self.params, text='Arquivo logo', bg=default.bg_color, width=default.label_size, anchor=default.label_just)
        self.out_logo_file.place(x=position_init_params_x, y=position_init_params_y + default.lines_space)

        self.in_number_init = Entry(self.params, textvariable=self.number_init, bd=default.thickness_border, width=10, justify=default.entry_just_number)
        self.in_number_init.place(x=position_init_params_x + 115, y=position_init_params_y)

        self.in_local_os = Entry(self.params, textvariable=self.local_os, bd=default.thickness_border, width=40, justify=default.entry_just)
        self.in_local_os.place(x=position_init_params_x + 465, y=position_init_params_y)

        self.in_logo_file = Entry(self.params, textvariable=self.logo_file, bd=default.thickness_border, width=40, justify=default.entry_just)
        self.in_logo_file.place(x=position_init_params_x + 115, y=position_init_params_y + default.lines_space)

        self.search_local = Button(self.params, text='...', width=1, bg=default.bg_color, command=lambda: self.local_os.set(filedialog.askdirectory() + '/'))
        self.search_local.place(x=position_block_config + 705, y=position_init_params_y - 2)

        self.search_file = Button(self.params, text='...', width=1, bg=default.bg_color, command=lambda: self.logo_file.set(filedialog.askopenfilenames(filetypes=self.extensions)[0]))
        self.search_file.place(x=position_block_config + 340, y=position_init_params_y + default.lines_space - 2)

        # atalhos
        #self.in_company_cnpj.bind('<F9>', lambda e: e * 2)

        # posicao inicial cursor
        self.in_company_cnpj.focus()