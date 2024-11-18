import csv
import os
from collections import defaultdict

def load_voting_locations(file_path):
    # Carrega as seções e seus respectivos bairros do arquivo locaisDeVotacao.csv
    section_to_neighborhood = {}
    with open(file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            section = row['Secao'].zfill(4)  # Padroniza a seção para 4 dígitos
            neighborhood = row['Bairro']
            section_to_neighborhood[section] = neighborhood
    return section_to_neighborhood

def load_total_votes(file_path):
    # Carrega os totais de votos do arquivo total_votos.csv
    total_votes = {}
    with open(file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            section = row['Secao'].zfill(4)  # Padroniza a seção para 4 dígitos
            total_votes[section] = int(row['Total de Votos'])
    return total_votes

def process_votes_by_neighborhood(input_directory, section_to_neighborhood):
    votes_by_neighborhood = defaultdict(lambda: defaultdict(int))
    total_votes = defaultdict(int)
    grand_total_votes = 0

    for filename in os.listdir(input_directory):
        if filename.startswith("votos_candidatos_Secao_") and filename.endswith(".csv"):
            section_number = filename.split('_')[-1].replace('.csv', '').zfill(4)
            neighborhood = section_to_neighborhood.get(section_number)

            if neighborhood:
                with open(os.path.join(input_directory, filename), 'r', encoding='utf-8') as csvfile:
                    reader = csv.DictReader(csvfile)
                    for row in reader:
                        candidate = row['Candidato']
                        votes = int(row['Votos'])
                        votes_by_neighborhood[neighborhood][candidate] += votes
                        total_votes[candidate] += votes
                        grand_total_votes += votes

                print(f"Arquivo: {filename}, Votos processados: {grand_total_votes}")

    return votes_by_neighborhood, total_votes, grand_total_votes

def save_votes_by_neighborhood(votes_by_neighborhood, total_votes, grand_total_votes, output_file_path, total_votes_by_section):
    all_candidates = set()
    for candidates in votes_by_neighborhood.values():
        all_candidates.update(candidates.keys())
    
    all_candidates = sorted(all_candidates)
    
    with open(output_file_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        
        headers = ['Bairro'] + all_candidates + ['Total Votos', 'Total Esperado']
        writer.writerow(headers)

        for neighborhood, candidates in votes_by_neighborhood.items():
            row = [neighborhood]
            total_votes_neighborhood = 0
            total_votes_for_section = 0

            for candidate in all_candidates:
                votes = candidates.get(candidate, 0)
                row.append(votes)
                total_votes_neighborhood += votes
            
            total_votes_for_section = total_votes.get(neighborhood, 0)
            row.append(total_votes_neighborhood)
            row.append(total_votes_for_section)
            writer.writerow(row)

        total_row = ['Total Votos']
        for candidate in all_candidates:
            total_row.append(total_votes[candidate])
        total_row.append(grand_total_votes)
        writer.writerow(total_row)

# Caminhos para os arquivos de entrada e saída
voting_locations_file = 'locaisDeVotacao.csv'
input_directory = 'csvs'
output_file = 'votos_por_bairro_comparacao.csv'
total_votes_file = 'total_votos.csv'

# Carrega as seções e seus respectivos bairros
section_to_neighborhood = load_voting_locations(voting_locations_file)

# Carrega os totais de votos do arquivo total_votos.csv
total_votes_by_section = load_total_votes(total_votes_file)

# Processa os votos agregados por bairro e totaliza os votos por candidato
votes_by_neighborhood, total_votes, grand_total_votes = process_votes_by_neighborhood(input_directory, section_to_neighborhood)

# Salva o resultado em um arquivo CSV
save_votes_by_neighborhood(votes_by_neighborhood, total_votes, grand_total_votes, output_file, total_votes_by_section)

# Exibindo total de votos ao final
print(f"Total geral de votos processados: {grand_total_votes}")
print(f"Relatório de votos por bairro salvo em {output_file}.")
