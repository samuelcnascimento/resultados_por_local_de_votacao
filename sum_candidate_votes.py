import os
import pandas as pd

# Definindo o diretório de entrada
input_directory = 'csvs/'

# Nome do candidato que queremos procurar
candidate_name = '40000 VIEIRA DO TIQUINHO'
total_votes = 0  # Inicializa a contagem total de votos

# Percorre os arquivos CSV no diretório
for filename in os.listdir(input_directory):
    if filename.endswith('.csv'):
        full_path = os.path.join(input_directory, filename)
        
        # Lê o arquivo CSV
        df = pd.read_csv(full_path, header=None, names=['Section', 'Candidate', 'Votes'])
        
        # Filtra os dados para encontrar o candidato
        candidate_votes = df[df['Candidate'] == candidate_name]
        
        # Soma os votos encontrados para o candidato
        total_votes += candidate_votes['Votes'].sum()

print(f'Total de votos para {candidate_name}: {total_votes}')
