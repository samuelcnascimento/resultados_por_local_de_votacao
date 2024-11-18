import os
import pdfkit
import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By  # Adicione esta linha

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

# URL base
base_url = 'https://resultados.tse.jus.br/oficial/app/index.html#/eleicao;e=e619;uf=ce;mu=13692;ufbu=ce;mubu=13692;tipo=3;zn=0007;se={}/dados-de-urna/boletim-de-urna'

# Lista das seções existentes
valid_sections = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15,
    17, 18, 19, 20, 21, 22, 23, 24, 25, 28, 34, 37,
    40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51,
    52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63,
    64, 65, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81,
    82, 83, 84, 85, 89, 90, 91, 92, 93, 96, 98, 99,
    100, 101, 102, 103, 106, 107, 108, 109, 110, 111,
    112, 114, 115, 118, 119, 121, 123, 124, 128, 129,
    130, 131, 132, 133, 135, 138, 139, 140, 141, 143,
    144, 146, 147, 148, 149, 150, 151, 152, 153, 155,
    156, 157, 158, 159, 160, 161, 163, 165, 166, 167,
    168, 169, 170, 171, 172, 173, 174, 175, 176, 177,
    181, 184, 185, 186, 187, 188, 189, 190, 191, 192,
    193, 195, 197, 198, 199, 200, 201, 202, 204, 205,
    206, 207, 210, 211, 212, 213, 214, 216, 217, 218,
    222, 223, 225, 226, 227, 229, 230, 233, 234, 237,
    238, 239, 240, 243, 245, 246, 247, 248, 249, 250,
    251, 252, 253, 254, 255, 256, 258, 259, 261, 262,
    263, 265, 266, 268, 270, 271, 272, 276, 278, 280,
    281, 283, 284, 285, 286, 290, 292, 294
]

# Nome a ser pesquisado
search_name = "PAULINHO PROMOÇÕES"  # Substitua pelo nome que deseja pesquisar

# Itera sobre as seções
for section_number in range(0, 299):  # Ajuste o intervalo conforme necessário
    if section_number not in valid_sections:
        print(f"Seção {section_number} não é válida. Pulando.")
        continue
    
    section_id = f"{section_number:04d}"
    url = base_url.format(section_id)

    # Acessa a URL da seção
    driver.get(url)
    if section_id == 1:
        driver.refresh()
    time.sleep(3)  # Espera o carregamento da página
    driver.refresh()

     # Procura pelo nome na página
    try:
        # Tenta encontrar o elemento que contém o nome
        element = driver.find_element(By.XPATH, f"//*[contains(text(), '{search_name}')]")
        print(f"Nome '{search_name}' encontrado na seção {section_id}.")
        
        # Para destacar o texto encontrado, você pode alterar o estilo com JavaScript
        driver.execute_script("arguments[0].style.backgroundColor = 'yellow';", element)

        # Espera para visualizar o destaque
        time.sleep(5)
    except:
        print(f"Nome '{search_name}' não encontrado na seção {section_id}.")

# Fecha o navegador
driver.quit()

print("Processo de conversão concluído.")
