# Linguaguem Python e SQL

import pandas as pd
import sqlite3


# AULA 01 - SELECT, WHERE AND FILTERS ----

dados = pd.read_table("Person.txt", delimiter='\t')
print(dados.columns)


# COMANDO SELECT
sql_query = """ SELECT * FROM dados; """
print(dados.head(10))

sql_query = """ SELECT 'FirstName' FROM dados; """
print(dados['FirstName'].head(10))

sql_query = """ SELECT FirstName','MiddleName','LastName' FROM dados; """
print(dados[['FirstName','MiddleName','LastName']].head(10))

sql_query = """ SELECT DISTINCT 'Title' FROM dados; """
print(dados['Title'].unique())
print(dados['Title'].drop_duplicates())


#  COMANDO WHERE

sql_query = """ SELECT * FROM dados WHERE 'BusinessEntityID' > 5; """
print(dados[dados['BusinessEntityID'] > 5].head(10))

sql_query = """ SELECT * FROM dados WHERE 'BusinessEntityID' >= 5; """
print(dados[dados['BusinessEntityID'] >= 5].head(10))

sql_query = """ SELECT * FROM dados WHERE 'BusinessEntityID' = 5; """
print(dados[dados['BusinessEntityID'] == 5].head(10))

sql_query = """ SELECT * FROM dados WHERE 'BusinessEntityID' <> 5; """
print(dados[dados['BusinessEntityID'] != 5].head(10))

sql_query = """ SELECT * FROM dados WHERE 'BusinessEntityID' > 5 and
                'Title' = 'Ms.'; """
print(dados[ (dados.BusinessEntityID > 5) & (dados.Title == 'Ms.') ])
print(dados[ (dados.BusinessEntityID > 5) & (dados.Title == 'Ms.') ][["BusinessEntityID","Title"]])

sql_query = """ SELECT * FROM dados WHERE 'BusinessEntityID' > 5 or
                'Title' = 'Ms.'; """
print(dados[ (dados.BusinessEntityID < 5) | (dados.Title == 'Ms.') ])
print(dados[ (dados.BusinessEntityID < 5) | (dados.Title == 'Ms.') ][["BusinessEntityID","Title"]])


sql_query = """ SELECT * FROM dados WHERE 'BusinessEntityID' > 5 and
                'Title' IS NULL; """
print(dados[ (dados.BusinessEntityID > 5) & (dados['Title'].isna())])
print(dados[ (dados.BusinessEntityID > 5) & (dados['Title'].isna()) ][["BusinessEntityID","Title"]])
print(dados[ (dados.BusinessEntityID > 5) & (dados['Title'].isnull())])
print(dados[ (dados.BusinessEntityID > 5) & (dados['Title'].isnull()) ][["BusinessEntityID","Title"]])

sql_query = """ SELECT * FROM dados WHERE 'BusinessEntityID' > 5 and
                'Title' IS NOT NULL; """
print(dados[ (dados.BusinessEntityID > 5) & (~dados['Title'].isna())])
print(dados[ (dados.BusinessEntityID > 5) & (~dados['Title'].isna()) ][["BusinessEntityID","Title"]])
print(dados[ (dados.BusinessEntityID > 5) & (~dados['Title'].isnull())])
print(dados[ (dados.BusinessEntityID > 5) & (~dados['Title'].isnull()) ][["BusinessEntityID","Title"]])

sql_query = """ SELECT * FROM dados WHERE 'BusinessEntityID' in (5,6,7) """
print(dados[ dados.BusinessEntityID.isin( [5,6,7] ) ])
print(dados[ dados.BusinessEntityID.isin( [5,6,7] ) ][["BusinessEntityID","Title"]])

sql_query = """ SELECT * FROM dados WHERE 'BusinessEntityID' not in (5,6,7) """
print(dados[ ~dados.BusinessEntityID.isin( [5,6,7] ) ])
print(dados[ ~dados.BusinessEntityID.isin( [5,6,7] ) ][["BusinessEntityID","Title"]])

sql_query = """ SELECT * FROM dados WHERE 'Title' in ('Ms.','Mr.') """
print(dados[ dados.Title.isin( ['Ms.','Mr.'] ) ])
print(dados[ dados.Title.isin( ['Ms.','Mr.'] ) ][["BusinessEntityID","Title"]])

sql_query = """ SELECT * FROM dados WHERE 'Title' not in ('Ms.','Mr.') """
print(dados[ ~dados.Title.isin( ['Ms.','Mr.'] ) ])
print(dados[ ~dados.Title.isin( ['Ms.','Mr.'] ) ][["BusinessEntityID","Title"]])
