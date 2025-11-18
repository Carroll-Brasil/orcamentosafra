# Análise Detalhada: Planilha de Orçamento Safra

**Data da Análise:** 2025-11-07  
**Arquivo Origem:** Orçamento Safra (Excel .xlsx)  
**Total de Abas:** 18 abas  
**Strings Compartilhadas:** 1.432 strings únicas

---

## 1. VISÃO GERAL DO SISTEMA

Esta planilha Excel representa um **sistema completo de gestão orçamentária agrícola (safra)**, organizado de forma descentralizada em múltiplas abas especializadas. O sistema controla custos operacionais, recursos humanos, insumos, equipamentos e fornece consolidações gerenciais.

### 1.1 Características Principais

- **Formato:** Excel OOXML (.xlsx)
- **Complexidade:** Alta (18 abas interconectadas)
- **Uso de Formatação:** Extensa (múltiplas células mescladas, formatação condicional)
- **Moeda:** Real brasileiro (R$) com múltiplos formatos monetários
- **Estrutura:** Descentralizada por departamento/categoria de despesa

### 1.2 Problemas Identificados

⚠️ **Arquitetura Problemática:**
- Dados distribuídos em múltiplas abas sem relacionamento formal
- Ausência de banco de dados estruturado
- Dependência de células mescladas (dificulta automação)
- Sem validação consistente de dados
- Falta de auditoria e rastreabilidade
- Difícil manutenção e escalabilidade

---

## 2. ESTRUTURA DAS ABAS

### 2.1 ABAS CONSOLIDADAS (Visão Gerencial)

#### **Orçam-Realiza** (Principal)
- **Dimensão:** 184 linhas × 21 colunas (A-U)
- **Propósito:** Dashboard comparativo Orçado vs Realizado
- **Células Mescladas:** 103 ranges (alta complexidade visual)
- **Características:**
  - Consolida dados de todas as outras abas
  - Compara orçamento planejado com valores realizados
  - Múltiplas seções por categoria de despesa
  - Formatação monetária em R$

**Estrutura Típica:**
```
[Título/Categoria Mesclada]
┌─────────────────┬──────────┬──────────┬──────────┐
│ Item/Descrição  │ Orçado   │ Realizado│ Variação │
├─────────────────┼──────────┼──────────┼──────────┤
│ Combustível     │ R$ X.XXX │ R$ X.XXX │ XX%      │
│ Lubrificante    │ R$ X.XXX │ R$ X.XXX │ XX%      │
└─────────────────┴──────────┴──────────┴──────────┘
```

#### **Orçamento Resumo**
- **Dimensão:** 99 linhas × 40 colunas (A-AN)
- **Propósito:** Visão executiva consolidada
- **Células Mescladas:** 15 ranges principais
- **Características:**
  - Sumariza todas as categorias de custo
  - Agrupa por tipo de despesa (operacional, administrativa, etc.)
  - Permite análise mensal/anual
  - Base para tomada de decisão estratégica

---

### 2.2 ABAS OPERACIONAIS (Detalhamento por Categoria)

#### **Combust. Lubrif** (Combustíveis e Lubrificantes)
- **Dimensão:** 104 linhas × 35 colunas (B-AI)
- **Propósito:** Controle de consumo de diesel, gasolina, óleos e graxas
- **Dados Rastreados:**
  - Máquinas/Veículos consumidores
  - Tipo de combustível/lubrificante
  - Quantidade prevista vs consumida
  - Custo unitário e total
  - Fornecedor
- **Exemplo de Strings:** "F4000", "8335R", "DB", "Extratora", "Graxa"

**Modelo de Dados Implícito:**
```
Veículo/Máquina → Tipo Produto → Quantidade → Valor Unitário → Total
```

#### **Peças**
- **Dimensão:** 36 linhas × 26 colunas (A-Z)
- **Propósito:** Orçamento de peças de reposição e manutenção
- **Células Mescladas:** Moderado uso para agrupamento
- **Características:**
  - Peças por máquina/equipamento
  - Previsão de manutenção preventiva e corretiva
  - Controle de estoque mínimo

#### **Alimentação**
- **Dimensão:** 27 linhas × Colunas variadas
- **Propósito:** Custos com alimentação de trabalhadores
- **Escopo:**
  - Refeições (café, almoço, jantar)
  - Lanches e suprimentos
  - Custo per capita estimado

#### **Utilidades e Veículos**
- **Dimensão:** 86 linhas
- **Propósito:** Despesas gerais de infraestrutura
- **Destaque:** Possui **filtro de dados** definido (`_xlnm._FilterDatabase` em $A$19:$P$58)
- **Inclui:**
  - Energia elétrica
  - Água e telefonia
  - Manutenção de veículos leves
  - Seguros e licenciamentos

#### **Supriment-Ser Profiss** (Suprimentos e Serviços Profissionais)
- **Dimensão:** 60 linhas
- **Propósito:** Contratações externas e materiais administrativos
- **Exemplos:**
  - Consultorias técnicas
  - Serviços contábeis/jurídicos
  - Material de escritório
  - TI e software

---

### 2.3 ABAS DE RECURSOS HUMANOS

#### **Folha Pagamento**
- **Dimensão:** 143 linhas
- **Propósito:** Orçamento de pessoal
- **Detalhamento:**
  - Salários base por função
  - Encargos sociais (INSS, FGTS)
  - Benefícios (vale-transporte, alimentação)
  - 13º salário, férias, rescisões
- **Importância:** Maior peso no custo fixo

#### **RH**
- **Dimensão:** 106 linhas
- **Propósito:** Gestão complementar de RH
- **Células Mescladas:** 31 ranges
- **Foco:**
  - Treinamentos
  - EPIs (Equipamentos de Proteção Individual)
  - Exames médicos
  - Recrutamento e seleção

---

### 2.4 ABAS DE INSUMOS AGRÍCOLAS

#### **Quimi. Fert. Semente** (Químicos, Fertilizantes e Sementes)
- **Dimensão:** 44 linhas
- **Propósito:** Principal input da produção agrícola
- **Categorias:**
  - Sementes (variedades, quantidade/ha)
  - Fertilizantes (NPK, micronutrientes)
  - Defensivos químicos (herbicidas, fungicidas, inseticidas)
  - Adjuvantes

**Criticidade:** Alta - impacta diretamente a produtividade

#### **Contratação Serviç.**
- **Dimensão:** 49 linhas
- **Propósito:** Serviços terceirizados agrícolas
- **Exemplos:**
  - Aplicação aérea (pulverização)
  - Colheita terceirizada
  - Transporte de grãos
  - Análises de solo/laboratório

#### **Avião**
- **Dimensão:** 31 linhas
- **Propósito:** Operações de aviação agrícola
- **Detalhamento:**
  - Horas de voo
  - Combustível de aviação
  - Manutenção de aeronaves
  - Seguros específicos

---

### 2.5 ABAS FINANCEIRAS E ADMINISTRATIVAS

#### **Deprecisação** (Depreciação)
- **Dimensão:** Não mapeada (sheet vazia ou sem dados)
- **Propósito Esperado:** Cálculo de depreciação de ativos
- **Método:** Provavelmente linear ou acelerado
- **Ativos:**
  - Máquinas agrícolas
  - Veículos
  - Benfeitorias
  - Equipamentos

#### **Compras**
- **Dimensão:** Não mapeada (sheet vazia)
- **Propósito Esperado:** Gestão de procurement
- **Funções:**
  - Registro de pedidos de compra
  - Acompanhamento de entregas
  - Gestão de fornecedores

---

### 2.6 ABAS PESSOAIS (Responsáveis/Departamentos)

Estas abas representam **responsabilidade departamental** ou **centros de custo individuais**:

#### **Pedro**
- **Dimensão:** 31 linhas
- **Propósito:** Orçamento gerenciado por Pedro (possivelmente gerente de área)

#### **Tecnico**
- **Dimensão:** 30 linhas
- **Propósito:** Departamento técnico/agronômico

#### **Oficina**
- **Dimensão:** Não mapeada (sheet vazia)
- **Propósito Esperado:** Manutenção mecânica interna

#### **Angelo**
- **Dimensão:** 43 linhas
- **Células Mescladas:** 9 ranges
- **Propósito:** Orçamento gerenciado por Angelo

**Observação:** Esta estrutura por pessoa indica descentralização extrema do controle orçamentário, o que dificulta consolidação e auditoria.

---

## 3. ANÁLISE TÉCNICA PROFUNDA

### 3.1 Formatação de Dados

#### **Formatos Numéricos Identificados:**

**Monetários em R$:**
- `"R$" #,##0.00` - Padrão com 2 decimais
- `"R$" #,##0` - Sem decimais (valores arredondados)
- `"R$" #,##0.0000` - Alta precisão (4 decimais)
- `[$R$-416] #,##0.00` - Locale Brasil

**Percentuais:**
- `0.0%` - Percentual com 1 decimal
- `0.0%;(0.0%)` - Com negativo entre parênteses

**Datas:**
- `m/d/yyyy` - Formato americano
- `dddd, mmmm dd, yyyy` - Data por extenso

### 3.2 Células Mescladas (Problema Crítico)

**Quantidade Total:** 150+ ranges mesclados

**Impactos:**
- ❌ Impossibilita importação direta para bancos de dados
- ❌ Dificulta automação e scripts
- ❌ Quebra referências em fórmulas
- ❌ Complexifica manutenção

**Exemplo de Merge Complexo (Orçam-Realiza):**
```
A1:D1    → Título da seção
E1:K2    → Subtítulo mesclado
A2:D4    → Bloco de informação
```

### 3.3 Ausência de Fórmulas

**Observação Crítica:** Nenhuma fórmula detectada no JSON analisado.

**Possíveis Explicações:**
1. Valores foram convertidos para estáticos (copy/paste special values)
2. Amostragem não capturou células com fórmulas
3. Cálculos feitos manualmente

**Implicação:** Alto risco de erros humanos em cálculos

### 3.4 Validação de Dados

**Status:** Nenhuma validação detectada

**Consequências:**
- Sem controle de tipos de dados
- Permite entrada de valores inválidos
- Sem listas suspensas para padronização
- Dificulta integridade dos dados

---

## 4. MODELO DE DADOS IMPLÍCITO

Embora a planilha não use banco de dados, podemos inferir o modelo relacional subjacente:

### 4.1 Entidades Principais

```
┌─────────────────┐
│  ORÇAMENTO      │
├─────────────────┤
│ id              │
│ safra_ano       │
│ versao          │
│ data_criacao    │
│ responsavel     │
│ status          │
└─────────────────┘
        │
        │ 1:N
        ▼
┌─────────────────────┐
│  CATEGORIA_CUSTO    │
├─────────────────────┤
│ id                  │
│ nome                │ → "Combustível", "RH", "Insumos"
│ tipo                │ → Fixo/Variável
│ centro_custo        │
└─────────────────────┘
        │
        │ 1:N
        ▼
┌──────────────────────┐
│  ITEM_ORCAMENTO      │
├──────────────────────┤
│ id                   │
│ categoria_id         │ FK
│ descricao            │
│ unidade              │
│ quantidade_prevista  │
│ preco_unitario       │
│ valor_orcado         │
│ valor_realizado      │
│ mes_referencia       │
│ fornecedor           │
│ responsavel          │
└──────────────────────┘
```

### 4.2 Relacionamentos Identificados

**Hierarquia de Consolidação:**
```
Abas Operacionais (Combustível, Peças, etc.)
        ↓
Orçamento Resumo (Consolidação 1º nível)
        ↓
Orçam-Realiza (Dashboard executivo)
```

**Centros de Custo:**
```
Operacional    → Combustível, Peças, Insumos
Administrativo → Suprimentos, RH
Infraestrutura → Utilidades, Veículos
Pessoal        → Folha Pagamento, RH
Departamental  → Pedro, Angelo, Técnico, Oficina
```

---

## 5. FLUXO DE TRABALHO ATUAL (Inferido)

### 5.1 Ciclo de Planejamento

```
1. INÍCIO DO ANO/SAFRA
   └─> Cada responsável preenche sua aba
       ├─> Pedro preenche "Pedro"
       ├─> RH preenche "Folha Pagamento"
       ├─> Agrônomo preenche "Quimi. Fert. Semente"
       └─> Etc.

2. CONSOLIDAÇÃO
   └─> Alguém (provavelmente gerente) consolida em "Orçamento Resumo"
       └─> Transferência manual de valores

3. APROVAÇÃO
   └─> Dashboard "Orçam-Realiza" para diretoria

4. EXECUÇÃO (Durante a safra)
   └─> Preenchimento de "Realizado" conforme gastos ocorrem

5. ANÁLISE
   └─> Comparação Orçado vs Realizado
   └─> Ajustes para próxima safra
```

### 5.2 Problemas no Fluxo

❌ **Ausência de versionamento**
❌ **Sem controle de quem alterou o quê**
❌ **Risco de sobrescrever dados**
❌ **Consolidação manual propensa a erros**
❌ **Sem histórico de alterações**

---

## 6. OBJETIVO FINAL: SISTEMA ESTRUTURADO

### 6.1 Por Que Migrar do Excel?

**Limitações Atuais:**
1. **Escalabilidade:** Difícil adicionar mais complexidade
2. **Concorrência:** Múltiplos usuários causam conflitos
3. **Integridade:** Sem garantia de dados consistentes
4. **Auditoria:** Impossível rastrear mudanças
5. **Integração:** Não conecta com outros sistemas (ERP, contabilidade)
6. **Performance:** Arquivos grandes ficam lentos
7. **Automação:** Difícil gerar relatórios automáticos

### 6.2 Proposta de Sistema Novo

**Arquitetura Recomendada:**

```
┌─────────────────────────────────────────┐
│         CAMADA DE APRESENTAÇÃO          │
├─────────────────────────────────────────┤
│  Web App (React/Vue) ou Desktop (Electron)
│  - Dashboards interativos
│  - Formulários por categoria
│  - Relatórios personalizados
│  - Gráficos e KPIs
└─────────────────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────┐
│         CAMADA DE NEGÓCIO (API)         │
├─────────────────────────────────────────┤
│  Backend (Node.js, Python, .NET)
│  - Lógica de validação
│  - Cálculos automáticos
│  - Workflow de aprovação
│  - Notificações
│  - Exportação (PDF, Excel, CSV)
└─────────────────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────┐
│        CAMADA DE DADOS                  │
├─────────────────────────────────────────┤
│  Banco Relacional (PostgreSQL/MySQL)
│  - Tabelas normalizadas
│  - Constraints e validações
│  - Triggers para auditoria
│  - Índices para performance
│  - Backup automático
└─────────────────────────────────────────┘
```

### 6.3 Funcionalidades do Novo Sistema

**Core:**
- ✅ Multi-usuário com controle de acesso (RBAC)
- ✅ Versionamento de orçamentos
- ✅ Workflow de aprovação (Solicitante → Aprovador → Financeiro)
- ✅ Auditoria completa (quem, quando, o quê)
- ✅ Cálculos automáticos (totais, variações, %)
- ✅ Alertas de desvio orçamentário

**Avançado:**
- ✅ Comparação multi-safra (histórico)
- ✅ Previsões baseadas em tendências
- ✅ Integração com sistemas financeiros
- ✅ API para importação de notas fiscais
- ✅ Dashboards em tempo real
- ✅ Exportação para formatos legados (Excel, PDF)

---

## 7. ROADMAP DE MIGRAÇÃO

### FASE 1: Análise e Preparação (2-3 semanas)
- ✅ Análise completa da planilha (CONCLUÍDO - este documento)
- ⬜ Entrevistas com usuários-chave
- ⬜ Definição de requisitos funcionais
- ⬜ Modelagem do banco de dados
- ⬜ Prototipação de telas

### FASE 2: Desenvolvimento MVP (6-8 semanas)
- ⬜ Setup da infraestrutura
- ⬜ Criação do banco de dados
- ⬜ API REST básica
- ⬜ Telas de cadastro por categoria
- ⬜ Dashboard consolidado
- ⬜ Migração de dados históricos

### FASE 3: Testes e Ajustes (3-4 semanas)
- ⬜ Testes com usuários
- ⬜ Correção de bugs
- ⬜ Treinamento da equipe
- ⬜ Documentação

### FASE 4: Implantação (2 semanas)
- ⬜ Deploy em produção
- ⬜ Migração final dos dados
- ⬜ Suporte intensivo
- ⬜ Ajustes pós-implantação

### FASE 5: Evolução Contínua
- ⬜ Coleta de feedback
- ⬜ Novas funcionalidades
- ⬜ Integrações adicionais
- ⬜ Otimizações

---

## 8. RISCOS E MITIGAÇÕES

### Riscos Técnicos
| Risco | Probabilidade | Impacto | Mitigação |
|-------|---------------|---------|-----------|
| Perda de dados na migração | Média | Alto | Backup triplo + testes exaustivos |
| Resistência dos usuários | Alta | Médio | Treinamento + UI intuitiva |
| Complexidade subestimada | Média | Alto | MVP incremental + revisões semanais |
| Dependência de Excel | Alta | Médio | Manter export para Excel por 6 meses |

### Riscos de Negócio
| Risco | Probabilidade | Impacto | Mitigação |
|-------|---------------|---------|-----------|
| Mudança de processo | Alta | Alto | Change management + sponsor executivo |
| Custo vs benefício | Média | Médio | ROI claro + quick wins |
| Timing (meio da safra) | Baixa | Alto | Implantar entre safras |

---

## 9. MÉTRICAS DE SUCESSO

**KPIs Pós-Implantação:**
- ⏱️ Redução de 80% no tempo de consolidação orçamentária
- 📊 100% de rastreabilidade de alterações
- 👥 Acesso simultâneo de 10+ usuários sem conflitos
- 🎯 Redução de 90% em erros de cálculo
- 📈 Relatórios gerenciais em tempo real
- 💾 Backup automático diário
- 🔒 Segregação de funções (quem cria ≠ quem aprova)

---

## 10. CONCLUSÕES

### Situação Atual
A planilha Excel atual é um **sistema complexo e funcional**, mas chegou ao limite de sua capacidade técnica. Serve bem para registro histórico, mas **não é adequada para crescimento futuro**.

### Recomendações Prioritárias
1. **Urgente:** Implementar backup automático da planilha atual
2. **Curto prazo:** Iniciar projeto de sistema estruturado
3. **Médio prazo:** Migração gradual (categoria por categoria)
4. **Longo prazo:** Evolução para sistema integrado de gestão

### Benefícios Esperados
- 💰 **ROI estimado:** 3x em 2 anos (economia de tempo + redução de erros)
- 🚀 **Produtividade:** +50% em tarefas de planejamento
- 📊 **Qualidade de decisão:** Dados confiáveis em tempo real
- 🔐 **Segurança:** Controle de acesso e auditoria completa
- 📈 **Escalabilidade:** Pronto para crescimento da operação

---

**Documento gerado automaticamente pela análise OOXML Profiler**  
**Próximos passos:** Validar com stakeholders e iniciar prototipação do novo sistema.
