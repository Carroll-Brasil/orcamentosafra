# Guia Completo de Extração de Dados

## 🎯 Problema das Células Mescladas

### O Que Acontece

```
Excel Original (células mescladas):
┌───────────────────────┐
│  Título (A1:C1)       │
├───────┬───────┬───────┤
│ Valor │       │       │  ← B1 e C1 estão vazios
└───────┴───────┴───────┘

Exportação Direta (ERRO):
A1: "Título"
B1: null      ← Perde contexto!
C1: null      ← Perde contexto!
```

### Solução

```
Após Desmesclar e Propagar:
┌───────┬───────┬───────┐
│ Título│ Título│ Título│  ← Valor replicado
├───────┼───────┼───────┤
│ Valor │ Valor │ Valor │
└───────┴───────┴───────┘

Exportação Correta:
A1: "Título"
B1: "Título"  ← Agora tem valor!
C1: "Título"  ← Agora tem valor!
```

---

## 📋 Passo a Passo Completo

### ETAPA 1: Instalar Dependências

```bash
# Instalar openpyxl (necessário para ambos os scripts)
pip install openpyxl
```

### ETAPA 2: Desmesclar Células

**Objetivo:** Criar versão "limpa" do Excel sem células mescladas

```bash
# Sintaxe
python unmarge_cells.py <arquivo_excel> [opções]

# Exemplo
python unmarge_cells.py "Orçamento Safra 2024.xlsx"

# Com saída customizada
python unmarge_cells.py "Orçamento Safra 2024.xlsx" -o "Orcamento_Limpo.xlsx"

# Com debug detalhado
python unmarge_cells.py "Orçamento Safra 2024.xlsx" --log-level DEBUG
```

**Saída:**
```
2024-11-07 17:00:00 - INFO - Carregando workbook: Orçamento Safra 2024.xlsx
2024-11-07 17:00:01 - INFO - Processando aba: Orçam-Realiza
2024-11-07 17:00:01 - INFO - Encontradas 103 células mescladas na aba 'Orçam-Realiza'
2024-11-07 17:00:02 - INFO - Processando aba: Orçamento Resumo
2024-11-07 17:00:02 - INFO - Encontradas 15 células mescladas na aba 'Orçamento Resumo'
...
2024-11-07 17:00:10 - INFO - ✅ Concluído! Total de 150 células mescladas processadas

✅ Arquivo processado salvo em: Orçamento Safra 2024_unmerged.xlsx
```

### ETAPA 3: Extrair Dados Completos

**Objetivo:** Exportar TODOS os dados para CSV e JSON

```bash
# Usando arquivo original (com merges)
python extract_full_data.py "Orçamento Safra 2024.xlsx"

# OU usando arquivo já desmesclado (RECOMENDADO)
python extract_full_data.py "Orçamento Safra 2024_unmerged.xlsx" -o ./dados_completos

# Com debug
python extract_full_data.py "Orçamento Safra 2024_unmerged.xlsx" --log-level DEBUG
```

**Saída:**
```
2024-11-07 17:05:00 - INFO - Carregando workbook: Orçamento Safra 2024_unmerged.xlsx
2024-11-07 17:05:01 - INFO - Extraindo aba: Orçam-Realiza
2024-11-07 17:05:01 - INFO -   Dimensões: 184 linhas × 21 colunas
2024-11-07 17:05:02 - INFO -   CSV salvo: extracted_data/csv/Orçam-Realiza.csv
2024-11-07 17:05:02 - INFO - Extraindo aba: Orçamento Resumo
2024-11-07 17:05:02 - INFO -   Dimensões: 99 linhas × 40 colunas
...
2024-11-07 17:05:30 - INFO - JSON completo salvo em: extracted_data/complete_data.json
2024-11-07 17:05:30 - INFO - Relatório salvo: extracted_data/EXTRACTION_REPORT.md

✅ Extração concluída!
📁 Dados salvos em: C:\...\extracted_data
📊 CSVs em: C:\...\extracted_data\csv
📄 JSON completo: C:\...\extracted_data\complete_data.json
📋 Relatório: C:\...\extracted_data\EXTRACTION_REPORT.md
```

---

## 📂 Estrutura de Arquivos Gerados

```
projeto orçamento safra/
│
├── Orçamento Safra 2024.xlsx                    ← Original
├── Orçamento Safra 2024_unmerged.xlsx           ← Desmesclado (ETAPA 1)
│
├── extracted_data/                               ← Dados extraídos (ETAPA 2)
│   ├── csv/
│   │   ├── Orçam-Realiza.csv
│   │   ├── Orçamento Resumo.csv
│   │   ├── Combust Lubrif.csv
│   │   ├── Peças.csv
│   │   ├── Alimentação.csv
│   │   ├── Utilidades e Veiculos.csv
│   │   ├── Supriment-Ser Profiss.csv
│   │   ├── Folha pagamento.csv
│   │   ├── Quimi Fert Semente.csv
│   │   ├── Contratação serviç.csv
│   │   ├── Avião.csv
│   │   ├── Pedro.csv
│   │   ├── RH.csv
│   │   ├── Tecnico.csv
│   │   └── Angelo.csv
│   │
│   ├── complete_data.json                       ← JSON estruturado completo
│   └── EXTRACTION_REPORT.md                     ← Relatório da extração
│
├── dados_extraida/                              ← Do ooxml_profile.py (análise)
│   ├── workbook_manifest.json
│   └── WORKBOOK_SUMMARY.md
│
├── unmarge_cells.py                             ← Script 1
├── extract_full_data.py                         ← Script 2
└── ANALISE_PLANILHA_ORCAMENTO_SAFRA.md         ← Análise completa
```

---

## 🔍 Diferenças Entre os Scripts

### ooxml_profile.py (Análise)
- ✅ Faz **amostragem** dos dados
- ✅ Gera **metadados** (estrutura, tipos, estatísticas)
- ✅ Identifica problemas (merges, validações)
- ❌ **Não extrai** todos os valores das células

### extract_full_data.py (Extração)
- ✅ Extrai **100%** dos dados
- ✅ Preserva **fórmulas**
- ✅ Exporta para **CSV** e **JSON**
- ✅ Pronto para **importação** em banco de dados

### unmarge_cells.py (Preparação)
- ✅ **Desmescla** células
- ✅ **Propaga** valores
- ✅ Preserva **formatação**
- ✅ Facilita processamento posterior

---

## 💡 Casos de Uso

### Caso 1: Análise Rápida
```bash
# Só quer entender a estrutura
python ooxml_profile.py --root ./dados_extraida --out ./analise
```

### Caso 2: Migração para Banco de Dados
```bash
# 1. Desmesclar
python unmarge_cells.py "Planilha.xlsx"

# 2. Extrair tudo
python extract_full_data.py "Planilha_unmerged.xlsx" -o ./dados_db

# 3. Importar CSVs para PostgreSQL/MySQL
psql -U user -d database -c "\COPY tabela FROM 'dados_db/csv/Aba.csv' CSV HEADER"
```

### Caso 3: Auditoria Completa
```bash
# 1. Análise estrutural
python ooxml_profile.py --root ./dados_extraida --out ./auditoria

# 2. Extração completa
python extract_full_data.py "Planilha.xlsx" -o ./auditoria/dados

# 3. Comparar com JSON
diff auditoria/workbook_manifest.json auditoria/dados/complete_data.json
```

---

## ⚙️ Opções Avançadas

### Processar Apenas Algumas Abas

Edite `extract_full_data.py`:

```python
# Linha ~85, adicione filtro:
for sheet_name in wb_values.sheetnames:
    # Processar apenas abas específicas
    if sheet_name not in ['Orçam-Realiza', 'Orçamento Resumo', 'RH']:
        continue
    
    self.logger.info(f"Extraindo aba: {sheet_name}")
    ...
```

### Exportar para Outros Formatos

**SQL INSERT Statements:**
```python
def export_to_sql(sheet_data, table_name):
    sql_lines = []
    for row_idx, row in enumerate(sheet_data['data']):
        if row_idx == 0:
            continue  # Skip header
        
        values = [f"'{cell['value']}'" if cell['value'] else 'NULL' for cell in row]
        sql_lines.append(f"INSERT INTO {table_name} VALUES ({', '.join(values)});")
    
    return '\n'.join(sql_lines)
```

**Parquet (para Big Data):**
```python
import pandas as pd

# Converter para DataFrame
df = pd.DataFrame([
    [cell['value'] for cell in row]
    for row in sheet_data['data']
])

# Salvar como Parquet
df.to_parquet('aba.parquet', compression='snappy')
```

---

## 🐛 Troubleshooting

### Erro: "No module named 'openpyxl'"
```bash
pip install openpyxl
```

### Erro: "Permission denied"
- Feche o Excel antes de processar
- Execute com permissões de administrador

### Arquivo muito grande / lento
- Use `extract_full_data.py` com filtro de abas
- Aumente memória disponível
- Processe em lotes

### Caracteres especiais quebrados
- Certifique-se que o terminal use UTF-8
- No Windows: `chcp 65001`

### Fórmulas não aparecem
- Use `openpyxl.load_workbook(file, data_only=False)`
- Já implementado no `extract_full_data.py`

---

## 📊 Validação dos Dados Extraídos

### 1. Verificar Integridade

```python
import json

with open('extracted_data/complete_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"Total de abas: {len(data['sheets'])}")

for sheet_name, sheet_data in data['sheets'].items():
    print(f"\n{sheet_name}:")
    print(f"  Células totais: {sheet_data['dimensions']['total_cells']}")
    print(f"  Preenchidas: {sheet_data['dimensions']['filled_cells']}")
    print(f"  Taxa: {sheet_data['dimensions']['fill_rate']:.2f}%")
    print(f"  Fórmulas: {sheet_data['formula_count']}")
```

### 2. Comparar CSV com Original

```bash
# Contar linhas
wc -l extracted_data/csv/*.csv

# Ver primeiras linhas
head -20 "extracted_data/csv/Orçam-Realiza.csv"

# Procurar valores específicos
grep "Combustível" extracted_data/csv/*.csv
```

---

## 🚀 Próximos Passos

1. ✅ **Análise estrutural** - Concluída (ANALISE_PLANILHA_ORCAMENTO_SAFRA.md)
2. ✅ **Scripts de extração** - Criados (unmarge_cells.py, extract_full_data.py)
3. ⬜ **Executar extração** - Aguardando arquivo Excel real
4. ⬜ **Modelar banco de dados** - Baseado nos CSVs gerados
5. ⬜ **Desenvolver API** - Backend para novo sistema
6. ⬜ **Criar interface** - Frontend web/desktop

---

## 📞 Suporte

Problemas com os scripts? 
1. Verifique logs com `--log-level DEBUG`
2. Confirme que openpyxl está instalado
3. Teste com arquivo Excel de exemplo primeiro
