# Linguaguem Python e SQL

import pandas as pd
import sqlite3


# AULA 02 - COUNT, TOP/LIMIT, ORDER BY, BETWEEN, IN, LIKE ----

dados = pd.read_table("Person.txt", delimiter='\t')
print(dados.columns)

# COMANDO COUNT

sql_query = """ SELECT COUNT (*) FROM dados """
print(dados.count())
print(dados.shape[0],dados.shape[1], dados.shape[0]*dados.shape[1])


sql_query = """ SELECT COUNT (FirstName) FROM dados """
print(dados["FirstName"].count())


sql_query = """ SELECT COUNT (DISTINCT FirstName) FROM dados """
print(dados["FirstName"].drop_duplicates().count())


# COMANDO TOP/LIMIT

sql_query = """ " SELECT * FROM dados LIMIT 10" """
print(dados.head(10))
print(dados.tail(10))

# COMANDO ORDER

sql_query = """ SELECT 'BusinessEntityID','FirstName','LastName' FROM dados ORDER BY 'BusinessEntityID' """
print(dados[['BusinessEntityID','FirstName','LastName']].sort_values(by='BusinessEntityID', ascending=True))
print(dados[['BusinessEntityID','FirstName','LastName']].sort_values(by='BusinessEntityID', ascending=False))

sql_query = """ SELECT 'BusinessEntityID','FirstName','LastName' FROM dados ORDER BY 'FirstName' """
print(dados[['BusinessEntityID','FirstName','LastName']].sort_values(by='FirstName', ascending=True))
print(dados[['BusinessEntityID','FirstName','LastName']].sort_values(by='FirstName', ascending=False))

sql_query = """ SELECT 'BusinessEntityID','FirstName','LastName' FROM dados ORDER BY 'FirstName' asc, 'LastName' desc"""
print(dados[['BusinessEntityID','FirstName','LastName']].sort_values(by=['FirstName','LastName'], ascending=[True, False]))


# COMANDO BETWEEN

sql_query = """ SELECT * FROM dados WHERE 'BusinessEntityID' BETWEEN 3 AND 10; """

print(dados[(dados['BusinessEntityID'] >=3) & (dados['BusinessEntityID'] <= 10)])
print(dados[dados['BusinessEntityID'].between(3, 10)])
print(dados[~dados['BusinessEntityID'].between(3, 10)])


# COMANDO LIKE

sql_query = """ SELECT * FROM dados WHERE Species LIKE 'SE%'; # COMECA COM """
print(dados[dados['FirstName'].str.startswith('Ed')][['FirstName','MiddleName','LastName']])
print(dados[~dados['FirstName'].str.startswith('Ed')][['FirstName','MiddleName','LastName']])

sql_query = """ SELECT * FROM dados WHERE Species LIKE '%SE'; # TERMINA COM """
print(dados[dados['FirstName'].str.endswith('a')][['FirstName','MiddleName','LastName']])
print(dados[~dados['FirstName'].str.endswith('a')][['FirstName','MiddleName','LastName']])

sql_query = """ SELECT * FROM dados WHERE Species LIKE '%SE%'; # CONTÉM """
print(dados[dados['FirstName'].str.contains('ar')][['FirstName','MiddleName','LastName']])
print(dados[~dados['FirstName'].str.contains('ar')][['FirstName','MiddleName','LastName']])



# AULA 03 - AS, ESTATISTICAS BASICAS, GROUP BY, HAVING ----


# COMANDO AS

sql_query = """ SELECT 'MiddleName' AS 'Nome do meio', 'Suffix' AS 'Sufixo' FROM dados; """
dados = dados.rename(columns={'MiddleName': 'Nome do meio', 'Suffix': 'Sufixo'})
print(dados[['Nome do meio','Sufixo']])


# FORMULAS ESTATISTICAS BASICAS

sql_query = """ SELECT SUM('BusinessEntityID') AS Soma FROM dados; """
print(dados.BusinessEntityID.sum())

sql_query = """ SELECT AVG('BusinessEntityID') AS Media FROM dados; """
print(dados.BusinessEntityID.mean())

sql_query = """ SELECT Min('BusinessEntityID') AS Minimo FROM dados; """
print(dados.BusinessEntityID.min())

sql_query = """ SELECT Max('BusinessEntityID') AS Maximo FROM dados; """
print(dados.BusinessEntityID.max())

sql_query = """ SELECT Median('BusinessEntityID') AS Mediana FROM dados; """
print(dados.BusinessEntityID.median())


# COMANDO GROUP BY

sql_query = """ SELECT 'Title', SUM('BusinessEntityID') AS Soma FROM dados GROUP BY 'Title'; """
print(dados.groupby('Title')['BusinessEntityID'].sum())

sql_query = """ SELECT 'Title', COUNT('BusinessEntityID') AS Contagem FROM dados GROUP BY 'Title', 'PersonType'; """
print(dados.groupby(['Title', 'PersonType'])['BusinessEntityID'].count())


sql_query = """ SELECT 'Ano', AVG('BusinessEntityID') AS Media FROM dados GROUP BY 'Ano'; """
dados['Ano'] = pd.to_datetime(dados['ModifiedDate']).dt.year
print(dados.groupby('Ano')['BusinessEntityID'].mean())

resultado = dados.groupby('Ano')['BusinessEntityID'].mean().reset_index()
resultado_ordenado = resultado.sort_values(by='Ano', ascending=True)
print(resultado_ordenado)


# COMANDO HAVING - COMANDO WHERE PARA A TABELA JA FILTRADA

sql_query = """ SELECT 'Ano', AVG('BusinessEntityID') AS Media FROM dados GROUP BY 'Ano' HAVING Media < 300; """
print(dados.groupby('Ano')['BusinessEntityID'].mean())

resultado = dados.groupby('Ano')['BusinessEntityID'].mean().reset_index()
resultado_ordenado = resultado[resultado.BusinessEntityID < 50]
print(resultado_ordenado)