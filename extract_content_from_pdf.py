import os
import PyPDF2

def copy_pdf_content(input_pdf_path, output_txt_path):
    try:
        # Abre o arquivo PDF
        with open(input_pdf_path, 'rb') as pdf_file:
            # Cria um objeto PDF Reader
            pdf_reader = PyPDF2.PdfReader(pdf_file)

            # Abre o arquivo TXT de saída
            with open(output_txt_path, 'w', encoding='utf-8') as txt_file:
                # Itera por cada página do PDF
                for page in pdf_reader.pages:
                    # Extrai texto da página
                    text = page.extract_text()
                    if text:  # Verifica se o texto não é None
                        # Escreve o texto no arquivo TXT
                        txt_file.write(text + '\n')  # Adiciona uma nova linha após cada página
            print(f"Conteúdo do PDF foi copiado com sucesso para {output_txt_path}.")
            return True  # Retorna True se o arquivo foi copiado com sucesso

    except FileNotFoundError:
        print(f"Erro: O arquivo {input_pdf_path} não foi encontrado.")
        return False
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return False

# Criar diretório 'txts/' se não existir
if not os.path.exists('txts'):
    os.makedirs('txts')

# Contador de arquivos convertidos
soma = 0

# Itera pelos arquivos PDF na pasta 'docs/'
docs_path = 'docs/'
for filename in os.listdir(docs_path):
    # Verifica se o arquivo é um PDF que começa com 'Secao_' e termina com '.pdf'
    if filename.startswith('Secao_') and filename.endswith('.pdf'):
        input_pdf = os.path.join(docs_path, filename)

        # Define o caminho para o arquivo TXT de saída
        output_txt = os.path.join('txts', f"{filename[:-4]}.txt")  # Remove '.pdf' do nome do arquivo

        # Chama a função para copiar o conteúdo do PDF
        if copy_pdf_content(input_pdf, output_txt):
            soma += 1  # Incrementa a contagem de arquivos convertidos

# Exibe a quantidade total de arquivos convertidos
print(f"Qtd de arquivos convertidos: {soma}")
