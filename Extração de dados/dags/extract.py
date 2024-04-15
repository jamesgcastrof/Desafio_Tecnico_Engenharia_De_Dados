import os
import pandas as pd
import requests

def extrair_e_salvar_dados(url, chave_api, termos):
    for termo in termos:
        dados = busca_artigo_keyword(url, chave_api, termo)
        articles = dados['articles']
        df = pd.DataFrame(articles)
        caminho_arquivo_csv = f'{termo}_dados.csv'
        if os.path.exists(caminho_arquivo_csv):
            df_existente = pd.read_csv(caminho_arquivo_csv)
            df_total = pd.concat([df_existente, df])
            df_total.drop_duplicates(inplace=True)
        else:
            df_total = df
        df_total.to_csv(caminho_arquivo_csv, index=False)

chave_api = '657a3d08bfd94920bc9e527fac57ee28'
url = 'https://newsapi.org/v2/everything'
termos = ['down syndrome', 'cancer', 'diabetes']  # lista de termos para busca

if __name__ == "__main__":
    data = extrair_e_salvar_dados()
    # Salvar DataFrame em um arquivo temporário para uso posterior
    data.to_pickle("data_extract.pkl")