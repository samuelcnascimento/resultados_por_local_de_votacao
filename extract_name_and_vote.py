import os
import pandas as pd

# Definindo os diretórios de entrada e saída
input_directory = 'cleaned_data/'
output_directory = 'csvs/'

# Garantindo que o diretório de saída exista
os.makedirs(output_directory, exist_ok=True)

# Função para processar cada arquivo e extrair os dados
def process_file(filename, section_number):
    data = []
    
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        
        # Percorre as linhas do arquivo
        for i in range(0, len(lines), 3):  # Avançar de 3 em 3 linhas
            if i + 2 < len(lines):  # Verifica se há linhas suficientes
                candidate_name = lines[i].strip()  # Nome do candidato
                votes = lines[i + 1].strip()  # 'Votação'
                if votes == 'Votação':  # Certifique-se de que a linha é a 'Votação'
                    votes_count = lines[i + 2].strip()  # Quantidade de votos
                    # Adiciona à lista de dados
                    data.append([section_number, candidate_name, votes_count])

    # Criar um DataFrame a partir dos dados coletados
    df = pd.DataFrame(data, columns=['Section', 'Candidate', 'Votes'])

    # Salvar o DataFrame em um arquivo CSV
    csv_filename = f'{output_directory}Secao_{section_number}.csv'
    df.to_csv(csv_filename, index=False, header=False)

# Percorre os arquivos no diretório
for filename in os.listdir(input_directory):
    if filename.endswith('.txt'):
        # Extrai o número da seção a partir do nome do arquivo
        section_number = filename.split('_')[1].split('.')[0]  # Pega a parte após 'Secao_'
        full_path = os.path.join(input_directory, filename)
        process_file(full_path, section_number)

print("Arquivos CSV gerados com sucesso!")
