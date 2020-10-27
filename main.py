import utils.xlsx_to_df as xdf
import SQL.connection as connection
import tkinter as tk

root = tk.Tk()
root.withdraw()

print("----------------- SISTEMA DE ENVIO DE ARQUIVOS -- CRUSOÉ ATLAS -----------------")
print()

replay = True
while replay == True:

    #Initial declaration:
    converter = xdf.converter()
    arquivo = converter.seletor()
    dataFrame = converter.xslx_to_Df(arquivo)

    #Declaration of the SENDING process
    sql = connection.sql()
    sql_engine = sql.connect()
    sql_choseTable = sql.table_to_send()

    #Sendding
    try:
        sql_run = sql.sender(dataFrame,sql_choseTable,sql_engine)
        print("Deseja realizar algum outro envio? (y/n)")
        again = input()
        if again.upper() == 'Y':
            replay = True
        else:
            replay = False
    except:
        replay = False
        print("Houve um erro ao Enviar o Banco, desejatentar novamente? (y/n)")
        replay_app = input()
        if replay_app.upper() == 'N':
            replay = False
            break
        else: 
            replay = True

print("Obrigado por utilizar o sistema de envio Atlas")
input("Pressione qualquer tecla para finalizar")
