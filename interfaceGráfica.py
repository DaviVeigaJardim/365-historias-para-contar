from tkinter import *
from tkinter import ttk

class Application:
    def __init__(self, master):
        self.root = master
        self.window_config()
        self.frames_da_tela()
        self.widgets()
        self.combobox()
        self.root.mainloop()
        
    def frames_da_tela(self):
     self.frame_1 = Frame(self.root, bd=4, bg='#DDA0DD',
                         highlightbackground='#DDA0DD', highlightthickness=1)
     self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.15)
    #Posição das cordenadas do frame de cima 
    
     self.frame_2 = Frame(self.root, bd=4, bg='#DDA0DD',
                         highlightbackground='#DDA0DD', highlightthickness=1)
     self.frame_2.place(relx=0.02, rely=0.2, relwidth=0.96, relheight=0.76)
    #Posições das cordenadas do frame de baixo, se o rely for igual, haverá sobreposição
        
    def window_config(self):
        self.root.configure(background='#DA70D6')
        self.root.title("Contador de histórias")
        self.root.geometry('600x600')
        self.root.resizable(True, True)
    def widgets(self):
       #Botão de play
       self.bt_play = Button(self.frame_1, text= 'PLAY/PAUSE', bd = 2, bg = '#DA70D6', fg='white', font= ('verdana', 10, 'bold'))
       self.bt_play.place(relx= 0.1, rely= 0.1, relheight= 0.6, relwidth= 0.3)
       self.icone_play_pause = PhotoImage(file='IMAGENS/3002890-200.png')
       self.bt_play.config(image=self.icone_play, compound="left", command=self.funcao_do_botao)
       self.bt_play.image = self.icone_play
       
    def combobox(self):
        #combobox para selecionar história do dia
        valores_dias = list(range(1,31))
        self.combo_dias = ttk.Combobox(self.frame_1, values= valores_dias)
        self.combo_dias.set('Dia') #Mensagem que fica dentro da combobox
        self.combo_dias.place(relx=0.5, rely=0.1, relheight=0.6, relwidth=0.1)

        valores_mes = list(range(1,13))  
        self.combo_meses = ttk.Combobox (self.frame_1, values= valores_mes)
        self.combo_meses.set('Mês')
        self.combo_meses.place(relx = 0.7, rely = 0.1, relheight = 0.6, relwidth = 0.1)

        
     
root = Tk()
app = Application(root)