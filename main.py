import requests
from tkinter import *

def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''

    resutado["text"] = texto


janela = Tk()
janela.title('Programa')

texto = Label(janela, text="Clique no botão para exibir a cotação: ")
texto.grid(column=0,row=0, padx=80,pady=20)

btn = Button(janela, text='Clique aqui',command=pegar_cotacoes)
btn.grid(column=0,row=1)

resutado = Label(janela,text="")
resutado.grid(column=0,row=3,pady=40)


janela.mainloop()