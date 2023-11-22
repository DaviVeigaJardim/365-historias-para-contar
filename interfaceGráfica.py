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
                         highlightbackground='#FF69B4', highlightthickness=3)
     self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.15)
    #Posição das cordenadas do frame de cima 
    
     self.frame_2 = Frame(self.root, bd=4, bg='#DDA0DD',
                         highlightbackground='#FF69B4', highlightthickness=3)
     self.frame_2.place(relx=0.02, rely=0.2, relwidth=0.96, relheight=0.76)
    #Posições das cordenadas do frame de baixo, se o rely for igual, haverá sobreposição
        
    def window_config(self):
        self.root.configure(background='#DA70D6')
        self.root.title("Contador de histórias")
        self.root.geometry('600x600')
        self.root.resizable(True, True)
    def widgets(self):
       #Botão de play
       self.bt_play = Button(self.frame_1, text= 'PLAY')
       self.bt_play.place(relx= 0.1, rely= 0.1, relheight= 0.6, relwidth= 0.3)
       
    def combobox(self):
        #combobox para selecionar história do dia
        self.combo = ttk.Combobox(self.frame_1, values=['História 1', 'História 2', 'História 3'])
        self.combo.place(relx=0.5, rely=0.1, relheight=0.6, relwidth=0.4)
     
root = Tk()
app = Application(root)