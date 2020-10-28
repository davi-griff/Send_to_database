from environs import Env
import psycopg2
import sqlalchemy
import pandas


#Class created to easily change database connections e tables to send
class sql():
    env = Env()

    env.read_env()

    #All of these propretioes are deffined on the .env file.
    sql_ip = env("SQL_IP")
    sql_loggin = env("SQL_LOGGIN")
    sql_password = env("SQL_PASSWORD")
    sql_port = env("SQL_PORT")
    sql_table = env("SQL_TABLE") 

    #Initial declaretion
    def __init(self, sql_ip,sql_loggin,sql_password,sql_port,sql_table,dataFrame):
        self.sql_ip = sql_ip
        self.sql_loggin = sql_loggin
        self.sql_password=sql_password
        self.sql_port = sql_port
        self.sql_table=sql_table

    #This bit will try to connect to de database using SQLAlchemy3 engine
    def connect(self):
        try:
            engine = sqlalchemy.create_engine(f'postgresql://{self.sql_loggin}:{self.sql_password}@{self.sql_ip}:{self.sql_port}/{self.sql_table}')
            return engine
        except:
            print("Erro ao conectar com a database")

    #Here we will choose the tablhe on our database, you can change the names on the print's and the tables on the if clause
    def table_to_send(self):
        print("Defina a tabela para o envio:")
        print('1 - LEITURA')
        print()
        print("2 - ATLASCOR")
        print()
        print("3 - LEITURA-DEV")
        print()
        print("4 - SGIP")
        print("---------------------")
        print(">", end='')
        tabelaenvresp = int(input())
        if tabelaenvresp == 1:
            tabela = 'leitura'
        elif tabelaenvresp == 2:
            tabela = 'atlascor'
        elif tabelaenvresp == 3:
            tabela = 'leitura_dev'
        elif tabelaenvresp == 4:
            tabela = 'sgip'
        return tabela

    #Here we have our DataFrame.to_sql() function, it will read de DataFrame created from the .xlsx sheet and it will send to the database. 
    #It will also reset the aplication if the process have any problem while sending.
    def sender(self,dataFrame,tabela,engine):
        df = dataFrame
        print("Realizando o Envio")
        df.to_sql(f'{tabela}',con=engine ,if_exists='append',chunksize=500,method='multi', index=False)
        print("Envio realizado com Sucesso.")
