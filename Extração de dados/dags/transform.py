#!/usr/bin/env python
# coding: utf-8

# In[79]:


import requests 
from datetime import datetime, timedelta
import pandas as pd
from pandas.errors import EmptyDataError
import csv
import os



df_dados = pd.read_pickle("data_extract.pkl")



df_dados


df_dados["publishedAt"] = pd.to_datetime(df_dados["publishedAt"])
df_dados['Ano'] = df_dados['publishedAt'].dt.year
df_dados['month'] = df_dados['publishedAt'].dt.month
df_dados['Mês'] = pd.to_datetime(df_dados['month'], format='%m').dt.strftime('%B')
df_dados['Dia'] = df_dados['publishedAt'].dt.day



df_dados.columns


# # 4.1 - Quantidade de notícias por ano, mês e dia de publicação


df_dados.groupby(['Ano', 'Mês', 'Dia']).size().reset_index(name='Quantidade').sort_values(by='Quantidade', ascending=False)


# # 4.2 - Quantidade de notícias por fonte e autor;

df_dados.groupby(['source', 'author']).size().reset_index(name='Quantidade').sort_values(by='Quantidade', ascending=False)


# # 4.3 - Quantidade de aparições de 3 palavras chaves por ano, mês e dia de publicação (as 3 palavras chaves serão as mesmas usadas para fazer os filtros de relevância do item 2 (2. Definir Critérios de Relevância)).



df_dados[df_dados['content'].str.contains('(?i)down syndrome', regex=True)]
df_dados[df_dados['content'].str.contains('(?i)cancer', regex=True)]
df_dados[df_dados['content'].str.contains('(?i)diabetes', regex=True)]



