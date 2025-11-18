# 🌾 Sistema ERP Agrícola - Agroinvest

## 📋 Visão Geral

Transformação digital do sistema de gestão orçamentária da **Agroinvest Ltda** - empresa agrícola que opera 2.280 hectares (900 ha soja + 1.380 ha milho) com faturamento estimado de R$ 23 milhões anuais.

### Problema Atual
- Planilha Excel complexa com 18 abas interconectadas
- 2.289 fórmulas desprotegidas e 523 células mescladas
- Risco operacional e sem controle de versão
- Processos manuais e vulneráveis

### Solução Proposta
Sistema ERP completo com **ROI estimado de 359% em 3 anos** e **payback de 7,8 meses**.

---

## 🚀 Arquitetura do Projeto

### Stack Tecnológico
- **Backend:** Node.js + TypeScript + Express
- **Frontend:** Next.js 14 + React + TailwindCSS
- **Banco de Dados:** PostgreSQL + Prisma ORM
- **Infraestrutura:** Docker + GitHub Actions
- **Mobile:** PWA (Progressive Web App)

### Estrutura do Monorepo
```
├── backend/          # API RESTful
├── frontend/         # Interface web
├── shared/          # Tipos e utilitários comuns
├── docs/            # Documentação
├── docker/          # Configurações Docker
└── plan.yaml        # Plano de desenvolvimento detalhado
```

---

## 📊 Plano de Desenvolvimento

### Status Atual: **Planning Phase** ✅
- [x] Análise completa dos dados existentes
- [x] Extração e validação de 18 abas da planilha
- [x] Identificação de oportunidades de negócio
- [x] Definição de arquitetura e tecnologia
- [x] Plano detalhado em checkpoints sequenciais

### Roadmap Estimado: **8 semanas para MVP**

#### Fase 1: Fundação (Semanas 1-2)
- Setup do projeto e configurações
- Schema de banco de dados
- API base com autenticação

#### Fase 2: Core Features (Semanas 3-5)
- Interface principal (dashboard)
- Migração de dados da planilha
- Módulo de orçamento vs realizado

#### Fase 3: Business Modules (Semanas 6-8)
- Gestão de insumos
- Recursos humanos
- Manutenção de equipamentos

---

## 💡 Insights de Negócio

### Métricas da Operação
- **Área Total:** 2.280 hectares cultivados
- **Equipe:** 20+ funcionários permanentes
- **Ativos:** R$ 12,3 milhões em maquinário
- **Margem Estimada:** 64% (excelente para setor)

### Centros de Custo Principais
1. **Insumos Químicos:** R$ 6,27M (65% do orçamento)
2. **Folha de Pagamento:** R$ 1,11M anual
3. **Depreciação:** R$ 514K/ano
4. **Combustíveis:** ~R$ 150K/ano

### Oportunidades Identificadas
- **15.000 ha** em aplicação química (prestação de serviços)
- **Expansão de soja** 151% (358 ha → 900 ha)
- **Eficiência operacional** via digitalização
- **Sustentabilidade** com energia solar e irrigação

---

## 🎯 Objetivos do Sistema

### Imediatos (MVP)
- ✅ Substituir planilha Excel por sistema digital
- ✅ Controle orçamento vs realizado em tempo real
- ✅ Automação de relatórios e dashboards
- ✅ Segurança e backup de dados

### Estratégicos
- 🎯 Agricultura de precisão com rastreamento talhão
- 🎯 Integração IoT (sensores, GPS)
- 🎯 BI preditivo para otimização de custos
- 🎯 Escalabilidade para outras fazendas

---

## 📁 Documentação

### Plano Detalhado
- **`docs/plan.yaml`** - Plano completo com checkpoints sequenciais
- **23 checkpoints** definidos e priorizados
- **240 horas** estimadas de desenvolvimento
- **Dependencies** mapeadas para execução incremental

### Análise de Dados
- Extração completa de 18 abas (29.328 células)
- Identificação de 20 funcionários e estruturas salariais
- Mapeamento de frotas e equipamentos
- Análise de custos e margens por cultura

---

## 🛠️ Como Usar

### Para Desenvolvedores

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/Carroll-Brasil/orcamentosafra.git
   cd orcamentosafra
   ```

2. **Siga o plano de desenvolvimento:**
   ```bash
   # Verificar plano detalhado
   cat docs/plan.yaml

   # Executar checkpoint 001 (Setup do projeto)
   # Verificar acceptance criteria no plan.yaml
   ```

3. **Setup do ambiente:**
   ```bash
   # Instalar dependências
   npm install

   # Iniciar ambiente de desenvolvimento
   docker-compose up -d
   npm run dev
   ```

### Para Stakeholders

1. **Revisar plano completo:** `docs/plan.yaml`
2. **Acompanhar progresso:** Verificar checkpoints concluídos
3. **Validar features:** Testar acceptance criteria de cada módulo
4. **Feedback:** Contribuir com ajustes nos requisitos

---

## 📈 ROI e Benefícios Esperados

### Retorno Financeiro
- **Investimento:** R$ 490K em 18 meses
- **Economia Anual:** R$ 750K
- **Payback:** 7,8 meses
- **ROI 3 anos:** 359%

### Benefícios Operacionais
- ⚡ **Decisões baseadas em dados** em tempo real
- 🛡️ **Segurança** dos dados orçamentários
- 📱 **Acesso mobile** para equipe de campo
- 📊 **Automatização** de relatórios e análises
- 🔄 **Escalabilidade** para crescimento futuro

---

## 🤝 Como Contribuir

### Processo de Desenvolvimento
1. **Fazer fork** do repositório
2. **Criar branch** para feature específica
3. **Executar checkpoint** conforme plan.yaml
4. **Validar acceptance criteria**
5. **Submeter pull request** com descrição

### Orquestração Autônoma
O plano YAML foi desenhado para ser executado por sistemas autônomos:
- **Checkpoints sequenciais** com dependências claras
- **Acceptance criteria** mensuráveis
- **Estimativas realistas** de tempo
- **Qualidade garantida** via validações

---

## 📞 Contato e Informações

- **Repositório:** https://github.com/Carroll-Brasil/orcamentosafra
- **Documentação:** `docs/plan.yaml`
- **Status:** Em planejamento → Pronto para desenvolvimento
- **Timeline:** 8 semanas para MVP funcional

---

*Este projeto representa a transformação digital de uma operação agrícola tradicional em referência de gestão baseada em dados. 🌱*