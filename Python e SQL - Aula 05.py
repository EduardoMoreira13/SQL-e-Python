# Linguaguem Python e SQL

import pandas as pd
import numpy as np
import sqlite3


# AULA 05 - SELF JOIN, SUBQUERY, DATEPART, STRINGS, MATH OPERATIONS ----

Pearson = pd.read_table("Person.txt", delimiter='\t')
Business = pd.read_table("Bussiness.txt", delimiter='\t')
Pearson['ModifiedDate'] = pd.to_datetime(Pearson['ModifiedDate'])
Business['ModifiedDate'] = pd.to_datetime(Business['ModifiedDate'])
Pearson["Number"] = np.linspace(100,10000,100)
Business.loc[[0,3,65,87,89], "BusinessEntityID"] = [101,102,103,104,105]
print(Business["BusinessEntityID"][[0,3,65,87,89]])
print(Pearson.columns)
print(Business.columns)


# COMANDO SELF JOIN

sql_query = """ SELECT A.FirstName, A.LastName, B.FirstName, B.LastName FROM Person AS A, Person AS B
        WHERE A.LastName = B.LastName """

A = Pearson[['BusinessEntityID', 'FirstName', 'LastName']]
B = Pearson[['BusinessEntityID', 'FirstName', 'LastName']]
resultado = pd.merge(A, B, on='LastName', how= 'inner', suffixes=('_1', '_2'))
print(resultado)


# COMANDO SUBQUERY (SUBSELECT)

sql_query = """ SELECT BusinessEntityID FROM Bussiness WHERE BusinessEntityID > (SELECT AVG(Number) / 100 FROM Person) """

A = Pearson.Number.mean() / 100
B = Business[ Business['BusinessEntityID'] > A]['BusinessEntityID']
print(A)
print(B)


# MANIPULACAO DE TEXTO - (STRINGS)

sql_query = """ SELECT CONCAT(FirstName, ' ',LastName) AS NOME FROM Person """
Pearson['Nome Completo'] = Pearson['FirstName'].str.cat(Pearson['LastName'], sep=' ')
print(Pearson['Nome Completo'] )
Pearson['Nome Completo'] = Pearson['FirstName'] + "-" + Pearson['LastName']
print(Pearson['Nome Completo'] )

sql_query =  """ SELECT LOWER('Nome Completo') FROM Pearson """
print(Pearson['Nome Completo'].str.lower() )

sql_query =  """ SELECT UPPER('Nome Completo') FROM Pearson """
print(Pearson['Nome Completo'].str.upper() )
print(Pearson['Nome Completo'].str.capitalize() )

sql_query =  """ SELECT LENGTH('Nome Completo') FROM Pearson """
print(Pearson['Nome Completo'].str.len() )

sql_query =  """ SELECT REPLACE('Nome Completo', '-', ' ') FROM Pearson """
print(Pearson['Nome Completo'].str.replace("-", " ") )

sql_query =  """ SELECT REPLACE('Nome Completo', '-', ' ') FROM Pearson """
print(Pearson['Nome Completo'].str.replace("-", " ") )

sql_query =  """ SELECT SUBSTRING('Nome Completo', 1, 3) FROM Pearson """
print(Pearson['Nome Completo'].str.slice(start=0, stop=3))

