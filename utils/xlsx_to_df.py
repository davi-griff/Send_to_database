import pandas as pd
import openpyxl
import tkinter as tk
import psycopg2
from tkinter import filedialog
import sqlalchemy


class converter():
    def __init__(self):
        pass


    def seletor(self):
        while True:
            arquivo = ''
            input("Pressione enter para selecionar o arquivo")
            arquivo = filedialog.askopenfilename()
            print("Voce selecionou:" + arquivo)
            print("Deseja confirmar? (y/n)")
            print(">", end='')
            resposta = input()
            if resposta == 'y' or resposta == 'Y':
                break
        return arquivo

    def xslx_to_Df(self,arquivo):
        df = pd.read_excel(f'{arquivo}',header=0, engine='openpyxl')
        print(df)
        return df 