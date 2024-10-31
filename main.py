from tkinter import *
from tkinter import  ttk
from PIL import ImageTk, Image
import requests
import json

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

# ========== Janela ========== #
janela = Tk()
janela.title("Monitor Bitcoin")
janela.geometry("320x350")
janela.configure(bg=cor_fundo)

# ========== Dividindo a janela em 2 frames ========== #
ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=157)

frame_cima = Frame(janela, width=320, height=50, bg=cor_branco, pady=0, padx=0, relief='flat')
frame_cima.grid(row=1, column=0)

frame_centro = Frame(janela, width=320, height=350, bg=cor_fundo, pady=0, padx=0, relief='flat')
frame_centro.grid(row=2, column=0, sticky=NW)

# ========== API ========== #
api_link = 'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR,BRL'
response = requests.get(api_link) # executando a requisicao
dados = response.json() # decodificando o json retornado

valor_dolar = float(dados['USD'])
valor_dolar = "US$ "+formata_moedas(valor_dolar)
valor_euro = float(dados['EUR'])
valor_euro = "€ "+formata_moedas(valor_euro)
valor_real = float(dados['BRL'])
valor_real = "R$ "+formata_moedas(valor_real)


# ========== Configurando o icone e legenda ========== #
imagem = Image.open('bitcoin.png')
imagem = imagem.resize((30,30), Image.LANCZOS)
imagem = ImageTk.PhotoImage(imagem)

legenda = Label(frame_cima, text="Bitcoin Price Monitor", image=imagem, compound=LEFT, bg=cor_branco, fg=cor_preto, relief=FLAT, font=("Arial 20"))
legenda.place(x=10, y=10)

# ========== Configurando os frames da janela ========== #
label_usd = Label(frame_centro, text=valor_dolar, compound=LEFT, bg=cor_fundo, fg=cor_branco, relief=FLAT, anchor="center", font=("Arial 20"))
label_usd.place(x=0, y=50)

label_euro = Label(frame_centro, text=valor_euro, compound=LEFT, bg=cor_fundo, fg=cor_branco, relief=FLAT, anchor="center", font=("Arial 20"))
label_euro.place(x=0, y=100)

label_real = Label(frame_centro, text=valor_real, compound=LEFT, bg=cor_fundo, fg=cor_branco, relief=FLAT, anchor="center", font=("Arial 20"))
label_real.place(x=0, y=130)

janela.mainloop()
