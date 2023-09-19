from threading import Thread
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from interface.custom import Custom_GUI


class Grid_Window():
    def __init__(self, master, *columns_params:list(tuple())):
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

        # tamanho da janela de configuracao
        window_width = 400
        window_height = 260

        # posicao da janela ao inicializar
        position_x = (screen_width / 2) - (window_width / 2)
        position_y = (screen_height / 2) - (window_height / 2)

        self.window.geometry("%dx%d+%d+%d" % (window_width, window_height, position_x, position_y))

        # blocos de cadastros
        position_block_filters = 10
        position_block_grid = position_block_filters + 50

        self.filters = Frame(self.window, width=380, height=40, bg=default.bg_color, bd=default.thickness_border_frames, relief='ridge')
        self.filters.place(x=10, y=position_block_filters)

        self.grid = Frame(self.window, width=380, height=190, bg=default.bg_color, bd=default.thickness_border_frames, relief='ridge')
        self.grid.place(x=10, y=position_block_grid)

        # campos dos blocos
        # filtros
        position_init_filters_x = 10
        position_init_filters_y = position_block_filters

        self.search = StringVar()
        logo_search = PhotoImage(file='./images/search.png')

        self.in_search = Entry(self.filters, textvariable=self.search, width=40, bd=default.thickness_border, justify=default.entry_just)
        self.in_search.place(x=position_init_filters_x, y=position_init_filters_y)

        self.run = Button(self.filters, image=logo_search, width=12, bg=default.bg_color)
        self.run.place(x=position_init_filters_x + 250, y=position_init_filters_y - 1)

        # grid
        position_init_grid_x = 0
        position_init_grid_y = 0

        self.grid_frame = Frame(self.grid)
        self.grid_frame.place(x=position_init_grid_x, y=position_init_grid_y)

        self.grid_list = ttk.Treeview(self.grid_frame, columns=columns_params, show='headings', selectmode='extended', height=8)
        self.grid_scroll = Scrollbar(self.grid_frame, orient='vertical', command=self.grid_list.yview)
        self.grid_scroll.pack(side='right', fill='y')
        self.grid_list.configure(yscrollcommand=self.grid_scroll.set)

        for index, column in enumerate(columns_params):
            self.grid_list.heading(index, text=column[0], anchor='w')
            self.grid_list.column(index, width=column[1], anchor=column[2])

        self.grid_list.pack() # place(x=100, y=position_init_items)

        # atalhos
        #self.in_company_cnpj.bind('<F9>', lambda e: e * 2)

        # posicao inicial cursor
        self.in_search.focus()