import os
import pdfkit
import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Configuração do caminho do GeckoDriver e wkhtmltopdf
geckodriver_path = "/usr/local/bin/geckodriver"
wkhtmltopdf_path = '/usr/bin/wkhtmltopdf'  # ajuste para o caminho correto
config = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path)

# Configurações do Firefox
options = Options()
profile_path = "/home/samuel/snap/firefox/common/.mozilla/firefox/dhcazztx.resultados"
options.set_preference("profile", profile_path)
options.set_preference("geo.enabled", True)
options.set_preference("geo.provider.use_corelocation", True)
options.set_preference("geo.prompt.testing", True)
options.set_preference("geo.prompt.testing.allow", True)

# Inicializa o Selenium com Firefox
service = Service(geckodriver_path)
driver = webdriver.Firefox(service=service, options=options)

# Diretório de destino dos PDFs
output_dir = 'docs/'
os.makedirs(output_dir, exist_ok=True)

# URL base
base_url = 'https://resultados.tse.jus.br/oficial/app/index.html#/eleicao;e=e619;uf=ce;mu=13692;ufbu=ce;mubu=13692;tipo=3;zn=0007;se={}/dados-de-urna/boletim-de-urna'

# Lista das seções existentes
valid_sections = [...]  # lista de seções válida

# Itera sobre as seções
for section_number in range(0, 299):
    if section_number not in valid_sections:
        print(f"Seção {section_number} não é válida. Pulando.")
        continue
    
    section_id = f"{section_number:04d}"
    url = base_url.format(section_id)
    file_name = f'Secao_{section_id}.pdf'
    file_path = os.path.join(output_dir, file_name)

    print(f"Acessando URL: {url}")
    driver.get(url)
    driver.refresh()
    time.sleep(5)  # Aumenta o tempo de espera

    # Captura o HTML da página carregada
    page_html = driver.page_source

    # Salva HTML para depuração
    with open(f'debug_{section_id}.html', 'w', encoding='utf-8') as f:
        f.write(page_html)

    # Converte o HTML carregado para PDF
    try:
        pdfkit.from_string(page_html, file_path, configuration=config, options={'no-stop-slow-scripts': ''})
        print(f'Seção {section_id} salva como {file_name}')
    except Exception as e:
        print(f'Erro ao salvar a seção {section_id} como PDF: {e}')

# Fecha o navegador
driver.quit()

print("Processo de conversão concluído.")
