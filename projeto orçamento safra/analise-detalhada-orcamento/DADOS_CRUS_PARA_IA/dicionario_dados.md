# 📚 DICIONÁRIO DE DADOS - Agroinvest Ltda

## 📋 ESTRUTURA GERAL

### Tabela de Abas e Propósitos

| Nome da Aba | Propósito | Principal Métrica | Status |
|-------------|-----------|-------------------|---------|
| Orçam-Realiza | Dashboard Principal | Comparação Orçado vs Real | Dashboard |
| Orçamento Resumo | Consolidação Executiva | Visão por categoria | Relatório |
| Combust. Lubrif | Controle de Combustíveis | Consumo por veículo | Operacional |
| peças | Manutenção de Máquinas | Peças e serviços | Operacional |
| Alimentação | Cantina/Refeitório | Custos alimentação | RH/Admin |
| Utilidades e Veiculos | Custos Administrativos | Água, luz, telefone | Admin |
| Supriment-Ser Profiss | TI e Consultoria | Serviços profissionais | Admin |
| Folha pagamento | RH e Encargos | Salários e benefícios | RH |
| Quimi. Fert. Semente | Insumos Agrícolas | Sementes, químicos | Produção |
| Contratação serviç | Serviços Terceiros | Aviação, consultoria | Operacional |
| Avião | Pulverização Aérea | Operações aéreas | Operacional |
| Deprecisação | Ativos Fixos | Controle patrimonial | Financeiro |
| Compras | Procurement | Aquisições | Admin |
| Pedro | Orçamento Setor Pedro | Custos específicos | Departamento |
| RH | Gestão de Pessoal | Treinamentos, EPIs | RH |
| Tecnico | Orçamento Técnico | Agronomia, consultoria | Técnico |
| Oficina | Manutenção Mecânica | Serviços oficina | Operacional |
| Angelo | Orçamento Setor Angelo | Custos específicos | Departamento |

---

## 👥 PESSOAS E CARGOS

### Hierarquia Identificada

#### Nível Estratégico
- **Romerio** - Gerente Geral (R$ 15.000)
  - Responsabilidade: Gestão geral da operação
  - Indicadores: Maior salário, nome em abas orçamentárias

#### Gerência de Setor
- **Angelo** - Gerente Setor Angelo (R$ 4.254,95)
  - Responsabilidade: Gestão específica do setor Angelo
  - Aba orçamentária própria: "Angelo"

- **Pedro** - Gerente Setor Pedro (R$ 1.321,00)
  - Responsabilidade: Gestão específica do setor Pedro
  - Aba orçamentária própria: "Pedro"

#### Equipe Técnica
- **Marcos Magalhães** - Técnico Agrícola (R$ 3.300 + insalubridade)
- **Joelson** - Técnico Agrícola (R$ 3.500 + insalubridade)
- **Francidalva** - Administrativo (R$ 2.500)

#### Equipe de Campo
- **Paulo Vitor** - Operador Plantio/TS (R$ 3.700 + insalubridade)
- **Raimundo** - Operador (R$ 2.200)
- **Marcos Santana** - Operador (R$ 4.000 + insalubridade)
- **Wanderson** - Operador (R$ 6.500 + insalubridade)
- **Bruno** - Operador (R$ 3.700 + insalubridade)

---

## 🚛 FROTA E EQUIPAMENTOS

### Veículos Leves
| Modelo | Identificação | Uso Principal | Consumo (L/safra) |
|--------|---------------|----------------|------------------|
| F4000 | Melosa | Transporte geral | 3.000 |
| F4000 | Aplicação | Aplicação insumos | 3.000 |
| S10 | Schu | Uso específico | 2.400 |
| S10 | Romerio | Uso intensivo | 5.500 |
| Pá Carregadeira | - | Carga/Descarga | 4.000 |
| JD5403 | Trator | Operações agrícolas | 1.000 |
| Ford Cargo | - | Transporte pesado | 3.000 |
| TS | - | Leve/curto | 100 |

### Máquinas Agrícolas (Inferidas)
- **Colheitadeiras** (para soja e milho)
- **Tratores** (além do JD5403)
- **Pulverizadores** (terrestres)
- **Plantadeiras/Adubadeiras**
- **Avião Agrícola** (aba específica)

---

## 🌾 CULTURAS E VARIEDADES

### Soja
- **Variedade Principal:** Intacta
- **Tecnologia:** Roundup Ready (RR)
- **Área Safra 25-26:** 900 hectares
- **Custo Sementes:** $83,57 USD/ha

### Milho
- **Variedade Principal:** Leptra
- **Tecnologia:** Trplice (herbicida + inseticida + tolerância)
- **Área Safra 25-26:** 1.380 hectares
- **Custo Sementes:** $187,00 USD/ha

### Outras Variedades (Orçadas mas não utilizadas)
- Algodão WS
- Algodão GLT
- Algodão B2RRF
- Algodão RR

---

## 💰 ESTRUTURA FINANCEIRA

### Centros de Custo Principal

#### 1. Insumos Agrícolas
- **Sementes:** Custo por hectare e variedade
- **Fertilizantes:** Adubação NPK e corretivos
- **Defensivos:** Herbicidas, inseticidas, fungicidas
- **Unidades:** USD/ha para sementes, BRL total para outros

#### 2. Operações Mecanizadas
- **Combustível:** Diesel por equipamento/atividade
- **Lubrificantes:** Óleos específicos por equipamento
- **Manutenção:** Peças e mão de obra oficina

#### 3. Recursos Humanos
- **Salários:** Valor base por funcionário
- **Encargos:** INSS, FGTS, 13º, férias
- **Benefícios:** Vale transporte, alimentação
- **Adicionais:** Insalubridade, periculosidade, horas extras

#### 4. Infraestrutura
- **Depreciação:** Método linear, vida útil definida
- **Alimentação:** Cantina (86 produtos cadastrados)
- **Utilidades:** Água, energia elétrica, telefone
- **Serviços:** TI, consultoria, contabilidade

### Moedas e Conversão
- **Real (BRL):** Principal moeda operacional
- **Dólar (USD):** Usado para insumos importados (sementes)
- **Taxa de Câmbio:** Não explicitada na planilha

---

## 📊 UNIDADES DE MEDIDA

### Área
- **Hectare (ha):** Unidade padrão para área agrícola
- **Kilômetro (km):** Distâncias e deslocamentos
- **Metro (m):** Dimensões lineares

### Volume
- **Litro (L):** Combustíveis, óleos, lubrificantes
- **Quilograma (kg):** Massa de insumos sólidos
- **Unidade (un):** Itens individuais (botijão, pacote)

### Tempo
- **Hora (h):** Duração de operações
- **Mês:** Período orçamentário
- **Safra:** Ciclo anual (out-set)

### Dinheiro
- **Real (R$):** Moeda principal brasileira
- **Dólar ($):** Moeda americana para importados

---

## 📝 INDICADORES E MÉTRICAS

### Indicadores de Produção
- **Produtividade:** sacas/hectare
- **Área Cultivada:** hectares por cultura
- **Custo/ha:** por categoria de insumo
- **Rendimento:** horas/atividade

### Indicadores Financeiros
- **Orçado vs Realizado:** comparação mensal
- **Variação %:** desvio orçamentário
- **Participação %:** peso no custo total
- **Custo Unitário:** R$ por unidade de medida

### Indicadores Operacionais
- **Consumo Combustível:** litros/atividade
- **Horas Máquina:** por equipamento/atividade
- **Produtividade Equipe:** funcionários/ha
- **Disponibilidade:** dias úteis vs parados

---

## 🏷️ NOMENCLATURAS E PADRÕES

### Padrões Identificados
- **Nomes Funcionários:** Nome completo sem padronização
- **Equipamentos:** Modelo + identificação única
- **Produtos:** Descrição comercial completa
- **Fornecedores:** Nome fantasia (quando disponível)

### Inconsistências Detectadas
- **Unidades:** ha vs KM vs hora misturadas
- **Nomes:** mesmo conceito com grafias diferentes
- **Códigos:** ausência de códigos padronizados
- **Categorias:** subclassificação inconsistente

---

## 🔗 RELACIONAMENTOS ENTRE DADOS

### Relações Principais
1. **Funcionário ↔ Departamento:** Cada pessoa associada a um setor
2. **Equipamento ↔ Atividade:** Cada máquina a uma ou mais operações
3. **Insumo ↔ Cultura:** Produtos específicos por tipo de plantio
4. **Custo ↔ Centro:** Cada despesa a um centro de custo

### Relações Transversais
1. **Tempo:** Todas as abas com períodos mensais
2. **Moeda:** Conversão BRL/USD quando necessário
3. **Responsabilidade:** Pessoas responsáveis por centros de custo
4. **Localização:** Áreas e talhões implícitos

---

## ⚠️ OBSERVAÇÕES CRÍTICAS

### Qualidade dos Dados
- **Completude:** 23,5% células preenchidas (aceitável)
- **Consistência:** Boa dentro de cada aba específica
- **Padronização:** Melhorias necessárias
- **Validação:** Ausente (opportunity para sistema novo)

### Riscos de Dados
1. **Células Mescladas:** 523 merges detectados
2. **Fórmulas Desprotegidas:** Risco de sobrescrita
3. **Nomes Inconsistentes:** Padronização necessária
4. **Códigos Ausentes:** Identificação única necessária

### Oportunidades de Melhoria
1. **Codificação:** ID único para cada entidade
2. **Padronização:** Nomenclatura consistente
3. **Validação:** Regras de integridade
4. **Hierarquia:** Estrutura organizacional clara
5. **Integração:** Relacionamentos explícitos

---

*Este dicionário serve como base para modelagem de dados do sistema digital, garantindo consistência e integridade das informações.*