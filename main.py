import tkinter as tk
from tkinter import *
from tkinter import  ttk
from PIL import ImageTk, Image
import requests
import json
import datetime

def formata_moedas(valor):
    moeda = '{:,.2f}'.format(valor)
    moeda = moeda.replace(',','v')
    moeda = moeda.replace('.',',')
    return str(moeda.replace('v','.'))


# ========== Cores ========== #
cor_preto  = "#444466"
cor_branco = "#FEFFFF"
cor_azul   = "#6F9FBD"
cor_fundo  = "#484F50"
cor_cinza  = "#F0F3F5"


# ========== Janela ========== #
janela = Tk()
janela.title("Monitor Bitcoin")
janela.geometry("440x480")
janela.configure(bg=cor_fundo)
janela.resizable(False, False)

# ========== Dividindo a janela em 2 frames ========== #
ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=157)

frame_cima = Frame(janela, width=320, height=50, bg=cor_branco, pady=0, padx=0, relief='flat')
frame_cima.grid(row=1, column=0, sticky=NSEW)

frame_centro = Frame(janela, width=320, height=170, bg=cor_fundo, pady=0, padx=0, relief='flat')
frame_centro.grid(row=2, column=0, sticky=NSEW)

frame_tabela = Frame(janela, width=400, height=100, bg=cor_cinza, relief="groove")
frame_tabela.grid(row=3, column=0, pady=1, padx=10, sticky=NW)

# ========== Configurando o icone e legenda ========== #
imagem = Image.open('bitcoin.png')
imagem = imagem.resize((30,30), Image.LANCZOS)
imagem = ImageTk.PhotoImage(imagem)

legenda = Label(frame_cima, text="Bitcoin Price Monitor", image=imagem, compound=LEFT, bg=cor_branco, fg=cor_preto, relief=FLAT, font=("Arial 20"))
legenda.place(x=70, y=10)

# ========== Configurando os frames da janela ========== #
label_usd = Label(frame_centro, compound=LEFT, bg=cor_fundo, fg=cor_branco, relief=FLAT, anchor="center", font=("Arial 30"))
label_usd.place(x=80, y=20)

label_real = Label(frame_centro, compound=LEFT, bg=cor_fundo, fg=cor_branco, relief=FLAT, anchor="center", font=("Arial 20"))
label_real.place(x=125, y=75)

label_euro = Label(frame_centro, compound=LEFT, bg=cor_fundo, fg=cor_branco, relief=FLAT, anchor="center", font=("Arial 20"))
label_euro.place(x=145, y=120)

# lista_precos = tk.Text(frame_centro, width=35, height=7)
# lista_precos.place(x=20, y=160)

dados_cabecalho = ['Data', 'Valores']
tabela = ttk.Treeview(frame_tabela, selectmode="extended", columns=dados_cabecalho, show="headings")

# barra de rolagem vertical e horizontal:
barra_vertical = ttk.Scrollbar(frame_tabela, orient="vertical", command=tabela.yview)

# configuração da tabela de exibição dos dados:
tabela.configure(yscrollcommand=barra_vertical.set)

tabela.grid(column=0, row=0, sticky='nsew')
barra_vertical.grid(column=1, row=0, sticky='ns')

# cabecalho tabela:
tabela.heading(0, text='Data', anchor='center')
tabela.heading(1, text='Valores', anchor='center')

# corpo tabela:
tabela.column(0, width=150, anchor='nw')
tabela.column(1, width=250, anchor='nw')


# ========== API ========== #
def get_valor_bitcoin():
    api_link = 'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR,BRL'
    response = requests.get(api_link) # executando a requisicao
    dados = response.json() # decodificando o json retornado

    valor_dolar = float(dados['USD'])
    valor_dolar = "US$ "+formata_moedas(valor_dolar)
    label_usd['text'] = valor_dolar

    valor_euro = float(dados['EUR'])
    valor_euro = "€ "+formata_moedas(valor_euro)
    label_euro['text'] = valor_euro

    valor_real = float(dados['BRL'])
    valor_real = "R$ "+formata_moedas(valor_real)
    label_real['text'] = valor_real

    agora = datetime.datetime.now() # pegando data e hora atual
    data_formatada = f"{agora.strftime('%d/%m/%Y %H:%M:%S')}"
    tabela.insert('', 'end', values=(data_formatada, valor_dolar+"; "+valor_real+"; "+valor_euro))
    frame_centro.after('1000', get_valor_bitcoin) # vai executar novamente a funcao após 1 segundo após o frame ter sido alterado


get_valor_bitcoin()
janela.mainloop()
