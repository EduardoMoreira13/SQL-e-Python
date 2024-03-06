# Linguaguem Python e SQL

import pandas as pd
import numpy as np
import sqlite3


# AULA 04 - INNER JOIN, LEFT JOIN, UNION ----

Pearson = pd.read_table("Person.txt", delimiter='\t')
Business = pd.read_table("Bussiness.txt", delimiter='\t')
Pearson["Number"] = np.linspace(100,10000,100)
Business.loc[[0,3,65,87,89], "BusinessEntityID"] = [101,102,103,104,105]
print(Business["BusinessEntityID"][[0,3,65,87,89]])
print(Pearson.columns)
print(Business.columns)


# COMANDO INNER JOIN - intersecção entre A e B

sql_query = """ SELECT A.BusinessEntityID, A.FirstName, A.LastName, B.BusinessEntityID, B.EmailAddress
        FROM Person AS A INNER JOIN Bussiness AS B ON A.BusinessEntityID = B.BusinessEntityID """

A = Pearson[['BusinessEntityID', 'FirstName', 'LastName']]
B = Business[['BusinessEntityID', 'EmailAddress']]

resultado = pd.merge(A, B, on='BusinessEntityID', how ='inner') # colunas com nomes iguais
# resultado = pd.merge(df1, df2, left_on='chave_df1', right_on='chave_df2', how='inner') # colunas com nomes diferentes
print(resultado.tail(20))


# COMANDO LEFT JOIN - Em A com restante em B ou somente em A

sql_query = """ SELECT A.BusinessEntityID, A.FirstName, A.LastName, B.BusinessEntityID, B.EmailAddress
        FROM Person AS A LEFT JOIN Bussiness AS B ON A.BusinessEntityID = B.BusinessEntityID """

A = Pearson[['BusinessEntityID', 'FirstName', 'LastName']]
B = Business[['BusinessEntityID', 'EmailAddress']]

resultado = pd.merge(A, B, on='BusinessEntityID', how ='left') # colunas com nomes iguais
# resultado = pd.merge(df1, df2, left_on='chave_df1', right_on='chave_df2', how='inner') # colunas com nomes diferentes
print(resultado)

sql_query = """ SELECT A.BusinessEntityID, A.FirstName, A.LastName, B.BusinessEntityID, B.EmailAddress
        FROM Person AS A LEFT JOIN Bussiness AS B ON A.BusinessEntityID = B.BusinessEntityID 
        WHERE B.BusinessEntityID is null"""

resultado = pd.merge(A, B, on='BusinessEntityID', how='left', indicator=True)
resultado_left_only = resultado[resultado['_merge'] == 'left_only'].drop(columns='_merge')

print(resultado_left_only)


# COMANDO RIGHT JOIN - Em B com restante em A ou somente em B

sql_query = """ SELECT A.BusinessEntityID, A.FirstName, A.LastName, B.BusinessEntityID, B.EmailAddress
        FROM Person AS A RIGHT JOIN Bussiness AS B ON A.BusinessEntityID = B.BusinessEntityID """

A = Pearson[['BusinessEntityID', 'FirstName', 'LastName']]
B = Business[['BusinessEntityID', 'EmailAddress']]

resultado = pd.merge(A, B, on='BusinessEntityID', how ='right') # colunas com nomes iguais
# resultado = pd.merge(df1, df2, left_on='chave_df1', right_on='chave_df2', how='inner') # colunas com nomes diferentes
print(resultado)


sql_query = """ SELECT A.BusinessEntityID, A.FirstName, A.LastName, B.BusinessEntityID, B.EmailAddress
        FROM Person AS A RIGHT JOIN Bussiness AS B ON A.BusinessEntityID = B.BusinessEntityID
        WHERE A.BusinessEntityID is null"""

resultado = pd.merge(A, B, on='BusinessEntityID', how='right', indicator=True)
resultado_right_only = resultado[resultado['_merge'] == 'right_only'].drop(columns='_merge')

print(resultado_right_only)


# COMANDO FULL JOIN - completo e sem a intersecção

sql_query = """ SELECT A.BusinessEntityID, A.FirstName, A.LastName, B.BusinessEntityID, B.EmailAddress
        FROM Person AS A FULL OUTER JOIN Bussiness AS B ON A.BusinessEntityID = B.BusinessEntityID """

A = Pearson[['BusinessEntityID', 'FirstName', 'LastName']]
B = Business[['BusinessEntityID', 'EmailAddress']]

resultado = pd.merge(A, B, on='BusinessEntityID', how ='outer') # colunas com nomes iguais
# resultado = pd.merge(df1, df2, left_on='chave_df1', right_on='chave_df2', how='inner') # colunas com nomes diferentes
print(resultado)

sql_query = """ SELECT A.BusinessEntityID, A.FirstName, A.LastName, B.BusinessEntityID, B.EmailAddress FROM Person AS A
        FULL OUTER JOIN Bussiness AS B ON A.BusinessEntityID = B.BusinessEntityID
        WHERE A.BusinessEntityID is null or B.BusinessEntityID is null """

A_not_in_B = A[~A['BusinessEntityID'].isin(B['BusinessEntityID'])]
B_not_in_A = B[~B['BusinessEntityID'].isin(A['BusinessEntityID'])]
resultado = pd.concat([A_not_in_B, B_not_in_A], ignore_index=True)

print(resultado)



# COMANDO UNION

sql_query = """ SELECT FirstName, LastName, BusinessEntityID FROM Person
        WHERE BusinessEntityID <= 40 UNION -- RETIRA DUPLICADOS
        SELECT FirstName, LastName, BusinessEntityID FROM Person WHERE BusinessEntityID > 25  """

A = Pearson[Pearson['BusinessEntityID'] <= 40][['FirstName','LastName','BusinessEntityID']]
B = Pearson[Pearson['BusinessEntityID'] > 25][['FirstName','LastName','BusinessEntityID']]

resultado = pd.concat([A, B], ignore_index=True).drop_duplicates()
print(resultado.head(50))

sql_query = """ SELECT FirstName, LastName, BusinessEntityID FROM Person
        WHERE BusinessEntityID <= 40 UNION ALL -- NAO RETIRA DUPLICADOS
        SELECT FirstName, LastName, BusinessEntityID FROM Person WHERE BusinessEntityID > 25  """

A = Pearson[Pearson['BusinessEntityID'] <= 40][['FirstName','LastName','BusinessEntityID']]
B = Pearson[Pearson['BusinessEntityID'] > 25][['FirstName','LastName','BusinessEntityID']]

resultado = pd.concat([A, B], ignore_index=True)
print(resultado.head(50))