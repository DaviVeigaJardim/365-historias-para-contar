from tkinter import *
from tkinter import ttk

class Application:
    def __init__(self, master):
        self.root = master
        self.window_config()
        self.quadros_da_tela()
        self.widgets()
        self.combobox()
        self.root.mainloop()

    def quadros_da_tela(self):
        self.frame_1 = Frame(self.root, bd=4, bg='#DDA0DD',
                             highlightbackground='#D8BFD8', highlightthickness=3)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.15)

        self.frame_2 = Frame(self.root, bd=4, bg='#DDA0DD',
                             highlightbackground='#D8BFD8', highlightthickness=3)
        self.frame_2.place(relx=0.02, rely=0.2, relwidth=0.96, relheight=0.76)

    def window_config(self):
        self.root.configure(background='#DA70D6')
        self.root.title("Contador de histórias")
        self.root.geometry('600x600')
        self.root.resizable(True, True)

    def widgets(self):
        self.play_clicked = False  

        self.bt_play = Button(self.frame_1, text='PLAY\ \nPAUSE', bd=3, bg='#DA70D6', fg='white', font=('verdana', 10, 'bold'), command=self.reproduzir_historia)
        self.bt_play.place(relx=0.01, rely=0.1, relheight=0.6, relwidth=0.2)

        self.bt_random = Button(self.frame_2, text=' reprodução \n aleatoria', bd=2, bg='#DA70D6', fg='white', font=('verdana', 10, 'bold'))
        self.bt_random.place(relx=0.01, rely=0.1, relheight=0.10, relwidth=0.2)

        self.bt_sequential = Button(self.frame_2, text='reprodução \n sequencial', bd=2, bg='#DA70D6', fg='white', font=('verdana', 10, 'bold'))
        self.bt_sequential.place(relx=0.01, rely=0.3, relheight=0.10, relwidth=0.2)

        self.label_mensagem = Label(self.frame_2, text='', font=('verdana', 12, 'bold'), bg='#DDA0DD')
        self.label_mensagem.place(relx=0.25, rely=0.5)

    def combobox(self):
        valores_dias = list(range(1, 31))
        self.combo_dias = ttk.Combobox(self.frame_1, values=valores_dias)
        self.combo_dias.set('Dia')
        self.combo_dias.place(relx=0.3, rely=0.1, relheight=0.6, relwidth=0.1)

        valores_mes = list(range(1, 13))
        self.combo_meses = ttk.Combobox(self.frame_1, values=valores_mes)
        self.combo_meses.set('Mês')
        self.combo_meses.place(relx=0.5, rely=0.1, relheight=0.6, relwidth=0.1)

    def reproduzir_historia(self):
        if not self.play_clicked:
            self.label_mensagem.config(text='Reproduzindo história...')
            self.label_mensagem.place(relx = 0.4, rely = 0.3)
            self.play_clicked = True


root = Tk()
app = Application(root)