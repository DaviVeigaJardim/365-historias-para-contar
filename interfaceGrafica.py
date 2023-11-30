from tkinter import *
from tkinter import ttk
import random
class Aplicacao:
    def __init__(self, master):
        self.raiz = master
        self.configurando_janela()
        self.quadros_da_tela()
        self.componentes()
        self.combobox()
        self.raiz.mainloop()

    def quadros_da_tela(self):
        self.quadro_1 = Frame(self.raiz, bd=0, bg='#1C1C1C',
                             highlightbackground='#1C1C1C', highlightthickness=1)
        self.quadro_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.15)

        self.quadro_2 = Frame(self.raiz, bd=0, bg='#1C1C1C',
                             highlightbackground='#363636', highlightthickness=2)
        self.quadro_2.place(relx=0.02, rely=0.2, relwidth=0.96, relheight=0.76)

    def configurando_janela(self):
        self.raiz.configure(background='#1C1C1C')
        self.raiz.title("Contador de histórias")
        self.raiz.geometry('600x600')
        self.raiz.resizable(True, True)

    def componentes(self):

        self.bt_play = Button(self.quadro_1, text='STOP', bd=5, bg='#FF8C00', fg='black', font=('verdana', 10, 'bold'), command=self.funcao_parar)
        self.bt_play.place(relx=0.01, rely=0.1, relheight=0.6, relwidth=0.2)

        self.bt_aleatorio = Button(self.quadro_2, text=' reprodução \n aleatoria', bd=5, bg='#FF8C00', fg='black', font=('verdana', 10, 'bold'), command = self.reproducao_aleatoria)
        self.bt_aleatorio.place(relx=0.01, rely=0.1, relheight=0.10, relwidth=0.2)

        self.bt_sequencial = Button(self.quadro_2, text='reprodução \n sequencial', bd=5, bg='#FF8C00', fg='black', font=('verdana', 10, 'bold'))
        self.bt_sequencial.place(relx=0.01, rely=0.3, relheight=0.10, relwidth=0.2)

        self.label_mensagem = Label(self.quadro_2, text='', font=('verdana', 12, 'bold'), bg='#1C1C1C', fg = '#FF8C00')
        self.label_mensagem.place(relx=0.4, rely=0.3)

        self.label_mensagem_mes = Label(self.quadro_2, text='', font = ('verdana', 12, 'bold' ), bg ='#1C1C1C', fg ='#FF8C00')
        self.label_mensagem_mes.place(relx = 0.7, rely = 0.3)

    def funcao_parar(self):
        self.botao_reproduzir_clicado = False
        self.label_mensagem.config(text= 'Reprodução parada')

    def combobox(self):
        self.valores_dias = list(range(1, 31))
        self.combo_dias = ttk.Combobox(self.quadro_1, values=self.valores_dias)
        self.combo_dias.set('Dia')
        self.combo_dias.place(relx=0.3, rely=0.2, relheight=0.4, relwidth=0.2)
        self.combo_dias.bind("<<ComboboxSelected>>", self.selecionar_dia)

        self.valores_mes = ['Janeiro', 'Fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro', 'novembro', 'dezembro']
        self.combo_meses = ttk.Combobox(self.quadro_1, values=self.valores_mes)
        self.combo_meses.set('Mês')
        self.combo_meses.place(relx=0.6, rely=0.2, relheight=0.4, relwidth=0.2)
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
        self.combo_dias.set(random.randint(0,31))
        self.combo_meses.set(random.choice(self.valores_mes))
        self.atualizar_label_mensagem()
        


raiz = Tk()
app = Aplicacao(raiz)