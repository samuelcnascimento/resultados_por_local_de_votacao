import os
import pandas as pd

# Definindo o diretório de entrada
input_directory = 'csvs/'

total_votes = 0  # Inicializa a contagem total de votos

# Percorre os arquivos CSV no diretório
for filename in os.listdir(input_directory):
    if filename.endswith('.csv'):
        full_path = os.path.join(input_directory, filename)
        
        # Lê o arquivo CSV
        df = pd.read_csv(full_path, header=None, names=['Section', 'Candidate', 'Votes'])
        
        # Verifica se a coluna de votos é numérica
        df['Votes'] = pd.to_numeric(df['Votes'], errors='coerce')  # Converte para numérico, substitui erros por NaN
        
        # Remove linhas com NaN na coluna de votos
        total_votes += df['Votes'].sum(skipna=True)  # Soma os votos, ignorando NaN

print(f'Total de votos de todos os candidatos: {total_votes}')
