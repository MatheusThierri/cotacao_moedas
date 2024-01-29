from tkinter import *
import requests

def cotacao_dolar():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
    requisicao.dic = requisicao.json()
    converter_dolar = requisicao.dic["USDBRL"]["bid"]
    dolar = f"DÓLAR: ${converter_dolar}"
    texto_dolar["text"] = dolar

def cotacao_euro():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
    requisicao.dic = requisicao.json()
    converter_euro = requisicao.dic["EURBRL"]["bid"]
    euro = f"EURO: €{converter_euro}"
    texto_euro["text"] = euro

def cotacao_bitcoin():
    
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
    requisicao.dic = requisicao.json()
    converter_bitcoin = requisicao.dic["BTCBRL"]["bid"]
    bitcoin = f"BITCOIN: ₿{converter_bitcoin}"
    texto_bitcoin["text"] = bitcoin


janela = Tk()

janela.resizable(width=False, height=False)
janela.title("Cotação de moedas")
janela.geometry("900x600")
janela.state('zoomed')
texto_orientacao = Label(janela, text="Escolha qual moeda você deseja ver a cotação: ", padx=10, pady=10, anchor="center", font=("Cascadia Code SemiBold", 12), bg='#8FBC8F', fg='#FF7F50')
texto_orientacao.grid(column=0, row=0)

botao_dolar = Button(janela, text="Cotação do dólar", command=cotacao_dolar, anchor="center", bg='#FFA07A', font=('Cascadia Code SemiBold', '14', 'bold'), fg='white')
botao_dolar.grid(column=0, row=1, padx=10, pady=10)
texto_dolar = Label(janela, text="", anchor="center", font=('Cascadia Code SemiBold', '14', 'bold'), fg='#8B4513')
texto_dolar.grid(column=0, row=6)
botao_euro = Button(janela, text="Cotação do euro", command=cotacao_euro, anchor="center", bg='#FFA07A', font=('Cascadia Code SemiBold', '14', 'bold'), fg='white')
botao_euro.grid(column=0, row=2, padx=10, pady=10)
texto_euro = Label(janela, text="", anchor="center", font=('Cascadia Code SemiBold', '14', 'bold'), fg='#8B4513')
texto_euro.grid(column=0, row=7)
botao_bitcoin = Button(janela, text="Cotação do bitcoin", command = cotacao_bitcoin, anchor="center", bg='#FFA07A', font=('Cascadia Code SemiBold', '14', 'bold'), fg='white')
botao_bitcoin.grid(column=0, row=3, padx=10, pady=10)
texto_bitcoin = Label(janela, text="", anchor="center", font=('Cascadia Code SemiBold', '14', 'bold'), fg='#8B4513')
texto_bitcoin.grid(column=0, row=8)

janela = mainloop()