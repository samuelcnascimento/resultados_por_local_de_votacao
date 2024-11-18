import os
import pandas as pd

# Carrega o arquivo de locais de votação para obter o mapeamento de seção para bairro
locais_df = pd.read_csv('locaisDeVotacao.csv', delimiter=';', dtype=str)
locais_df = locais_df[['Secao', 'Bairro']].dropna()  # Filtra apenas as colunas relevantes e remove linhas vazias

# Cria um dicionário de seção para bairro
secao_para_bairro = dict(zip(locais_df['Secao'], locais_df['Bairro']))

# Dicionário para armazenar os votos por bairro e total geral
votos_por_bairro = {}
votos_totais = {}

# Caminho do diretório com os arquivos das seções
caminho_diretorio = 'csvs/'

# Processa cada arquivo de seção no diretório 'csvs/'
for nome_arquivo in os.listdir(caminho_diretorio):
    if nome_arquivo.endswith('.csv'):
        # Carrega o arquivo da seção
        secao_df = pd.read_csv(os.path.join(caminho_diretorio, nome_arquivo), header=None, names=['Secao', 'Candidato', 'Votos'])
        
        # Processa cada linha do arquivo
        for _, row in secao_df.iterrows():
            secao = row['Secao']
            candidato = row['Candidato']
            votos = int(row['Votos'])
            
            # Obtém o bairro correspondente à seção
            bairro = secao_para_bairro.get(str(secao).zfill(4))
            
            if bairro:
                # Atualiza o total de votos por candidato no bairro
                if bairro not in votos_por_bairro:
                    votos_por_bairro[bairro] = {}
                if candidato not in votos_por_bairro[bairro]:
                    votos_por_bairro[bairro][candidato] = 0
                votos_por_bairro[bairro][candidato] += votos

                # Atualiza o total geral de votos por candidato
                if candidato not in votos_totais:
                    votos_totais[candidato] = 0
                votos_totais[candidato] += votos

# Converte os dados de votos por bairro em um DataFrame
resultado_df = pd.DataFrame(votos_por_bairro).T.fillna(0).astype(int)

# Adiciona a linha de total geral
resultado_df.loc['Total Geral'] = resultado_df.sum()

# Salva o resultado em um novo arquivo CSV
resultado_df.to_csv('resultado_eleicao_pivotado.csv', index=True, encoding='utf-8')

print("Arquivo 'resultado_eleicao_pivotado.csv' gerado com sucesso!")
