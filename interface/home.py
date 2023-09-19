from threading import Thread
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from interface.custom import Custom_GUI
from interface.grid import Grid_Window
from class_.client import Client
from class_.service_order import Service_Order
from class_.service_order_item import Service_Order_Item
import features.viacep_api as viacep
import database.interactionsdb as db
import configparser


class Os_Window():
    def __init__(self, master):
        # objeto da janela principal
        self.master = master

        # objeto de padronizacao do tema
        default = Custom_GUI()

        # blocos de cadastros
        position_block_head = 10
        position_block_os = position_block_head + 50 # 60
        position_block_customer = position_block_os + 50 # 110
        position_block_vehicle = position_block_customer + 150 # 260
        position_block_items = position_block_vehicle + 100 # 360
        position_block_summary = position_block_items + 310 # 670

        self.head = Frame(self.master, width=1000, height=40, bg=default.bg_color, bd=default.thickness_border_frames, relief='ridge').place(x=10, y=position_block_head)
        self.os = Frame(self.master, width=1000, height=600, bg=default.bg_color, bd=default.thickness_border_frames, relief='ridge').place(x=10, y=position_block_os)
        self.customer = Frame(self.os, width=980, height=140, bg=default.bg_color, bd=default.thickness_border_frames, relief='raised').place(x=20, y=position_block_customer)
        self.vehicle = Frame(self.os, width=980, height=90, bg=default.bg_color, bd=default.thickness_border_frames, relief='raised').place(x=20, y=position_block_vehicle)
        self.items = Frame(self.os, width=980, height=190, bg=default.bg_color, bd=default.thickness_border_frames, relief='raised').place(x=20, y=position_block_items)
        self.summary = Frame(self.master, width=1000, height=40, bg=default.bg_color, bd=default.thickness_border_frames, relief='ridge').place(x=10, y=position_block_summary)

        # identificacao dos blocos
        Label(self.os, text='Cliente', bg=default.bg_color).place(x=40, y=position_block_customer - 10)
        Label(self.os, text='Veículo', bg=default.bg_color).place(x=40, y=position_block_vehicle - 10)
        Label(self.os, text='Produtos/Serviços', bg=default.bg_color).place(x=40, y=position_block_items - 10)

        # campos dos blocos
        # cabecalho
        position_init_head_x = 15
        position_init_head_y = position_block_head + 10
        logo = PhotoImage(file='./images/logoempresa.png')
        logo.subsample(6,6)

        self.logo_head = Frame(self.head, width=150, height=40, relief='ridge')
        self.logo_head.pack_propagate(0)
        self.logo_head.place(x=position_init_head_x, y=position_init_head_y - 10)

        Label(self.logo_head, image=logo).pack() #place(x=0, y=0)
        Label(self.head, text='Auto Center: Hercules LTDA.', font='Helvetica-bold 14', bg=default.bg_color).place(x=400, y=position_init_head_y)

        # soma-se 115 na posicao x da entry em relacao a posicao do label
        # os
        position_init_os_x = 25
        position_init_os_y = position_block_os + 10 # 70

        self.number_os = StringVar()
        self.date_os = StringVar()
        self.technician_os = StringVar()
        self.approved_os = BooleanVar()
        self.approved_os.set(False)
        self.concluded_os = BooleanVar()
        self.concluded_os.set(False)
        self.value_os = StringVar()

        Label(self.os, text='Número', bg=default.bg_color, width=default.label_size, anchor=default.label_just).place(x=position_init_os_x, y=position_init_os_y)
        Label(self.os, text='Data', bg=default.bg_color, width=default.label_size, anchor=default.label_just).place(x=330, y=position_init_os_y)
        Label(self.os, text='Técnico', bg=default.bg_color, width=default.label_size, anchor=default.label_just).place(x=600, y=position_init_os_y)
        Label(self.os, text='Aprovado', bg=default.bg_color, width=default.label_size, anchor=default.label_just).place(x=position_init_os_x, y=position_init_os_y + (default.lines_space * 20))
        Label(self.os, text='Concluído', bg=default.bg_color, width=default.label_size, anchor=default.label_just).place(x=250, y=position_init_os_y + (default.lines_space * 20))
        Label(self.os, text='Valor total', bg=default.bg_color, width=default.label_size, anchor=default.label_just).place(x=750, y=position_init_os_y + (default.lines_space * 20))

        self.in_os_number = Entry(self.os, width=10, textvariable=self.number_os, bd=default.thickness_border, justify='left')
        self.in_os_number.place(x=position_init_os_x + 115, y=position_init_os_y)
        
        self.in_os_date = Entry(self.os, width=10, textvariable=self.date_os, bd=default.thickness_border, justify='left').place(x=445, y=position_init_os_y)
        self.in_os_technician = Entry(self.os, width=30, textvariable=self.technician_os, bd=default.thickness_border, justify='left').place(x=715, y=position_init_os_y)
        self.in_os_budget = Checkbutton(self.os, variable=self.approved_os, bd=default.thickness_border, onvalue=True, offvalue=False, bg=default.bg_color).place(x=position_init_os_x + 115, y=position_init_os_y + (default.lines_space * 20))
        self.in_os_budget = Checkbutton(self.os, variable=self.concluded_os, bd=default.thickness_border, onvalue=True, offvalue=False, bg=default.bg_color).place(x=365, y=position_init_os_y + (default.lines_space * 20))
        self.in_os_value = Entry(self.os, width=18, textvariable=self.value_os, bd=default.thickness_border, justify='right').place(x=865, y=position_init_os_y + (default.lines_space * 20))

        searchicon = PhotoImage(file='./images/search.png')
        #Button(self.os, image=searchicon, bg=default.bg_color).place(x=position_init_os_x + 180, y=position_init_os_y, )
        Button(self.os, text='Consultar', bg=default.bg_color, height=0, bd=0, command=self.__run_grid).place(x=position_init_os_x + 180, y=position_init_os_y - 2)
        Button(self.os, text='Excluir', bg=default.bg_color, width=12).place(x=position_init_os_x, y=position_init_os_y + (default.lines_space * 22))
        Button(self.os, text='Gerar PDF', bg=default.bg_color, width=12).place(x=750, y=position_init_os_y + (default.lines_space * 22))
        Button(self.os, text='Gravar', bg=default.bg_color, width=12, command=self.__record).place(x=865, y=position_init_os_y + (default.lines_space * 22))
        Button()

        # cliente
        position_init_customer_x = 40
        position_init_customer_y = position_block_customer + 10 # 120

        self.customer_doc = StringVar()
        self.customer_name = StringVar()
        self.customer_phone = StringVar()
        self.customer_email = StringVar()
        self.customer_postcode = StringVar()
        self.customer_address = StringVar()
        self.customer_address_number = StringVar()
        self.customer_address_compl = StringVar()
        self.customer_address_neigh = StringVar()
        self.customer_address_city = StringVar()
        
        Label(self.customer, text='CPF/CNPJ', bg=default.bg_color, width=default.label_size, anchor=default.label_just).place(x=position_init_customer_x, y=position_init_customer_y)
        Label(self.customer, text='Nome', bg=default.bg_color, width=default.label_size, anchor=default.label_just).place(x=600, y=position_init_customer_y)
        Label(self.customer, text='Celular', bg=default.bg_color, width=default.label_size, anchor=default.label_just).place(x=position_init_customer_x, y=position_init_customer_y + (default.lines_space * 1))
        Label(self.customer, text='E-mail', bg=default.bg_color, width=default.label_size, anchor=default.label_just).place(x=600, y=position_init_customer_y + (default.lines_space * 1))
        Label(self.customer, text='Cep', bg=default.bg_color, width=default.label_size, anchor=default.label_just).place(x=position_init_customer_x, y=position_init_customer_y + (default.lines_space * 2))
        Label(self.customer, text='Endereço', bg=default.bg_color, width=default.label_size, anchor=default.label_just).place(x=600, y=position_init_customer_y + (default.lines_space * 2))
        Label(self.customer, text='Número', bg=default.bg_color, width=default.label_size, anchor=default.label_just).place(x=position_init_customer_x, y=position_init_customer_y + (default.lines_space * 3))
        Label(self.customer, text='Complemento', bg=default.bg_color, width=default.label_size, anchor=default.label_just).place(x=600, y=position_init_customer_y + (default.lines_space * 3))
        Label(self.customer, text='Bairro', bg=default.bg_color, width=default.label_size, anchor=default.label_just).place(x=position_init_customer_x, y=position_init_customer_y + (default.lines_space * 4))
        Label(self.customer, text='Cidade', bg=default.bg_color, width=default.label_size, anchor=default.label_just).place(x=600, y=position_init_customer_y + (default.lines_space * 4))

        self.in_customer_doc = Entry(self.customer, width=14, textvariable=self.customer_doc, bd=default.thickness_border, justify='left').place(x=position_init_customer_x + 115, y=position_init_customer_y)
        self.in_customer_name = Entry(self.customer, width=40, textvariable=self.customer_name, bd=default.thickness_border, justify='left').place(x=715, y=position_init_customer_y)
        self.in_customer_phone = Entry(self.customer, width=14, textvariable=self.customer_phone, bd=default.thickness_border, justify='left').place(x=position_init_customer_x + 115, y=position_init_customer_y + (default.lines_space * 1))
        self.in_customer_email = Entry(self.customer, width=30, textvariable=self.customer_email, bd=default.thickness_border, justify='left').place(x=715, y=position_init_customer_y + (default.lines_space * 1))

        self.in_customer_postcode = Entry(self.customer, width=9, textvariable=self.customer_postcode, bd=default.thickness_border, justify='left')
        self.in_customer_postcode.place(x=position_init_customer_x + 115, y=position_init_customer_y + (default.lines_space * 2))

        self.in_customer_address = Entry(self.customer, width=40, textvariable=self.customer_address, bd=default.thickness_border, justify='left').place(x=715, y=position_init_customer_y + (default.lines_space * 2))

        self.in_customer_address_number = Entry(self.customer, width=10, textvariable=self.customer_address_number, bd=default.thickness_border, justify='left')
        self.in_customer_address_number.place(x=position_init_customer_x + 115, y=position_init_customer_y + (default.lines_space * 3))

        self.in_customer_address_compl = Entry(self.customer, width=30, textvariable=self.customer_address_compl, bd=default.thickness_border, justify='left').place(x=715, y=position_init_customer_y + (default.lines_space * 3))
        self.in_customer_address_neigh = Entry(self.customer, width=30, textvariable=self.customer_address_neigh, bd=default.thickness_border, justify='left').place(x=position_init_customer_x + 115, y=position_init_customer_y + (default.lines_space * 4))
        self.in_customer_address_city = Entry(self.customer, width=30, textvariable=self.customer_address_city, bd=default.thickness_border, justify='left').place(x=715, y=position_init_customer_y + (default.lines_space * 4))

        # veiculo
        position_init_vehicle_x = 40
        position_init_vehicle_y = position_block_vehicle + 10 # 270

        self.vehicle_model = StringVar()
        self.vehicle_plate = StringVar()
        self.vehicle_version = StringVar()
        self.vehicle_manuf = StringVar()
        self.vehicle_year = StringVar()
        self.vehicle_km = StringVar()
        
        Label(self.vehicle, text='Modelo', bg=default.bg_color, width=default.label_size, anchor=default.label_just).place(x=position_init_vehicle_x, y=position_init_vehicle_y)
        Label(self.vehicle, text='Placa', bg=default.bg_color, width=default.label_size, anchor=default.label_just).place(x=600, y=position_init_vehicle_y)
        Label(self.vehicle, text='Versão', bg=default.bg_color, width=default.label_size, anchor=default.label_just).place(x=position_init_vehicle_x, y=position_init_vehicle_y + (default.lines_space * 1))
        Label(self.vehicle, text='Fabricante', bg=default.bg_color, width=default.label_size, anchor=default.label_just).place(x=600, y=position_init_vehicle_y + (default.lines_space * 1))
        Label(self.vehicle, text='Ano', bg=default.bg_color, width=default.label_size, anchor=default.label_just).place(x=position_init_vehicle_x, y=position_init_vehicle_y + (default.lines_space * 2))
        Label(self.vehicle, text='Kilometragem', bg=default.bg_color, width=default.label_size, anchor=default.label_just).place(x=600, y=position_init_vehicle_y + (default.lines_space * 2))

        self.in_vehicle_model = Entry(self.vehicle, width=30, textvariable=self.vehicle_model, bd=default.thickness_border, justify='left').place(x=position_init_vehicle_x + 115, y=position_init_vehicle_y)
        self.in_vehicle_plate = Entry(self.vehicle, width=8, textvariable=self.vehicle_plate, bd=default.thickness_border, justify='left').place(x=715, y=position_init_vehicle_y)
        self.in_vehicle_version = Entry(self.vehicle, width=30, textvariable=self.vehicle_version, bd=default.thickness_border, justify='left').place(x=position_init_vehicle_x + 115, y=position_init_vehicle_y + (default.lines_space * 1))
        self.in_vehicle_manuf = Entry(self.vehicle, width=20, textvariable=self.vehicle_manuf, bd=default.thickness_border, justify='left').place(x=715, y=position_init_vehicle_y + (default.lines_space * 1))
        self.in_vehicle_year = Entry(self.vehicle, width=4, textvariable=self.vehicle_year, bd=default.thickness_border, justify='left').place(x=position_init_vehicle_x + 115, y=position_init_vehicle_y + (default.lines_space * 2))
        self.in_vehicle_km = Entry(self.vehicle, width=7, textvariable=self.vehicle_km, bd=default.thickness_border, justify='left').place(x=715, y=position_init_vehicle_y + (default.lines_space * 2))

        # itens os
        # correcao de estilo da treeview
        self.style = ttk.Style()
        self.style.map('Treeview', foreground=self.fixed_map('foreground'), background=self.fixed_map('background'))

        position_init_items_x = 30
        position_init_items_y = position_block_items + 10 # 370
        self.description_item = StringVar()
        self.value_item = StringVar()
        self.quantity_item = IntVar()
        self.percent_item = IntVar()

        Label(self.items, text='Descrição', bg=default.bg_color).place(x=position_init_items_x, y=position_init_items_y)
        Label(self.items, text='Valor unitário', bg=default.bg_color).place(x=position_init_items_x, y=position_init_items_y + 40)
        Label(self.items, text='Quantidade', bg=default.bg_color).place(x=position_init_items_x, y=position_init_items_y + 80)
        Label(self.items, text='Percentual venda', bg=default.bg_color).place(x=position_init_items_x + 125, y=position_init_items_y + 80)

        self.in_description_item = Entry(self.items, textvariable=self.description_item, width=35, bd=default.thickness_border, justify='left')
        self.in_description_item.place(x=position_init_items_x, y=position_init_items_y + 20)

        self.in_value_item = Entry(self.items, textvariable=self.value_item, width=30, bd=default.thickness_border, justify='right').place(x=position_init_items_x, y=position_init_items_y + 40 + 20)
        self.in_quantity_item = Entry(self.items, textvariable=self.quantity_item, width=15, bd=default.thickness_border, justify='right').place(x=position_init_items_x, y=position_init_items_y + 80 + 20)
        self.in_percent_item = Entry(self.items, textvariable=self.percent_item, width=15, bd=default.thickness_border, justify='right').place(x=position_init_items_x + 125, y=position_init_items_y + 80 + 20)

        Button(self.items, text='Inserir', bg='lightgreen', width=8, command=self.__insert_treeview_item).place(x=position_init_items_x, y=position_init_items_y + 140)
        Button(self.items, text='Limpar', bg='White', width=8, command=self.__clear_item_fields).place(x=position_init_items_x + 80, y=position_init_items_y + 140)
        Button(self.items, text='Remover', bg='Pink', width=8, command='').place(x=position_init_items_x + 160, y=position_init_items_y + 140)

        columns = [
            ('Descrição', 402, 'w'),
            ('Valor', 100, 'e'),
            ('Quantidade', 80, 'e'),
            ('Total item', 100, 'e')
        ]
        self.items_frame = Frame(self.items)
        self.items_frame.place(x=position_init_items_x + 250, y=position_init_items_y)

        self.items_list = ttk.Treeview(self.items_frame, columns=columns, show='headings', selectmode='extended', height=7)
        self.items_scroll = Scrollbar(self.items_frame, orient='vertical', command=self.items_list.yview)
        self.items_scroll.pack(side='right', fill='y')
        self.items_list.configure(yscrollcommand=self.items_scroll.set)

        for index, column in enumerate(columns):
            self.items_list.heading(index, text=column[0], anchor='w')
            self.items_list.column(index, width=column[1], anchor=column[2])

        self.items_list.pack() # place(x=100, y=position_init_items)

        # resumo rodape
        position_init_summary_x = 30
        position_init_summary_y = position_block_summary + 10 # 680

        self.summary_concluded = Label(self.summary, text="OS's Pendentes", bg=default.bg_color, fg='Red').place(x=position_init_summary_x + 70, y=position_init_summary_y)
        self.summary_approved = Label(self.summary, text="OS's Aprovadas/Em andamento", bg=default.bg_color, fg='Blue').place(x=position_init_summary_x + 380, y=position_init_summary_y)
        self.summary_pending = Label(self.summary, text="OS's Concluídas", bg=default.bg_color, fg='Green').place(x=position_init_summary_x + 800, y=position_init_summary_y)

        # atalhos
        self.in_customer_postcode.bind('<Return>', self.__search_cep_data)
        self.in_customer_postcode.bind('<Tab>', self.__search_cep_data)

        # posicao inicial cursor
        self.in_os_number.focus()


    def __run_grid(self):
        Grid_Window(self.master, ('Descrição', 150, 'e'))


    # checar viabilidade de gravar o valor sem a aplicacao do percentual de venda e usa-lo como custo do produto
    def __insert_treeview_item(self):
        # transformacoes
        percent_item = 1 + (self.percent_item.get() / 100)
        value = float(self.value_item.get().replace(',', '.')) * percent_item
        total_value = value * self.quantity_item.get()

        # indice atual do treeview
        sequence = len(self.items_list.get_children(''))

        registry = (
            self.description_item.get(),
            value,
            self.quantity_item.get(),
            total_value,
            self.percent_item.get()
        )

        self.items_list.insert('', 'end', iid=sequence, values=registry)

        # calcula o valor total da OS e atualiza o campo correspondente
        self.__calc_total_value(total_value)
        # limpa os campos apos a insercao
        self.__clear_item_fields()

        return


    def __clear_item_fields(self):
        self.description_item.set('')
        self.value_item.set('')
        self.quantity_item.set(0)
        self.percent_item.set(0)

        # reposiciona o cursos para mais insercoes
        self.in_description_item.focus()

        return


    def __calc_total_value(self, sum_value):
        # se o campo estiver em branco, zera o valor parcial para usa-lo na operacao matematica seguinte
        try:
            partial = float(self.value_os.get().replace(',', '.'))
        except ValueError:
            partial = 0

        self.value_os.set(partial + sum_value)

        return


    def __record(self):
        client = Client(
            self.customer_doc.get(),
            self.customer_name.get(),
            self.customer_phone.get(),
            self.customer_email.get(),
            self.customer_postcode.get(),
            self.customer_address.get(),
            self.customer_address_number.get(),
            self.customer_address_compl.get(),
            self.customer_address_neigh.get(),
            self.customer_address_city.get()
        )

        # transformacoes dados os
        number_os = int(self.number_os.get())
        date_os = '-'.join(self.date_os.get().split('/')[::-1])
        vehicle_year = int(self.vehicle_year.get())
        vehicle_km = int(self.vehicle_km.get().replace('.',''))
        value_os = float(self.value_os.get().replace('.', '').replace(',', '.'))

        os = Service_Order(
            number_os,
            date_os,
            self.technician_os.get(),
            self.customer_doc.get(),
            self.vehicle_model.get(),
            self.vehicle_plate.get(),
            self.vehicle_version.get(),
            self.vehicle_manuf.get(),
            vehicle_year,
            vehicle_km,
            self.approved_os.get(),
            self.concluded_os.get(),
            value_os
        )

        # grava os dados
        db.new_customer(client)
        os_code = db.new_os(os)

        # captura os dados das linhas da treeview e converte-os em objetos da classe Service_Ordem_Items
        os_items = self.__get_treeview_list(os_code)

        for item in os_items:
            db.new_os_item(item)

        return


    def __get_treeview_list(self, os_code):
        # retorna a id de cada item dentro do nó principal da treeview
        items = self.items_list.get_children('')

        os_items = []

        # itera sobre os itens da treeview e cria um objeto da classe Service_Order_Item para cada um deles
        for sequence, index in enumerate(items, start=1):
            index = int(index)

            description = self.items_list.item(index)['values'][0]
            unit_value = self.items_list.item(index)['values'][1]
            quantity = self.items_list.item(index)['values'][2]
            sale_percent = self.items_list.item(index)['values'][4]

            os_items.append(Service_Order_Item(os_code, sequence, description, unit_value, quantity, sale_percent))

        return os_items
    

    def __search_cep_data(self, event):
        _, public_place, address, neigh, city, _, _ = viacep.get(self.customer_postcode.get())

        self.customer_address.set(f'{public_place} {address}')
        self.customer_address_neigh.set(neigh)
        self.customer_address_city.set(city)

        # reposiciona o foco do cursor para o numero do endereco para continuar com o cadastro
        self.in_customer_address_number.focus()

        return

    # correcao para a coloração de linhas no treeview
    def fixed_map(self, option):
        # Fix for setting text colour for Tkinter 8.6.9
        # From: https://core.tcl.tk/tk/info/509cafafae
        #
        # Returns the style map for 'option' with any styles starting with
        # ('!disabled', '!selected', ...) filtered out.

        # style.map() returns an empty list for missing options, so this
        # should be future-safe.
        return [elm for elm in self.style.map('Treeview', query_opt=option) if elm[:2] != ('!disabled', '!selected')]