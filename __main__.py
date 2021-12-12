from modules.connector import IntegrageCassandra
from cassandra.cluster import Cluster
import pandas as pd

if __name__ == "__main__":
    
    database = 'oldtech'
    nome_tabela = 'sistemab'
    
    df = pd.read_csv("Sistema_B_NoSQL.csv", sep=",")

    # Remover arquivo com campo  Vazio
    df_unico = df.dropna()
    #print(df_unico)
    
    #   Comando para transformar as linhas de dataframe tratado em uma lista de listas
    
    #lista_df_unico=df_unico.values.tolist()
    cursor = IntegrageCassandra(database,nome_tabela)
    
    for linha in range(4):#lista_df_unico:
        try:
            #linha.insert(0,str('uuid()'))        # adiciona string na primeira posição da lista
            tupla_valores=tuple(linha)      # transformar em tupla para o insert
            
            
            
            #query_insert=f"INSERT INTO {nome_tabela} (id_vendas, nota_fiscal, vendedor, total) values (uuid(), 1, 'edson', 8);"
            #query_insert=
            #print(type(tupla_valores[0]))
            cursor.insert()
        except Exception as e:
            print("erro",str(e))
            



















































































































































































































































































































