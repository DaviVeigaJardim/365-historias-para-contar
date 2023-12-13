from tkinter import *
from tkinter import ttk
import random
import pygame 
from download import download_stories
class Aplicacao:
    def __init__(self, master):
        self.raiz = master
        self.configurando_janela()
        self.quadros_da_tela()
        self.componentes()
        self.combobox()
        self.raiz.mainloop()

    def quadros_da_tela(self):
        self.quadro_1 = Frame(self.raiz, bd=0, bg='#FFB6C1',
                             highlightbackground='#FFB6C1', highlightthickness=1)
        self.quadro_1.place(relx=0.001, rely=0.001, relwidth= 1, relheight= 1)

    def configurando_janela(self):
        self.raiz.configure(background='#1C1C1C')
        self.raiz.title("Contador de histórias")
        self.raiz.geometry('600x400')
        self.raiz.resizable(True, True)

    def componentes(self):

        self.bt_parar = Button(self.quadro_1, text='Stop', bd=0.5, bg='#FFE4E1', fg='black', font=('verdana', 10, 'bold'), command=self.funcao_parar)
        self.bt_parar.place(relx=0.25, rely=0.03, relheight=0.1, relwidth=0.2)
       
        self.bt_comecar = Button(self.quadro_1, text='Play', bd=0.5, bg='#FFE4E1', fg='black', font=('verdana', 10, 'bold'), command =self.inicializar_reprodutor)
        self.bt_comecar.place(relx=0.01, rely=0.03, relheight=0.1, relwidth=0.2)

        self.bt_aleatorio = Button(self.quadro_1, text=' reprodução \n aleatoria', bd=2, bg='#FFE4E1', fg='black', font=('verdana', 10, 'bold'), command = self.reproducao_aleatoria)
        self.bt_aleatorio.place(relx=0.01, rely=0.3, relheight=0.1, relwidth=0.2)

        self.bt_sequencial = Button(self.quadro_1, text='reprodução \n sequencial', bd=2, bg='#FFE4E1', fg='black', font=('verdana', 10, 'bold'))
        self.bt_sequencial.place(relx=0.01, rely=0.5, relheight=0.10, relwidth=0.2)

        self.label_mensagem = Label(self.quadro_1, text='', font=('verdana', 12, 'bold'), fg = 'black', bg = '#FFB6C1')
        self.label_mensagem.place(relx=0.35, rely=0.4)
        self.label_mensagem_mes = Label(self.quadro_1, text='', font = ('verdana', 12, 'bold' ), fg ='black', bg = '#FFB6C1')
        self.label_mensagem_mes.place(relx = 0.65, rely = 0.4)
    
    def funcao_parar(self):
        pygame.mixer_music.stop()
        self.botao_reproduzir_clicado = False
        self.label_mensagem.config(text= 'Reprodução parada')

    def combobox(self):
        self.valores_dias = list(range(1, 31))
        self.combo_dias = ttk.Combobox(self.quadro_1, values=self.valores_dias)
        self.combo_dias.set('Dia')
        self.combo_dias.place(relx=0.5, rely=0.03, relheight=0.1, relwidth=0.15)
        self.combo_dias.bind("<<ComboboxSelected>>", self.selecionar_dia)

        self.valores_mes = ['Janeiro', 'Fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro', 'novembro', 'dezembro']
        self.combo_meses = ttk.Combobox(self.quadro_1, values=self.valores_mes)
        self.combo_meses.set('Mês')
        self.combo_meses.place(relx=0.7, rely=0.03, relheight=0.1, relwidth=0.15)
        self.combo_meses.bind("<<ComboboxSelected>>", self.selecionar_mes)


    def selecionar_dia(self, event):
        self.atualizar_label_mensagem()

    def selecionar_mes(self, event):
        self.atualizar_label_mensagem()

    def atualizar_label_mensagem(self):   
        dia_selecionado = self.combo_dias.get()
        mes_selecionado = self.combo_meses.get()

        if dia_selecionado != 'Dia' and mes_selecionado != 'Mês':
            mensagem = (f'Historia do dia {dia_selecionado} de {mes_selecionado}')
            self.label_mensagem.config(text=mensagem)
        else:
            self.label_mensagem.config(text = '')
            self.label_mensagem_mes.config(text= '')
    def reproducao_aleatoria(self):
        self.botao_aleatorio_clicado = False
        dia_aleatorio = random.randint(0,31)
        mes_aleatorio = random.choice(self.valores_mes)
        self.combo_dias.set(dia_aleatorio)
        self.combo_meses.set(mes_aleatorio)
        self.atualizar_label_mensagem()
        
        date = (f'{mes_aleatorio.lower()}{dia_aleatorio}')
        file_path = download_stories(date)

        pygame.mixer.init()
        pygame.mixer.music.load(file_path)
        pygame.mixer_music.play()
 
    def inicializar_reprodutor(self):
       dia_selecionado = self.combo_dias.get()
       mes_selecionado = self.combo_meses.get()

       if dia_selecionado != 'Dia' and mes_selecionado != 'Mês': 
           date = (f'{mes_selecionado.lower()}{dia_selecionado}')
           file_path = download_stories(date)

           pygame.mixer.init()
           pygame.mixer.music.load(file_path)
           pygame.mixer.music.play()
           self.label_mensagem.config(text=f'História do dia {dia_selecionado} de {mes_selecionado}')


raiz = Tk()
app = Aplicacao(raiz)