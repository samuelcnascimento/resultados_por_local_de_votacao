import re
import csv
import os

def extract_candidates_info(text, electoral_section):
    pattern = r'(\d{5,6})\s+([A-ZÀ-ÿ\s]+?)\s+Votação\s+(\d+)'
    matches = re.findall(pattern, text)

    candidates_data = []
    for match in matches:
        number, name, votes = match
        name = name.replace('"', '').strip()
        candidate_info = f"{number} {name}"
        candidates_data.append({
            'Secao': electoral_section,
            'Candidato': candidate_info,
            'Votos': int(votes)
        })

    return candidates_data

def extract_total_votes(text):
    pattern = r'Votos\s+de\s+legenda:\s+(\d+)'
    match = re.search(pattern, text)

    if match:
        legend_votes = int(match.group(1))
        return legend_votes
    return 0  # Se não encontrar, retorna 0

def save_to_csv(candidates_data, total_votes_data, output_csv_path, text):
    with open(output_csv_path, 'w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ['Secao', 'Candidato', 'Votos']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        
        # Adiciona os votos de legenda aos votos dos candidatos
        for candidate in candidates_data:
            candidate['Votos'] += extract_total_votes(text)  # Inclui os votos de legenda
            writer.writerow(candidate)

        total_row = {'Secao': total_votes_data['Secao'], 'Candidato': 'Total Votos', 'Votos': total_votes_data['Total']}
        writer.writerow(total_row)

def save_total_votes(total_votes, output_total_votes_path):
    with open(output_total_votes_path, 'w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ['Secao', 'Total de Votos']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        
        for secao in sorted(total_votes.keys()):
            writer.writerow({'Secao': secao, 'Total de Votos': total_votes[secao]})

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def extract_electoral_section(text):
    pattern = r'Seção\s+Eleitoral\s*\n*(\d{4})'
    match = re.search(pattern, text)
    return match.group(1) if match else None

# Diretório onde estão os arquivos de texto
input_directory = 'txts/'
output_directory = 'csvs/'

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

total_votes = {}

for filename in os.listdir(input_directory):
    if filename.startswith("Secao_") and filename.endswith(".txt"):
        input_file_path = os.path.join(input_directory, filename)
        pdf_content = read_file(input_file_path)

        electoral_section = extract_electoral_section(pdf_content)

        # Extrai informações dos candidatos
        candidates_data = extract_candidates_info(pdf_content, electoral_section)
        
        # Calcula o total de votos para cada seção
        total_votes_data = {
            'Secao': electoral_section,
            'Total': sum(candidate['Votos'] for candidate in candidates_data) + extract_total_votes(pdf_content)  # Soma os votos de legenda
        }

        # Salva os dados em CSV
        output_csv_path = os.path.join(output_directory, f"votos_candidatos_{filename[:-4]}.csv")
        save_to_csv(candidates_data, total_votes_data, output_csv_path, pdf_content)  # Passa o texto aqui

        # Armazena os totais por seção
        total_votes[electoral_section] = total_votes_data['Total']

# Salva o total de votos em um arquivo separado
output_total_votes_path = os.path.join(output_directory, 'total_votos.csv')
save_total_votes(total_votes, output_total_votes_path)
