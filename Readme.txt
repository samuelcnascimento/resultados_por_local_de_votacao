# README - Análise de Resultados de Eleições

## Descrição do Projeto

Este projeto é uma ferramenta de análise de dados para apresentar os resultados de eleições municipais no Brasil. Ele processa os dados de votação por seção eleitoral e cruza essas informações com os locais de votação, exibindo os votos por bairro e o total geral de votos para cada candidato.

O resultado final é salvo em arquivos CSV, facilitando a visualização e análise dos dados.

---

## Estrutura do Projeto

### **Arquivos de Entrada**
1. **`locaisDeVotacao.csv`**
   - Contém os dados dos locais de votação, mapeando cada seção para um bairro.
   - Estrutura:
     ```
     Municipio;Zona;Secao;Quantidade de Eleitores Aptos;Local;Endereco;Bairro;CEP
     ```

2. **Arquivos no diretório `csvs/`**
   - Cada arquivo representa os dados de votação de uma seção específica.
   - Estrutura:
     ```
     Secao,Candidato,Votos
     ```

### **Arquivo de Saída**
1. **`resultado_eleicao_pivotado.csv`**
   - Contém os votos de cada candidato, organizados por bairro, e uma linha de total geral no final.
   - Estrutura:
     ```
     Bairro,Candidato1,Candidato2,Candidato3,...
     Centro,15,28,5,...
     Bairro X,20,10,12,...
     Total Geral,35,38,17,...
     ```

---

## Como Utilizar

### **Pré-requisitos**
- Python 3.7 ou superior
- Pacote **pandas**

Instale o pacote necessário:
```bash
pip install pandas
```

### **Execução**
1. Certifique-se de que o arquivo `locaisDeVotacao.csv` e os arquivos de seções estejam na estrutura correta.
2. Coloque os arquivos de seções no diretório `csvs/`.
3. Execute o script:
   ```bash
   python script_analise_eleicao.py
   ```
4. O resultado será gerado no arquivo `resultado_eleicao_pivotado.csv` no mesmo diretório do script.

---

## Funcionalidades

- **Mapeamento de Seções para Bairros**: Utiliza o arquivo `locaisDeVotacao.csv` para associar seções eleitorais aos bairros correspondentes.
- **Agregação de Dados**: Soma os votos por candidato para cada bairro e calcula o total geral.
- **Formato Legível**: Gera uma tabela clara e estruturada, com bairros em linhas e candidatos em colunas.

---

## Exemplo de Uso

### Dados de Entrada
**`locaisDeVotacao.csv`**
```
Municipio;Zona;Secao;Quantidade de Eleitores Aptos;Local;Endereco;Bairro;CEP
CASCAVEL;7;0001;308;E.E.F.M. RONALDO CAMINHA BARBOSA;ESTRADA DO PRATIUS, 1985;CAPONGA(ESTRADA DO PRATIUS);62850000
CASCAVEL;7;0002;313;UNIDADE BÁSICA DE SAÚDE - SEDE;RUA JOSÉ ANTONIO DE QUEIROZ, 2024;CENTRO;62850000
```

**`csvs/Secao_0001.csv`**
```
0001,10000 LUZIANE DO MUCURA,1
0001,10111 PROFESSORA NONATA COSTA,10
```

**`csvs/Secao_0002.csv`**
```
0002,10000 LUZIANE DO MUCURA,2
0002,10123 PAULINHO PROMOÇÕES,15
```

### Resultado Gerado
**`resultado_eleicao_pivotado.csv`**
```
Bairro,10000 LUZIANE DO MUCURA,10111 PROFESSORA NONATA COSTA,10123 PAULINHO PROMOÇÕES
CAPONGA(ESTRADA DO PRATIUS),1,10,0
CENTRO,2,0,15
Total Geral,3,10,15
```

---

## Contribuição

Contribuições são bem-vindas! Se você deseja melhorar o código ou adicionar novas funcionalidades, sinta-se à vontade para abrir um pull request ou enviar sugestões.

---

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
