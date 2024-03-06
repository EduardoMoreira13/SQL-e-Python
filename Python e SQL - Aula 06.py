# Linguaguem Python e SQL

import pandas as pd
import numpy as np
import sqlite3


# AULA 06 - CASE WHEN ----

Pearson = pd.read_table("Person.txt", delimiter='\t')
Business = pd.read_table("Bussiness.txt", delimiter='\t')
Pearson['ModifiedDate'] = pd.to_datetime(Pearson['ModifiedDate'])
Business['ModifiedDate'] = pd.to_datetime(Business['ModifiedDate'])
Pearson["Number"] = np.linspace(100,10000,100)
Business.loc[[0,3,65,87,89], "BusinessEntityID"] = [101,102,103,104,105]
print(Business["BusinessEntityID"][[0,3,65,87,89]])
print(Pearson.columns)
print(Business.columns)

sql_query = """ SELECT 'Title',
        CASE WHEN 'Title' = 'Mr.' THEN  'Masculino'
            ELSE 'Feminino'
            END AS Classificacao
        FROM dados """

# Duas condições
Pearson['Classificacao'] = np.where(Pearson['Title'] == 'Mr.', 'Masculino', 'Feminino')
print(Pearson[['Title','Classificacao']].head(10))

Pearson.loc[Pearson['Title'] == 'Mr.', 'Classificacao'] = 'M'
Pearson.loc[Pearson['Title'] != 'Mr.', 'Classificacao'] = 'F'
print(Pearson[['Title','Classificacao']].head(10))


# Mais de duas condições
Pearson['Classificacao'] = np.where(Pearson['BusinessEntityID'] <= 10, 'A',
                                    np.where(Pearson['BusinessEntityID'] <= 20, 'B',
                                    np.where(Pearson['BusinessEntityID'] <= 50, 'C', 'D')))
print(Pearson[['BusinessEntityID','Title','Classificacao']].head(50))
print(Pearson[['BusinessEntityID','Title','Classificacao']].tail(50))

Pearson.loc[Pearson['BusinessEntityID'] <= 10, 'Classificacao'] = 'A'
Pearson.loc[(Pearson['BusinessEntityID'] <= 20) & (Pearson['BusinessEntityID'] > 10), 'Classificacao'] = 'B'
Pearson.loc[(Pearson['BusinessEntityID'] <= 50) & (Pearson['BusinessEntityID'] > 20), 'Classificacao'] = 'C'
Pearson.loc[Pearson['BusinessEntityID'] > 50, 'Classificacao'] = 'D'
print(Pearson[['BusinessEntityID','Title','Classificacao']].head(50))
print(Pearson[['BusinessEntityID','Title','Classificacao']].tail(50))


