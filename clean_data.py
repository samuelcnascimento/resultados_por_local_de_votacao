import os
import re

# Caminhos dos diretórios de entrada e saída
input_dir = 'txts'
output_dir = 'cleaned_data'

# Cria o diretório de saída se ele não existir
os.makedirs(output_dir, exist_ok=True)

# Padrão para capturar os candidatos e votos dentro do trecho desejado
pattern = re.compile(r'(\d+)\s+([\w\s]+?)\s+Votação\s+(\d+)')

# Itera sobre todos os arquivos na pasta de entrada
for filename in os.listdir(input_dir):
    if filename.startswith('Secao_') and filename.endswith('.txt'):
        # Abre o arquivo de entrada para leitura
        with open(os.path.join(input_dir, filename), 'r', encoding='utf-8') as file:
            data = file.read()

        # Encontra todas as seções de partidos
        party_sections = re.split(r'Partido\s+\d+\s+-', data)

        output_data = ""

        for section in party_sections[1:]:  # Ignora a parte antes do primeiro partido
            # Extrai o trecho entre 'Candidato' e 'Votos de legenda:'
            candidate_section = re.search(r'Candidato(.*?)Votos\s+de\s+legenda:', section, re.DOTALL)

            if candidate_section:
                section_text = candidate_section.group(1)

                # Remove tabs e múltiplos espaços para manter apenas um espaço entre palavras
                section_text = re.sub(r'\t+', ' ', section_text)
                section_text = re.sub(r'\s+', ' ', section_text)

                # Encontra todos os candidatos e suas votações na seção extraída
                matches = pattern.findall(section_text)

                if matches:
                    for m in matches:
                        output_data += f"{m[0]} {m[1].strip()}\nVotação\n{m[2]}\n"

        # Salva o conteúdo limpo em um novo arquivo no diretório de saída, se houver dados
        if output_data:
            with open(os.path.join(output_dir, filename), 'w', encoding='utf-8') as output_file:
                output_file.write(output_data.strip())  # Remove espaços em branco no início e no final
                print(f"{filename} processado com sucesso!")
        else:
            print(f"{filename} não contém dados correspondentes ao padrão na seção especificada.")
