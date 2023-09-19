# classe template para cadastro de clientes

class Custom_GUI():
    def __init__(self, **kwargs):
        self.window_width = 1020
        self.window_height = 720
        self.bg_window_color = 'grey'
        self.bg_mainframe_color = 'lightgrey'
        self.bg_color = 'white'
        self.font = ''
        self.lines_height = '' # altura dos widgets nas linhas
        self.lines_space = 25 # intervalo de espaco entre os widgets de uma linha para outra
        self.thickness_border = 2 # espessura de linhas de borda dos widgets
        self.thickness_border_frames = 1 # espessura de linhas de borda dos frames/blocos
        self.label_size = 15
        self.label_just = 'e'
        self.entry_just = 'left'
        self.entry_just_number = 'right'