# Análise de Resultados de Eleições

Este repositório contém uma ferramenta para análise de resultados de eleições municipais no Brasil. O projeto processa dados de votação de diferentes seções eleitorais e cruza essas informações com os locais de votação para gerar relatórios claros e organizados.

O principal objetivo é apresentar os votos de cada candidato por bairro, bem como os totais gerais, em um formato tabular legível.

---

## 🚀 Funcionalidades

- **Mapeamento de Seções para Bairros**: Utiliza um arquivo mestre para associar seções aos bairros correspondentes.
- **Agregação de Dados**: Soma os votos por candidato em cada bairro e calcula os totais gerais.
- **Geração de Relatórios**: Produz um arquivo CSV com bairros em linhas e candidatos em colunas.

---

## 🛠️ Tecnologias Utilizadas

- **Python**: Linguagem principal para o processamento dos dados.
- **Pandas**: Biblioteca para manipulação e análise de dados.
- **CSV**: Formato de entrada e saída dos arquivos.

---

## 📂 Estrutura do Repositório

```plaintext
├── locaisDeVotacao.csv  # Dados mapeando seções para bairros
├── csvs/                # Diretório contendo os arquivos de votação por seção
│   ├── Secao_0001.csv
│   ├── Secao_0002.csv
│   └── ...
├── script_analise_eleicao.py  # Script principal de processamento
├── resultado_eleicao_pivotado.csv  # Arquivo de saída gerado
├── README.md            # Documentação do projeto
```

---

## 📋 Como Utilizar

### 1. Pré-requisitos

- Python 3.7 ou superior
- Instale o pacote `pandas`:
  ```bash
  pip install pandas
  ```

### 2. Estrutura Esperada dos Arquivos

#### **`locaisDeVotacao.csv`**
Arquivo que relaciona cada seção eleitoral ao bairro correspondente. Deve conter as seguintes colunas (delimitadas por `;`):

```
Municipio;Zona;Secao;Quantidade de Eleitores Aptos;Local;Endereco;Bairro;CEP
```

Exemplo:
```
CASCAVEL;7;0001;308;E.E.F.M. RONALDO CAMINHA BARBOSA;ESTRADA DO PRATIUS, 1985;CAPONGA(ESTRADA DO PRATIUS);62850000
CASCAVEL;7;0002;313;UNIDADE BÁSICA DE SAÚDE - SEDE;RUA JOSÉ ANTONIO DE QUEIROZ, 2024;CENTRO;62850000
```

#### **Arquivos no Diretório `csvs/`**
Cada arquivo representa os votos em uma seção eleitoral. Deve ter as seguintes colunas (sem cabeçalho):

```
Secao,Candidato,Votos
```

Exemplo:
```
0001,10000 LUZIANE DO MUCURA,1
0001,10111 PROFESSORA NONATA COSTA,10
```

### 3. Executando o Script

1. Certifique-se de que o arquivo `locaisDeVotacao.csv` e os arquivos de votação estão no formato correto.
2. Execute o script principal:
   ```bash
   python script_analise_eleicao.py
   ```
3. O relatório será gerado no arquivo `resultado_eleicao_pivotado.csv`.

---

## 📊 Exemplo de Saída

**Arquivo Gerado: `resultado_eleicao_pivotado.csv`**
```
Bairro,10000 LUZIANE DO MUCURA,10111 PROFESSORA NONATA COSTA,10123 PAULINHO PROMOÇÕES
CAPONGA(ESTRADA DO PRATIUS),1,10,0
CENTRO,2,0,15
Total Geral,3,10,15
```

---

## 🤝 Contribuições

Contribuições são bem-vindas! Se você tiver sugestões de melhorias, correções ou novas funcionalidades, abra uma *issue* ou envie um *pull request*. 

---

## 📝 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).