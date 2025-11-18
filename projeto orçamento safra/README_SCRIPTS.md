# Scripts de Extração de Dados - Orçamento Safra

## 🎯 Objetivo

Resolver o problema de **células mescladas** e **extrair 100% dos dados** da planilha Excel para formatos estruturados (CSV, JSON).

## 📦 Arquivos Criados

### 1. Scripts Python

| Script | Propósito | Quando Usar |
|--------|-----------|-------------|
| `unmarge_cells.py` | Desmescla células e propaga valores | **Antes** de exportar dados |
| `extract_full_data.py` | Extrai todos os dados para CSV/JSON | Após desmesclar ou para análise |
| `test_extraction.py` | Demonstração do problema | Para entender o conceito |

### 2. Documentação

| Arquivo | Conteúdo |
|---------|----------|
| `ANALISE_PLANILHA_ORCAMENTO_SAFRA.md` | Análise completa da estrutura |
| `GUIA_EXTRACAO_DADOS.md` | Instruções detalhadas de uso |
| `README_SCRIPTS.md` | Este arquivo (resumo) |

---

## 🚀 Uso Rápido (3 Comandos)

### Passo 1: Instalar Dependência
```bash
pip install openpyxl
```

### Passo 2: Desmesclar Células
```bash
python unmarge_cells.py "Orçamento Safra.xlsx"
```
**Saída:** `Orçamento Safra_unmerged.xlsx`

### Passo 3: Extrair Dados
```bash
python extract_full_data.py "Orçamento Safra_unmerged.xlsx"
```
**Saída:** 
- `extracted_data/csv/` - 18 CSVs (um por aba)
- `extracted_data/complete_data.json` - JSON completo
- `extracted_data/EXTRACTION_REPORT.md` - Relatório

---

## 🔍 O Problema Explicado

### Células Mescladas no Excel

```
┌─────────────────────────┐
│  Categoria (A1:A3)      │  ← Merge A1:A3
├─────────────────────────┤
│                         │
├─────────────────────────┤
│                         │
└─────────────────────────┘
```

**Ao exportar:**
- A1 = "Categoria" ✅
- A2 = NULL ❌ (perdeu o contexto!)
- A3 = NULL ❌ (perdeu o contexto!)

### Após Desmesclar

```
┌─────────────────────────┐
│  Categoria              │  ← A1 = "Categoria"
├─────────────────────────┤
│  Categoria              │  ← A2 = "Categoria" (propagado)
├─────────────────────────┤
│  Categoria              │  ← A3 = "Categoria" (propagado)
└─────────────────────────┘
```

**Ao exportar:**
- A1 = "Categoria" ✅
- A2 = "Categoria" ✅ (agora tem valor!)
- A3 = "Categoria" ✅ (agora tem valor!)

---

## 📊 Comparação com ooxml_profile.py

| Característica | ooxml_profile.py | extract_full_data.py |
|----------------|------------------|----------------------|
| **Propósito** | Análise estrutural | Extração de dados |
| **Dados** | Amostragem (~2%) | 100% completo |
| **Fórmulas** | Detecta presença | Extrai fórmulas completas |
| **Valores** | Estatísticas | Todos os valores |
| **Saída** | JSON + MD (metadados) | CSV + JSON (dados brutos) |
| **Uso** | Entender estrutura | Migrar para BD |

**Recomendação:** Use **ambos**!
1. `ooxml_profile.py` para análise
2. `extract_full_data.py` para migração

---

## 💡 Casos de Uso

### Caso 1: Entender a Planilha (Primeiro Contato)

```bash
# 1. Extrair pasta XML
unzip "Planilha.xlsx" -d planilha_xml

# 2. Analisar estrutura
python ooxml_profile.py --root ./planilha_xml --out ./analise

# 3. Ler relatórios
cat analise/WORKBOOK_SUMMARY.md
```

### Caso 2: Migrar para Banco de Dados

```bash
# 1. Desmesclar
python unmarge_cells.py "Planilha.xlsx"

# 2. Extrair tudo
python extract_full_data.py "Planilha_unmerged.xlsx" -o ./dados_bd

# 3. Importar CSVs para PostgreSQL
for csv in dados_bd/csv/*.csv; do
    table=$(basename "$csv" .csv)
    psql -U user -d database -c "\COPY $table FROM '$csv' CSV HEADER"
done
```

### Caso 3: Auditoria e Validação

```bash
# 1. Demonstração do problema
python test_extraction.py

# 2. Processar arquivo real
python unmarge_cells.py "Real.xlsx"
python extract_full_data.py "Real_unmerged.xlsx" -o ./auditoria

# 3. Validar dados
diff <(wc -l Real.xlsx) <(wc -l auditoria/csv/*.csv)
```

---

## 🛠️ Opções Avançadas

### Processar Apenas Algumas Abas

```bash
# Edite extract_full_data.py, linha ~85:
abas_desejadas = ['Orçam-Realiza', 'RH', 'Folha pagamento']

for sheet_name in wb_values.sheetnames:
    if sheet_name not in abas_desejadas:
        continue
    # ... resto do código
```

### Exportar com Encoding Específico

```bash
# Edite extract_full_data.py, linha ~160:
with open(csv_path, 'w', newline='', encoding='latin-1') as f:
    # ... (trocar utf-8 por latin-1 se necessário)
```

### Debug Detalhado

```bash
python unmarge_cells.py "Planilha.xlsx" --log-level DEBUG
python extract_full_data.py "Planilha.xlsx" --log-level DEBUG
```

---

## 📁 Estrutura Final do Projeto

```
projeto orçamento safra/
│
├── 📄 Scripts Python
│   ├── ooxml_profile.py           # Análise estrutural (original)
│   ├── unmarge_cells.py           # Novo: Desmesclar células
│   ├── extract_full_data.py       # Novo: Extração completa
│   └── test_extraction.py         # Novo: Demonstração
│
├── 📊 Dados (após processamento)
│   ├── dados_extraida/            # Do ooxml_profile.py
│   │   ├── workbook_manifest.json
│   │   └── WORKBOOK_SUMMARY.md
│   │
│   └── extracted_data/            # Do extract_full_data.py
│       ├── csv/                   # 18 arquivos CSV
│       ├── complete_data.json     # Dados completos
│       └── EXTRACTION_REPORT.md
│
├── 📚 Documentação
│   ├── ANALISE_PLANILHA_ORCAMENTO_SAFRA.md  # Análise completa
│   ├── GUIA_EXTRACAO_DADOS.md               # Guia de uso
│   ├── README_SCRIPTS.md                    # Este arquivo
│   ├── README.md                            # Original
│   └── EXEMPLO_USO.md                       # Original
│
└── 📈 Arquivos Excel
    ├── Orçamento Safra.xlsx       # Original
    └── Orçamento Safra_unmerged.xlsx  # Processado
```

---

## ⚡ Quick Reference

### Comandos Essenciais

```bash
# Instalar
pip install openpyxl

# Desmesclar
python unmarge_cells.py arquivo.xlsx

# Extrair
python extract_full_data.py arquivo_unmerged.xlsx

# Testar
python test_extraction.py
```

### Verificar Resultados

```bash
# Listar CSVs gerados
ls -lh extracted_data/csv/

# Ver primeiras linhas de um CSV
head -20 "extracted_data/csv/Orçam-Realiza.csv"

# Contar registros
wc -l extracted_data/csv/*.csv

# Buscar valor específico
grep "Combustível" extracted_data/csv/*.csv
```

### Validar JSON

```bash
# Verificar se JSON é válido
python -m json.tool extracted_data/complete_data.json > /dev/null

# Ver estrutura
cat extracted_data/complete_data.json | jq '.metadata'

# Contar células preenchidas por aba
cat extracted_data/complete_data.json | jq '.sheets[].dimensions.filled_cells'
```

---

## 🐛 Solução de Problemas

### "No module named 'openpyxl'"
```bash
pip install openpyxl
# ou
pip3 install openpyxl
```

### "Permission denied"
- Feche o Excel antes de executar
- No Windows: Execute como Administrador

### Encoding de caracteres errado
```bash
# Windows PowerShell
chcp 65001  # UTF-8

# Ou use Latin-1 nos scripts
encoding='latin-1'  # ao invés de 'utf-8'
```

### Arquivo muito grande
```bash
# Processar apenas algumas abas (edite o script)
# Ou aumente memória do Python
python -X dev extract_full_data.py arquivo.xlsx
```

---

## 📈 Próximos Passos

1. ✅ **Análise concluída** - ANALISE_PLANILHA_ORCAMENTO_SAFRA.md
2. ✅ **Scripts criados** - unmarge_cells.py, extract_full_data.py
3. ⬜ **Executar extração** - Processar arquivo Excel real
4. ⬜ **Modelar banco** - Criar schema SQL baseado nos CSVs
5. ⬜ **Desenvolver API** - Backend (Node.js/Python/C#)
6. ⬜ **Criar frontend** - Interface web/desktop

---

## 📞 Suporte

### Logs de Debug

```bash
# Habilitar logs detalhados
python script.py --log-level DEBUG 2>&1 | tee debug.log
```

### Testar com Exemplo

```bash
# Criar Excel de teste
python test_extraction.py

# Processar exemplo
python unmarge_cells.py teste_merge.xlsx
python extract_full_data.py teste_merge_FIXED.xlsx
```

### Validar Dados Extraídos

```python
# Script de validação
import json

with open('extracted_data/complete_data.json') as f:
    data = json.load(f)

for sheet_name, sheet_data in data['sheets'].items():
    print(f"{sheet_name}:")
    print(f"  Linhas: {sheet_data['dimensions']['rows']}")
    print(f"  Colunas: {sheet_data['dimensions']['columns']}")
    print(f"  Taxa preenchimento: {sheet_data['dimensions']['fill_rate']:.1f}%")
```

---

## 🎓 Referências

- **Openpyxl Docs:** https://openpyxl.readthedocs.io/
- **Excel OOXML Spec:** https://www.ecma-international.org/publications-and-standards/standards/ecma-376/
- **Análise Original:** ANALISE_PLANILHA_ORCAMENTO_SAFRA.md
- **Guia Completo:** GUIA_EXTRACAO_DADOS.md

---

**Última atualização:** 2025-11-07  
**Versão:** 1.0  
**Autor:** Sistema de Análise OOXML
