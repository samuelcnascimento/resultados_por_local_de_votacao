import pandas as pd

def validar_arquivo(arquivo):
  # Carrega o arquivo em um DataFrame
  df = pd.read_csv(arquivo, sep='\t')

  # Define as regras de validação
  regras = {
    'Número de colunas': 10,  # Ajustar de acordo com o seu arquivo
    'Tipos de dados': {
      'Município': str,
      'Zona Eleitoral': int,
      # ... outras colunas
    }
  }

  # Aplica as regras de validação
  for coluna, tipo in regras['Tipos de dados'].items():
    if df[coluna].dtype != tipo:
      return False

  if df.shape[1] != regras['Número de colunas']:
    return False

  # Outras regras de validação podem ser adicionadas aqui

  return True

# Lista os arquivos no diretório
import os
arquivos = os.listdir('txts/')

# Valida cada arquivo
for arquivo in arquivos:
  if not validar_arquivo(f'txts/{arquivo}'):
    print(f'O arquivo {arquivo} está fora do padrão.')