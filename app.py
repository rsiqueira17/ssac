from tkinter import *
from gui_.home import Os_Window
from gui_.custom import Custom_GUI
from gui_.configuration import Company_Window
from gui_.smtp import SMTP_Window
from gui_.reports import Reports_Window


# funcoes para chamadas as janelas adicionais
def run_configuration(master):
    Company_Window(master)


def run_smtp(master):
    SMTP_Window(master)


def run_report_invoicing(master):
    over_window = Reports_Window(master)

    over_window.window.title('Relatório de faturamento')

    over_window.generate.command = lambda: print('Hello Universe!')


# bloco main
def main():
    # objeto principal da GUI
    app = Tk()
    app.title('Simple Solutions AutoCenter')

    # objeto de padronizacao da GUI
    default = Custom_GUI()

    # cor de fundo da janela
    app.configure(bg=default.bg_window_color)

    # calculo do tamanho da janela em relacao a tela
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()

    window_width = default.window_width
    window_height = default.window_height

    # posicao da janela ao inicializar
    position_x = (screen_width / 2) - (window_width / 2)
    position_y = (screen_height / 2) - (window_height / 2)

    app.geometry("%dx%d+%d+%d" % (window_width, window_height, position_x, position_y))
    #app.state('zoomed')
    #app.resizable(False, False)

    # favicon
    #app.iconbitmap('image.ico')

    # carrega os elementos na janela
    Os_Window(app)

    # barra de menus
    menu_bar = Menu(app)
    app.config(menu=menu_bar)
    
    config = Menu(menu_bar, tearoff=False)
    reports = Menu(menu_bar, tearoff=False)
    
    menu_bar.add_cascade(label='Configurações', menu=config)
    menu_bar.add_cascade(label='Relatórios', menu=reports)

    config.add_command(label='Empresa', command=lambda: run_configuration(app))
    config.add_command(label='SMTP', command=lambda: run_smtp(app))
    reports.add_command(label='Faturamento', command=lambda: run_report_invoicing(app))

    # mantem a janela em execucao
    app.mainloop()


# execucao
if __name__ == '__main__':
    main()