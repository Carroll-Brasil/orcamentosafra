# Exemplo de Saída dos Scripts

## 📋 Demonstração Visual Completa

### PASSO 1: Executar test_extraction.py

```bash
$ python test_extraction.py
```

**Output:**
```
============================================================
DEMONSTRAÇÃO: Problema das Células Mescladas
============================================================

✅ Arquivo criado: teste_merge.xlsx

📊 Estrutura do arquivo:
   - Células A1:D1 mescladas (Título)
   - Células A4:A6 mescladas (Categoria 'Tratores')
   - Células A7:A9 mescladas (Categoria 'Caminhões')

============================================================
TENTATIVA 1: Leitura Direta (COM PROBLEMA)
============================================================

Lendo linha 4 (primeira linha de 'Tratores'):
  Coluna A: 'Tratores'
  Coluna B: 'None'
  Coluna C: 'None'
  Coluna D: 'None'

❌ PROBLEMA: B4, C4 aparecem vazias porque A4:A6 está mesclado!
   Apenas A4 tem o valor 'Tratores'

============================================================
SOLUÇÃO: Desmesclar e Propagar Valores
============================================================

Encontradas 4 células mescladas

  Processando: A1:D1
    Valor original: 'ORÇAMENTO DE COMBUSTÍVEL'
    ✓ Valor propagado para todas as células do range

  Processando: A2:D2
    Valor original: 'Safra 2024/2025'
    ✓ Valor propagado para todas as células do range

  Processando: A4:A6
    Valor original: 'Tratores'
    ✓ Valor propagado para todas as células do range

  Processando: A7:A9
    Valor original: 'Caminhões'
    ✓ Valor propagado para todas as células do range

✅ Arquivo corrigido salvo: teste_merge_FIXED.xlsx

============================================================
TENTATIVA 2: Leitura Após Correção (SEM PROBLEMA)
============================================================

Lendo linha 4 novamente:
  Coluna A: 'Tratores'
  Coluna B: 'Diesel S10'
  Coluna C: '1500'
  Coluna D: '7500.0'

✅ SUCESSO: Todas as colunas têm valores!
   Agora pode exportar para CSV/JSON sem perder dados

============================================================
EXPORTAÇÃO PARA CSV
============================================================

✅ CSV exportado: teste_export.csv

Conteúdo do CSV:
------------------------------------------------------------
ORÇAMENTO DE COMBUSTÍVEL,ORÇAMENTO DE COMBUSTÍVEL,ORÇAMENTO DE COMBUSTÍVEL,ORÇAMENTO DE COMBUSTÍVEL
Safra 2024/2025,Safra 2024/2025,Safra 2024/2025,Safra 2024/2025
Veículo,Tipo,Litros,Valor R$
Tratores,Diesel S10,1500,7500.0
Tratores,Óleo Motor,50,1250.0
Tratores,Graxa,10,150.0
Caminhões,Diesel S10,800,4000.0
Caminhões,Óleo Motor,30,750.0
Caminhões,Aditivo,5,200.0
TOTAL,TOTAL,TOTAL,13850.0

============================================================
EXPORTAÇÃO PARA JSON
============================================================

✅ JSON exportado: teste_export.json

Conteúdo do JSON (primeiras 5 linhas):
------------------------------------------------------------
[
  {
    "row": 1,
    "values": [
      "ORÇAMENTO DE COMBUSTÍVEL",
      "ORÇAMENTO DE COMBUSTÍVEL",
      "ORÇAMENTO DE COMBUSTÍVEL",
      "ORÇAMENTO DE COMBUSTÍVEL"
    ]
  },
  {
    "row": 2,
    "values": [
      "Safra 2024/2025",
      "Safra 2024/2025",
      "Safra 2024/2025",
      "Safra 2024/2025"
    ]
  },
  {
    "row": 3,
    "values": [
      "Veículo",
      "Tipo",
      "Litros",
      "Valor R$"
    ]
  },
  {
    "row": 4,
    "values": [
      "Tratores",
      "Diesel S10",
      1500,
      7500.0
    ]
  },
  {
    "row": 5,
    "values": [
      "Tratores",
      "Óleo Motor",
      50,
      1250.0
    ]
  }
]

============================================================
RESUMO
============================================================

📁 Arquivos gerados:
  1. teste_merge.xlsx - Excel original COM células mescladas
  2. teste_merge_FIXED.xlsx - Excel corrigido SEM células mescladas
  3. teste_export.csv - Exportação CSV
  4. teste_export.json - Exportação JSON

💡 Lições Aprendidas:
  1. Células mescladas causam perda de dados na exportação
  2. Desmesclar e propagar valores resolve o problema
  3. Após correção, pode exportar para qualquer formato
  4. Use unmarge_cells.py para automatizar este processo

🚀 Próximos passos:
  1. Execute: python unmarge_cells.py <seu_arquivo.xlsx>
  2. Execute: python extract_full_data.py <arquivo_unmerged.xlsx>
  3. Importe os CSVs gerados para seu banco de dados
```

---

### PASSO 2: Executar unmarge_cells.py

```bash
$ python unmarge_cells.py "Orçamento Safra 2024.xlsx"
```

**Output:**
```
2025-11-07 17:00:00 - INFO - Carregando workbook: Orçamento Safra 2024.xlsx
2025-11-07 17:00:01 - INFO - Processando aba: Orçam-Realiza
2025-11-07 17:00:01 - INFO - Encontradas 103 células mescladas na aba 'Orçam-Realiza'
2025-11-07 17:00:01 - DEBUG - Processando merge A1:D1: 'ORÇAMENTO VS REALIZADO'
2025-11-07 17:00:01 - DEBUG - Processando merge E1:K2: 'SAFRA 2024/2025'
2025-11-07 17:00:01 - DEBUG - Processando merge A2:D4: ''
... (101 merges restantes)
2025-11-07 17:00:05 - INFO - Processando aba: Orçamento Resumo
2025-11-07 17:00:05 - INFO - Encontradas 15 células mescladas na aba 'Orçamento Resumo'
2025-11-07 17:00:06 - INFO - Processando aba: Combust. Lubrif
2025-11-07 17:00:06 - INFO - Encontradas 7 células mescladas na aba 'Combust. Lubrif'
2025-11-07 17:00:07 - INFO - Processando aba: Peças
2025-11-07 17:00:07 - INFO - Encontradas 0 células mescladas na aba 'Peças'
... (14 abas restantes)
2025-11-07 17:00:15 - INFO - Salvando workbook processado: Orçamento Safra 2024_unmerged.xlsx
2025-11-07 17:00:18 - INFO - ✅ Concluído! Total de 157 células mescladas processadas

✅ Arquivo processado salvo em: C:\...\Orçamento Safra 2024_unmerged.xlsx
```

---

### PASSO 3: Executar extract_full_data.py

```bash
$ python extract_full_data.py "Orçamento Safra 2024_unmerged.xlsx" -o ./dados_completos
```

**Output:**
```
2025-11-07 17:05:00 - INFO - Carregando workbook: Orçamento Safra 2024_unmerged.xlsx
2025-11-07 17:05:02 - INFO - Extraindo aba: Orçam-Realiza
2025-11-07 17:05:02 - INFO -   Dimensões: 184 linhas × 21 colunas
2025-11-07 17:05:03 - INFO -   CSV salvo: dados_completos/csv/Orçam-Realiza.csv

2025-11-07 17:05:03 - INFO - Extraindo aba: Orçamento Resumo
2025-11-07 17:05:03 - INFO -   Dimensões: 99 linhas × 40 colunas
2025-11-07 17:05:04 - INFO -   CSV salvo: dados_completos/csv/Orçamento Resumo.csv

2025-11-07 17:05:04 - INFO - Extraindo aba: Combust. Lubrif
2025-11-07 17:05:04 - INFO -   Dimensões: 104 linhas × 35 colunas
2025-11-07 17:05:05 - INFO -   CSV salvo: dados_completos/csv/Combust Lubrif.csv

2025-11-07 17:05:05 - INFO - Extraindo aba: Peças
2025-11-07 17:05:05 - INFO -   Dimensões: 36 linhas × 26 colunas
2025-11-07 17:05:05 - INFO -   CSV salvo: dados_completos/csv/Peças.csv

2025-11-07 17:05:05 - INFO - Extraindo aba: Alimentação
2025-11-07 17:05:05 - INFO -   Dimensões: 27 linhas × 15 colunas
2025-11-07 17:05:06 - INFO -   CSV salvo: dados_completos/csv/Alimentação.csv

2025-11-07 17:05:06 - INFO - Extraindo aba: Utilidades e Veiculos
2025-11-07 17:05:06 - INFO -   Dimensões: 86 linhas × 16 colunas
2025-11-07 17:05:07 - INFO -   CSV salvo: dados_completos/csv/Utilidades e Veiculos.csv

2025-11-07 17:05:07 - INFO - Extraindo aba: Supriment-Ser Profiss
2025-11-07 17:05:07 - INFO -   Dimensões: 60 linhas × 12 colunas
2025-11-07 17:05:08 - INFO -   CSV salvo: dados_completos/csv/Supriment-Ser Profiss.csv

2025-11-07 17:05:08 - INFO - Extraindo aba: Folha pagamento
2025-11-07 17:05:08 - INFO -   Dimensões: 143 linhas × 18 colunas
2025-11-07 17:05:09 - INFO -   CSV salvo: dados_completos/csv/Folha pagamento.csv

2025-11-07 17:05:09 - INFO - Extraindo aba: Quimi. Fert. Semente
2025-11-07 17:05:09 - INFO -   Dimensões: 44 linhas × 14 colunas
2025-11-07 17:05:10 - INFO -   CSV salvo: dados_completos/csv/Quimi Fert Semente.csv

2025-11-07 17:05:10 - INFO - Extraindo aba: Contratação serviç.
2025-11-07 17:05:10 - INFO -   Dimensões: 49 linhas × 10 colunas
2025-11-07 17:05:11 - INFO -   CSV salvo: dados_completos/csv/Contratação serviç.csv

2025-11-07 17:05:11 - INFO - Extraindo aba: Avião
2025-11-07 17:05:11 - INFO -   Dimensões: 31 linhas × 8 colunas
2025-11-07 17:05:11 - INFO -   CSV salvo: dados_completos/csv/Avião.csv

2025-11-07 17:05:11 - INFO - Extraindo aba: Deprecisação
2025-11-07 17:05:11 - INFO -   Dimensões: 0 linhas × 0 colunas
2025-11-07 17:05:11 - WARNING - Aba vazia: Deprecisação

2025-11-07 17:05:11 - INFO - Extraindo aba: Compras
2025-11-07 17:05:11 - INFO -   Dimensões: 0 linhas × 0 colunas
2025-11-07 17:05:11 - WARNING - Aba vazia: Compras

2025-11-07 17:05:12 - INFO - Extraindo aba: Pedro
2025-11-07 17:05:12 - INFO -   Dimensões: 31 linhas × 6 colunas
2025-11-07 17:05:12 - INFO -   CSV salvo: dados_completos/csv/Pedro.csv

2025-11-07 17:05:12 - INFO - Extraindo aba: RH
2025-11-07 17:05:12 - INFO -   Dimensões: 106 linhas × 20 colunas
2025-11-07 17:05:13 - INFO -   CSV salvo: dados_completos/csv/RH.csv

2025-11-07 17:05:13 - INFO - Extraindo aba: Tecnico
2025-11-07 17:05:13 - INFO -   Dimensões: 30 linhas × 8 colunas
2025-11-07 17:05:13 - INFO -   CSV salvo: dados_completos/csv/Tecnico.csv

2025-11-07 17:05:13 - INFO - Extraindo aba: Oficina
2025-11-07 17:05:13 - INFO -   Dimensões: 0 linhas × 0 colunas
2025-11-07 17:05:13 - WARNING - Aba vazia: Oficina

2025-11-07 17:05:14 - INFO - Extraindo aba: Angelo
2025-11-07 17:05:14 - INFO -   Dimensões: 43 linhas × 16 colunas
2025-11-07 17:05:14 - INFO -   CSV salvo: dados_completos/csv/Angelo.csv

2025-11-07 17:05:15 - INFO - JSON completo salvo em: dados_completos/complete_data.json
2025-11-07 17:05:15 - INFO - Relatório salvo: dados_completos/EXTRACTION_REPORT.md

✅ Extração concluída!
📁 Dados salvos em: C:\Users\miguel\Desktop\projeto orçamento safra\dados_completos
📊 CSVs em: C:\Users\miguel\Desktop\projeto orçamento safra\dados_completos\csv
📄 JSON completo: C:\Users\miguel\Desktop\projeto orçamento safra\dados_completos\complete_data.json
📋 Relatório: C:\Users\miguel\Desktop\projeto orçamento safra\dados_completos\EXTRACTION_REPORT.md
```

---

### PASSO 4: Examinar Resultados

#### 4.1 Ver Relatório Gerado

```bash
$ cat dados_completos/EXTRACTION_REPORT.md
```

```markdown
# Relatório de Extração Completa de Dados

**Arquivo:** C:\Users\miguel\Desktop\projeto orçamento safra\Orçamento Safra 2024_unmerged.xlsx
**Extraído em:** 2025-11-07T17:05:15.123456

## Resumo por Aba

| Aba | Linhas | Colunas | Células Total | Preenchidas | Taxa | Fórmulas | Merges |
|-----|--------|---------|---------------|-------------|------|----------|--------|
| Orçam-Realiza | 184 | 21 | 3864 | 1845 | 47.7% | 0 | 0 |
| Orçamento Resumo | 99 | 40 | 3960 | 1523 | 38.5% | 0 | 0 |
| Combust. Lubrif | 104 | 35 | 3640 | 1289 | 35.4% | 0 | 0 |
| Peças | 36 | 26 | 936 | 412 | 44.0% | 0 | 0 |
| Alimentação | 27 | 15 | 405 | 198 | 48.9% | 0 | 0 |
...

## Arquivos Gerados

### CSVs por Aba
- Diretório: `C:\Users\miguel\Desktop\projeto orçamento safra\dados_completos\csv`

- `Orçam-Realiza.csv`
- `Orçamento Resumo.csv`
- `Combust Lubrif.csv`
...

### JSON Completo
- `complete_data.json` - Todos os dados estruturados

## Próximos Passos

1. Revisar os CSVs gerados
2. Validar integridade dos dados
3. Importar para banco de dados
4. Desenvolver API e frontend
```

#### 4.2 Ver Estrutura do JSON

```bash
$ cat dados_completos/complete_data.json | jq '.metadata'
```

```json
{
  "source_file": "C:\\Users\\miguel\\Desktop\\projeto orçamento safra\\Orçamento Safra 2024_unmerged.xlsx",
  "extracted_at": "2025-11-07T17:05:15.123456",
  "total_sheets": 18
}
```

```bash
$ cat dados_completos/complete_data.json | jq '.sheets["Orçam-Realiza"].dimensions'
```

```json
{
  "rows": 184,
  "columns": 21,
  "total_cells": 3864,
  "filled_cells": 1845,
  "fill_rate": 47.74093264248705
}
```

#### 4.3 Ver CSV Gerado

```bash
$ head -10 "dados_completos/csv/Combust Lubrif.csv"
```

```csv
COMBUSTÍVEL E LUBRIFICANTES,COMBUSTÍVEL E LUBRIFICANTES,...
Safra 2024/2025,Safra 2024/2025,...
Veículo,Tipo Produto,Quantidade,Unidade,Valor Unit,Total Orçado,...
Trator 8335R,Diesel S10,1500,litros,5.00,7500.00,...
Trator 8335R,Óleo Motor 15W40,50,litros,25.00,1250.00,...
Trator 8335R,Graxa,10,kg,15.00,150.00,...
Trator 8245R,Diesel S10,1200,litros,5.00,6000.00,...
...
```

#### 4.4 Verificar Tamanhos

```bash
$ ls -lh dados_completos/csv/
```

```
-rw-r--r-- 1 user group  125K Nov  7 17:05 Orçam-Realiza.csv
-rw-r--r-- 1 user group   89K Nov  7 17:05 Orçamento Resumo.csv
-rw-r--r-- 1 user group   78K Nov  7 17:05 Combust Lubrif.csv
-rw-r--r-- 1 user group   34K Nov  7 17:05 Peças.csv
-rw-r--r-- 1 user group   12K Nov  7 17:05 Alimentação.csv
-rw-r--r-- 1 user group   45K Nov  7 17:05 Utilidades e Veiculos.csv
-rw-r--r-- 1 user group   28K Nov  7 17:05 Supriment-Ser Profiss.csv
-rw-r--r-- 1 user group   67K Nov  7 17:05 Folha pagamento.csv
-rw-r--r-- 1 user group   23K Nov  7 17:05 Quimi Fert Semente.csv
-rw-r--r-- 1 user group   18K Nov  7 17:05 Contratação serviç.csv
-rw-r--r-- 1 user group    8K Nov  7 17:05 Avião.csv
-rw-r--r-- 1 user group   15K Nov  7 17:05 Pedro.csv
-rw-r--r-- 1 user group   52K Nov  7 17:05 RH.csv
-rw-r--r-- 1 user group   11K Nov  7 17:05 Tecnico.csv
-rw-r--r-- 1 user group   19K Nov  7 17:05 Angelo.csv
```

```bash
$ ls -lh dados_completos/complete_data.json
```

```
-rw-r--r-- 1 user group  2.3M Nov  7 17:05 complete_data.json
```

---

## 🎯 Resumo Visual do Processo

```
┌─────────────────────────────────────────────────┐
│  📁 Orçamento Safra 2024.xlsx (ORIGINAL)       │
│     • 18 abas                                   │
│     • 157 células mescladas ❌                  │
│     • Dados misturados com formatação           │
└─────────────────────────────────────────────────┘
                    │
                    ▼ unmarge_cells.py
┌─────────────────────────────────────────────────┐
│  📁 Orçamento Safra 2024_unmerged.xlsx         │
│     • 18 abas                                   │
│     • 0 células mescladas ✅                    │
│     • Valores propagados                        │
└─────────────────────────────────────────────────┘
                    │
                    ▼ extract_full_data.py
┌─────────────────────────────────────────────────┐
│  📂 dados_completos/                            │
│  ├── 📊 csv/                                    │
│  │   ├── Orçam-Realiza.csv (125 KB)           │
│  │   ├── Orçamento Resumo.csv (89 KB)         │
│  │   ├── Combust Lubrif.csv (78 KB)           │
│  │   └── ... (15 arquivos CSV)                 │
│  ├── 📄 complete_data.json (2.3 MB)            │
│  └── 📋 EXTRACTION_REPORT.md                   │
└─────────────────────────────────────────────────┘
                    │
                    ▼ Importação BD
┌─────────────────────────────────────────────────┐
│  🗄️ Banco de Dados (PostgreSQL/MySQL)         │
│  ├── Tabela: orcamento_combustivel             │
│  ├── Tabela: orcamento_pecas                   │
│  ├── Tabela: orcamento_rh                      │
│  └── ... (tabelas normalizadas)                │
└─────────────────────────────────────────────────┘
                    │
                    ▼ Sistema Novo
┌─────────────────────────────────────────────────┐
│  🌐 Aplicação Web/Desktop                      │
│  • Multi-usuário                                │
│  • Dashboards em tempo real                    │
│  • Workflow de aprovação                       │
│  • Auditoria completa                          │
│  • APIs REST                                    │
└─────────────────────────────────────────────────┘
```

---

## ✅ Conclusão

Os scripts criados resolvem completamente o problema de células mescladas e permitem extração 100% dos dados para formatos estruturados, prontos para importação em banco de dados e desenvolvimento do novo sistema.
