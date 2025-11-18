#!/usr/bin/env python3
"""
OOXML Workbook Profiler

Analisa pacotes OOXML do Excel (pasta extraída de .xlsx) e gera:
- workbook_manifest.json: esquema completo com metadados
- WORKBOOK_SUMMARY.md: relatório detalhado em Markdown

Uso: python ooxml_profile.py --root /caminho/pasta_extraida --out ./saida
"""

import argparse
import csv
import itertools
import json
import logging
import re
import statistics
import textwrap
from collections import defaultdict, Counter
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple, Set
import xml.etree.ElementTree as ET
import zipfile


class OOXMLLoader:
    """Carrega e faz parse dos arquivos principais do OOXML"""
    
    def __init__(self, root_path: Path):
        self.root_path = root_path
        self.logger = logging.getLogger(__name__)
        
    def load_workbook_xml(self) -> Dict[str, Any]:
        """Parse de xl/workbook.xml"""
        workbook_path = self.root_path / "xl" / "workbook.xml"
        if not workbook_path.exists():
            self.logger.warning("workbook.xml não encontrado")
            return {}
            
        try:
            tree = ET.parse(workbook_path)
            root = tree.getroot()
            
            # Namespaces
            ns = {'main': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
            
            result = {
                'sheets': [],
                'definedNames': [],
                'app_name': 'Excel'
            }
            
            # Parse sheets
            sheets_elem = root.find('.//main:sheets', ns)
            if sheets_elem is not None:
                for sheet in sheets_elem.findall('main:sheet', ns):
                    result['sheets'].append({
                        'name': sheet.get('name', ''),
                        'sheetId': int(sheet.get('sheetId', 0)),
                        'rid': sheet.get('r:id', '')
                    })
            
            # Parse defined names
            defined_names = root.find('.//main:definedNames', ns)
            if defined_names is not None:
                for defined_name in defined_names.findall('main:definedName', ns):
                    name_data = {
                        'name': defined_name.get('name', ''),
                        'refersTo': (defined_name.text or '').strip(),
                        'localSheetId': None
                    }
                    if defined_name.get('localSheetId'):
                        name_data['localSheetId'] = int(defined_name.get('localSheetId'))
                    result['definedNames'].append(name_data)
                    
            return result
            
        except Exception as e:
            self.logger.error(f"Erro ao parse workbook.xml: {e}")
            return {}
    
    def load_relationships(self) -> List[Dict[str, str]]:
        """Parse de xl/_rels/workbook.xml.rels"""
        rels_path = self.root_path / "xl" / "_rels" / "workbook.xml.rels"
        if not rels_path.exists():
            self.logger.warning("workbook.xml.rels não encontrado")
            return []
            
        try:
            tree = ET.parse(rels_path)
            root = tree.getroot()
            
            ns = {'rels': 'http://schemas.openxmlformats.org/package/2006/relationships'}
            
            relationships = []
            for rel in root.findall('.//rels:Relationship', ns):
                relationships.append({
                    'rid': rel.get('Id', ''),
                    'type': rel.get('Type', ''),
                    'target': rel.get('Target', '')
                })
                
            return relationships
            
        except Exception as e:
            self.logger.error(f"Erro ao parse relationships: {e}")
            return []
    
    def load_shared_strings(self) -> Dict[str, Any]:
        """Parse de xl/sharedStrings.xml"""
        ss_path = self.root_path / "xl" / "sharedStrings.xml"
        if not ss_path.exists():
            self.logger.info("sharedStrings.xml não encontrado")
            return {'strings': [], 'count': 0, 'uniqueCount': 0}
            
        try:
            strings = []
            tree = ET.parse(ss_path)
            root = tree.getroot()
            
            ns = {'main': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
            
            for si in root.findall('.//main:si', ns):
                text_parts = []
                for t in si.findall('.//main:t', ns):
                    if t.text:
                        text_parts.append(t.text)
                strings.append(''.join(text_parts))
            
            return {
                'strings': strings,
                'count': len(strings),
                'uniqueCount': len(strings)
            }
            
        except Exception as e:
            self.logger.error(f"Erro ao parse sharedStrings.xml: {e}")
            return {'strings': [], 'count': 0, 'uniqueCount': 0}
    
    def load_styles(self) -> Dict[str, Any]:
        """Parse de xl/styles.xml para formatos numéricos"""
        styles_path = self.root_path / "xl" / "styles.xml"
        if not styles_path.exists():
            self.logger.info("styles.xml não encontrado")
            return {'numFmts': {}, 'cellXfs': []}
            
        try:
            tree = ET.parse(styles_path)
            root = tree.getroot()
            
            ns = {'main': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
            
            # Parse numFmts
            numFmts = {}
            for numFmt in root.findall('.//main:numFmt', ns):
                numFmtId = int(numFmt.get('numFmtId', 0))
                formatCode = numFmt.get('formatCode', '')
                numFmts[numFmtId] = formatCode
            
            # Parse cellXfs
            cellXfs = []
            for xf in root.findall('.//main:xf', ns):
                xf_data = {'xfId': int(xf.get('xfId', 0))}
                if xf.get('numFmtId'):
                    xf_data['numFmtId'] = int(xf.get('numFmtId'))
                cellXfs.append(xf_data)
            
            return {
                'numFmts': numFmts,
                'cellXfs': cellXfs
            }
            
        except Exception as e:
            self.logger.error(f"Erro ao parse styles.xml: {e}")
            return {'numFmts': {}, 'cellXfs': []}


class SheetProfiler:
    """Analisa worksheets usando iterparse para eficiência"""
    
    def __init__(self, sheet_path: Path, shared_strings: List[str], styles: Dict[str, Any], sample_rows: int = 5000):
        self.sheet_path = sheet_path
        self.shared_strings = shared_strings
        self.styles = styles
        self.sample_rows = sample_rows
        self.logger = logging.getLogger(__name__)
        
        # Formatos de data/hora comuns
        self.date_formats = {
            'm/d/yy', 'mm/dd/yy', 'd/m/yy', 'dd/mm/yy',
            'm/d/yyyy', 'mm/dd/yyyy', 'd/m/yyyy', 'dd/mm/yyyy',
            'dd-mm-yy', 'dd-mm-yyyy', 'mm-dd-yy', 'mm-dd-yyyy',
            'yyyy-mm-dd', 'yy-mm-dd', 'hh:mm', 'hh:mm:ss',
            'm/d/yy h:mm', 'mm/dd/yyyy hh:mm:ss'
        }
        
    def is_date_format(self, formatCode: str) -> bool:
        """Verifica se formato é de data/hora"""
        if not formatCode:
            return False
        
        # Remove caracteres especiais e converte para minúsculo
        clean_format = re.sub(r'[^a-z/\\-:]', '', formatCode.lower())
        
        return any(date_pat in clean_format for date_pat in ['d', 'm', 'y', 'h', 's']) and len(clean_format) > 2
    
    def excel_date_to_iso(self, excel_date: float) -> str:
        """Converte data serial do Excel para ISO 8601"""
        try:
            # Base do Excel: 1 de janeiro de 1900
            base_date = datetime(1899, 12, 30)
            converted = base_date + datetime.timedelta(days=excel_date)
            return converted.isoformat()
        except:
            return str(excel_date)
    
    def column_index_from_address(self, address: str) -> str:
        """Extrai letra da coluna do endereço (ex: 'A1' -> 'A')"""
        match = re.match(r'([A-Z]+)', address.upper())
        return match.group(1) if match else ''
    
    def profile_sheet(self) -> Dict[str, Any]:
        """Perfil completo da worksheet"""
        if not self.sheet_path.exists():
            return {}
            
        start_time = datetime.now()
        
        profile = {
            'dimension': {'ref': '', 'rows': 0, 'cols': 0},
            'columns': {},
            'formulas': {'count': 0, 'examples': []},
            'merges': [],
            'conditionalFormatting': [],
            'hyperlinks': [],
            'validations': []
        }
        
        try:
            # Usar iterparse para streaming
            context = ET.iterparse(str(self.sheet_path), events=('start', 'end'))
            context = iter(context)
            
            # Variáveis de controle
            current_row = None
            current_cell = None
            row_count = 0
            sample_interval = max(1, self.sample_rows // 100)  # Amostrar 1% das linhas
            
            for event, elem in context:
                if event == 'start':
                    if elem.tag.endswith('dimension'):
                        ref = elem.get('ref', '')
                        if ref:
                            profile['dimension']['ref'] = ref
                            # Estimar dimensões
                            if ':' in ref:
                                start, end = ref.split(':')
                                profile['dimension']['cols'] = self.column_index_from_address(end)
                                profile['dimension']['rows'] = int(re.search(r'\d+', end).group())
                    
                    elif elem.tag.endswith('row'):
                        current_row = elem
                        row_count += 1
                        
                    elif elem.tag.endswith('c'):
                        current_cell = elem
                        addr = elem.get('r', '')
                        if addr:
                            col = self.column_index_from_address(addr)
                            
                            # Inicializar coluna se não existir
                            if col not in profile['columns']:
                                profile['columns'][col] = {
                                    'address': col,
                                    'header_guess': '',
                                    'inferred_type': 'unknown',
                                    'nulls': 0,
                                    'unique': set(),
                                    'samples': [],
                                    'num_stats': {},
                                    'has_formula': False,
                                    'validations': []
                                }
                            
                            # Amostragem estratégica
                            if row_count % sample_interval == 0 or row_count <= 10:
                                self._process_cell(elem, profile['columns'][col])
                
                elif event == 'end':
                    if elem.tag.endswith('mergeCell'):
                        ref = elem.get('ref', '')
                        if ref:
                            profile['merges'].append({'ref': ref})
                    
                    elif elem.tag.endswith('dataValidation'):
                        self._process_validation(elem, profile)
                    
                    elif elem.tag.endswith('conditionalFormatting'):
                        sqref = elem.get('sqref', '')
                        if sqref:
                            rules = []
                            for rule in elem.findall('.//*'):
                                if rule.tag and 'rule' in rule.tag.lower():
                                    rule_text = ET.tostring(rule, encoding='unicode')
                                    rules.append(rule_text[:100])  # Limitar tamanho
                            
                            profile['conditionalFormatting'].append({
                                'sqref': sqref,
                                'rule': '; '.join(rules)
                            })
                    
                    elif elem.tag.endswith('hyperlink'):
                        ref = elem.get('ref', '')
                        rid = elem.get('r:id', '')
                        if ref and rid:
                            profile['hyperlinks'].append({
                                'ref': ref,
                                'r:id': rid,
                                'target': f'hyperlink_{rid}'
                            })
                    
                    # Limpar elementos processados
                    elem.clear()
            
            # Finalizar perfil das colunas
            for col_data in profile['columns'].values():
                self._finalize_column_stats(col_data)
            
            # Atualizar dimensão real se não encontrada
            if profile['dimension']['rows'] == 0:
                profile['dimension']['rows'] = row_count
                if profile['columns']:
                    profile['dimension']['cols'] = len(profile['columns'])
            
            duration = (datetime.now() - start_time).total_seconds()
            self.logger.info(f"Sheet {self.sheet_path.name}: {row_count} linhas em {duration:.2f}s")
            
            return profile
            
        except Exception as e:
            self.logger.error(f"Erro ao profile sheet {self.sheet_path}: {e}")
            return {}
    
    def _process_cell(self, cell_elem, col_data: Dict[str, Any]):
        """Processa célula individual"""
        cell_type = cell_elem.get('t', '')  # s=shared string, n=number, str=inline string, b=bool, e=error
        
        value_elem = cell_elem.find('.//v')
        formula_elem = cell_elem.find('.//f')
        
        # Processar fórmula
        if formula_elem is not None and formula_elem.text:
            col_data['has_formula'] = True
        
        # Processar valor
        if value_elem is not None and value_elem.text:
            value = value_elem.text.strip()
            
            if not value:
                col_data['nulls'] += 1
                return
            
            # Converter valor baseado no tipo
            if cell_type == 's':  # Shared string
                try:
                    idx = int(value)
                    if idx < len(self.shared_strings):
                        value = self.shared_strings[idx]
                except:
                    pass
            elif cell_type == 'b':  # Boolean
                value = '1' if value == '1' else '0'
            elif cell_type == 'n' or cell_type == '':  # Number
                try:
                    num_value = float(value)
                    
                    # Verificar se é data baseado no estilo
                    style_idx = cell_elem.get('s')
                    if style_idx and self.styles['cellXfs']:
                        try:
                            xf = self.styles['cellXfs'][int(style_idx)]
                            if 'numFmtId' in xf:
                                fmt_id = xf['numFmtId']
                                formatCode = self.styles['numFmts'].get(fmt_id, '')
                                if self.is_date_format(formatCode):
                                    # Converter para ISO apenas para amostras
                                    if len(col_data['samples']) < 20:
                                        value = self.excel_date_to_iso(num_value)
                                    col_data['inferred_type'] = 'date'
                                    col_data['unique'].add(value)
                                    col_data['samples'].append(value)
                                    return
                        except:
                            pass
                    
                    value = str(num_value)
                    
                except ValueError:
                    pass
            
            # Adicionar às estatísticas
            col_data['unique'].add(value)
            if len(col_data['samples']) < 20:
                col_data['samples'].append(value)
            
            # Inferir tipo se ainda não definido
            if col_data['inferred_type'] == 'unknown':
                col_data['inferred_type'] = self._infer_type(value)
        else:
            col_data['nulls'] += 1
    
    def _infer_type(self, value: str) -> str:
        """Infere tipo do valor"""
        if value.lower() in ['true', 'false', '1', '0']:
            return 'bool'
        
        # Tentar número
        try:
            float(value)
            return 'float'
        except ValueError:
            pass
        
        # Tentar inteiro
        try:
            int(value)
            return 'integer'
        except ValueError:
            pass
        
        # Verificar se parece data (ISO format)
        if re.match(r'\d{4}-\d{2}-\d{2}', value):
            return 'date'
        
        return 'string'
    
    def _finalize_column_stats(self, col_data: Dict[str, Any]):
        """Finaliza estatísticas da coluna"""
        # Converter sets para counts
        col_data['unique'] = len(col_data['unique'])
        
        # Calcular estatísticas numéricas se aplicável
        if col_data['inferred_type'] in ['integer', 'float'] and col_data['samples']:
            try:
                numbers = [float(x) for x in col_data['samples'] if self._is_number(x)]
                if numbers:
                    col_data['num_stats'] = {
                        'min': min(numbers),
                        'max': max(numbers),
                        'mean': statistics.mean(numbers)
                    }
            except:
                pass
        
        # Limitar amostras
        col_data['samples'] = col_data['samples'][:20]
    
    def _is_number(self, value: str) -> bool:
        """Verifica se string representa número"""
        try:
            float(value)
            return True
        except ValueError:
            return False
    
    def _process_validation(self, validation_elem, profile: Dict[str, Any]):
        """Processa validação de dados"""
        val_type = validation_elem.get('type', '')
        sqref = validation_elem.get('sqref', '')
        
        formula1 = validation_elem.find('.//formula1')
        formula_text = formula1.text if formula1 is not None and formula1.text else ''
        
        if sqref:
            validation = {
                'type': val_type,
                'sqref': sqref,
                'formula': formula_text
            }
            
            if validation_elem.get('allowBlank') == '1':
                validation['allowBlank'] = True
            
            profile['validations'].append(validation)


class ManifestBuilder:
    """Constrói o manifesto JSON final"""
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
    
    def build_manifest(self, workbook_data: Dict, relationships: List, shared_strings: Dict, 
                      styles: Dict, sheets_profiles: List[Dict], pivots: List) -> Dict[str, Any]:
        """Monta o manifesto completo"""
        
        manifest = {
            'workbook': {
                'app_name': workbook_data.get('app_name', 'Excel'),
                'sheets': workbook_data.get('sheets', []),
                'definedNames': workbook_data.get('definedNames', []),
                'relationships': relationships,
                'has_sharedStrings': len(shared_strings.get('strings', [])) > 0,
                'has_styles': len(styles.get('numFmts', {})) > 0
            },
            'styles': {
                'numFmts': [{'numFmtId': k, 'formatCode': v} for k, v in styles.get('numFmts', {}).items()],
                'cellXfs': styles.get('cellXfs', [])
            },
            'sharedStrings': {
                'count': shared_strings.get('count', 0),
                'uniqueCount': shared_strings.get('uniqueCount', 0),
                'examples': shared_strings.get('strings', [])[:10]
            },
            'sheets': sheets_profiles,
            'pivots': pivots,
            'notes': []
        }
        
        # Adicionar warnings
        if not manifest['workbook']['has_sharedStrings']:
            manifest['notes'].append('sharedStrings.xml não encontrado - valores textuais lidos diretamente')
        if not manifest['workbook']['has_styles']:
            manifest['notes'].append('styles.xml não encontrado - heurística de data desabilitada')
        
        return manifest


class MarkdownWriter:
    """Gera relatório Markdown a partir do manifesto JSON"""
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
    
    def generate_summary(self, manifest: Dict[str, Any]) -> str:
        """Gera WORKBOOK_SUMMARY.md"""
        
        md_lines = [
            "# Workbook Summary",
            "",
            f"**Gerado em:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            "",
            "## Visão Geral",
            ""
        ]
        
        workbook = manifest['workbook']
        
        # Estatísticas gerais
        md_lines.extend([
            f"- **Aplicação:** {workbook['app_name']}",
            f"- **Total de abas:** {len(workbook['sheets'])}",
            f"- **Nomes definidos:** {len(workbook['definedNames'])}",
            f"- **Strings compartilhadas:** {manifest['sharedStrings']['count']} ({manifest['sharedStrings']['uniqueCount']} únicas)",
            f"- **Pivot Tables:** {len(manifest['pivots'])}",
            f"- **Possui styles.xml:** {'Sim' if workbook['has_styles'] else 'Não'}",
            f"- **Possui sharedStrings.xml:** {'Sim' if workbook['has_sharedStrings'] else 'Não'}",
            ""
        ])
        
        # Tabela resumo por aba
        md_lines.extend([
            "## Resumo por Aba",
            "",
            "| Aba | Linhas | Colunas | Fórmulas | Merges | Validações | CF | Hyperlinks |",
            "|-----|--------|---------|-----------|--------|------------|----|------------|"
        ])
        
        for sheet in manifest['sheets']:
            dimension = sheet.get('dimension', {})
            rows = dimension.get('rows', 0)
            cols = len(dimension.get('cols', [])) if isinstance(dimension.get('cols'), list) else dimension.get('cols', 0)
            
            md_lines.append(
                f"| {sheet.get('name', 'N/A')} | {rows} | {cols} | "
                f"{sheet.get('formulas', {}).get('count', 0)} | "
                f"{len(sheet.get('merges', []))} | "
                f"{len(sheet.get('validations', []))} | "
                f"{len(sheet.get('conditionalFormatting', []))} | "
                f"{len(sheet.get('hyperlinks', []))} |"
            )
        
        md_lines.append("")
        
        # Detalhes por aba
        for i, sheet in enumerate(manifest['sheets']):
            md_lines.extend([
                f"## Aba: {sheet.get('name', f'Sheet{i+1}')}",
                "",
                f"**Caminho:** `{sheet.get('path', '')}`",
                f"**Dimensão:** {sheet.get('dimension', {}).get('ref', 'Desconhecida')}",
                ""
            ])
            
            # Dicionário de colunas
            if sheet.get('columns'):
                md_lines.extend([
                    "### Dicionário de Colunas",
                    "",
                    "| Coluna | Header (Guess) | Tipo | % Nulos | Únicos | Amostras | Stats | Fórmulas |",
                    "|--------|----------------|------|---------|--------|----------|-------|----------|"
                ])
                
                dimension = sheet.get('dimension', {})
                total_rows = dimension.get('rows', 1)
                
                for col_addr, col_data in sheet.get('columns', {}).items():
                    null_pct = (col_data.get('nulls', 0) / total_rows * 100) if total_rows > 0 else 0
                    
                    samples_str = ', '.join(str(s) for s in col_data.get('samples', [])[:3])
                    stats_str = ""
                    
                    if col_data.get('num_stats'):
                        stats = col_data['num_stats']
                        stats_str = f"min:{stats.get('min', 'N/A'):.2f}, max:{stats.get('max', 'N/A'):.2f}, mean:{stats.get('mean', 'N/A'):.2f}"
                    
                    md_lines.append(
                        f"| {col_addr} | {col_data.get('header_guess', '')} | "
                        f"{col_data.get('inferred_type', 'unknown')} | "
                        f"{null_pct:.1f}% | {col_data.get('unique', 0)} | "
                        f"{samples_str} | {stats_str} | "
                        f"{'Sim' if col_data.get('has_formula') else 'Não'} |"
                    )
                
                md_lines.append("")
            
            # Fórmulas
            formulas = sheet.get('formulas', {})
            if formulas.get('count', 0) > 0:
                md_lines.extend([
                    "### Fórmulas",
                    "",
                    f"**Total de fórmulas:** {formulas['count']}",
                    ""
                ])
                
                if formulas.get('examples'):
                    md_lines.append("**Exemplos:**")
                    for example in formulas['examples'][:5]:
                        md_lines.append(f"- `{example.get('cell', '')}`: `{example.get('formula', '')}`")
                    md_lines.append("")
            
            # Validações
            if sheet.get('validations'):
                md_lines.extend([
                    "### Validações de Dados",
                    ""
                ])
                
                for validation in sheet['validations'][:5]:
                    md_lines.append(
                        f"- **Tipo:** {validation.get('type', 'unknown')} | "
                        f"**Range:** `{validation.get('sqref', '')}` | "
                        f"**Fórmula:** `{validation.get('formula', '')}`"
                    )
                md_lines.append("")
            
            # Formatação condicional
            if sheet.get('conditionalFormatting'):
                md_lines.extend([
                    "### Formatação Condicional",
                    ""
                ])
                
                for cf in sheet['conditionalFormatting'][:3]:
                    md_lines.append(
                        f"- **Range:** `{cf.get('sqref', '')}` | "
                        f"**Regra:** `{cf.get('rule', '')[:100]}...`"
                    )
                md_lines.append("")
        
        # Nomes definidos
        if workbook.get('definedNames'):
            md_lines.extend([
                "## Nomes Definidos",
                "",
                "| Nome | Referência | Sheet Local |",
                "|------|------------|-------------|"
            ])
            
            for defined_name in workbook['definedNames']:
                sheet_id = defined_name.get('localSheetId', 'Global')
                md_lines.append(
                    f"| `{defined_name.get('name', '')}` | "
                    f"`{defined_name.get('refersTo', '')}` | "
                    f"{sheet_id} |"
                )
            
            md_lines.append("")
        
        # Pivot Tables
        if manifest.get('pivots'):
            md_lines.extend([
                "## Pivot Tables",
                ""
            ])
            
            for pivot in manifest['pivots']:
                md_lines.append(
                    f"- **Nome:** {pivot.get('name', 'N/A')} | "
                    f"**Fonte:** `{pivot.get('source', 'N/A')}` | "
                    f"**Caminho:** `{pivot.get('path', '')}`"
                )
            md_lines.append("")
        
        # Riscos e recomendações
        md_lines.extend([
            "## Análise de Qualidade",
            ""
        ])
        
        # Analisar potenciais problemas
        issues = []
        
        for sheet in manifest['sheets']:
            sheet_name = sheet.get('name', 'Unknown')
            
            # Colunas com muitos nulos
            for col_addr, col_data in sheet.get('columns', {}).items():
                dimension = sheet.get('dimension', {})
                total_rows = dimension.get('rows', 1)
                null_pct = (col_data.get('nulls', 0) / total_rows * 100) if total_rows > 0 else 0
                
                if null_pct > 50:
                    issues.append(f"**{sheet_name}!{col_addr}:** {null_pct:.1f}% de valores nulos")
            
            # Muitas fórmulas
            if sheet.get('formulas', {}).get('count', 0) > 1000:
                issues.append(f"**{sheet_name}:** {sheet['formulas']['count']} fórmulas (possível impacto de performance)")
        
        if issues:
            md_lines.append("### ⚠️ Pontos de Atenção")
            for issue in issues[:10]:
                md_lines.append(f"- {issue}")
            md_lines.append("")
        
        # Notas do parser
        if manifest.get('notes'):
            md_lines.extend([
                "## Notas do Processamento",
                ""
            ])
            for note in manifest['notes']:
                md_lines.append(f"- {note}")
            md_lines.append("")
        
        # Footer
        md_lines.extend([
            "---",
            f"*Relatório gerado por OOXML Profiler em {datetime.now().isoformat()}*"
        ])
        
        return '\n'.join(md_lines)


def find_pivot_tables(root_path: Path) -> List[Dict[str, str]]:
    """Encontra pivot tables e extrai metadados básicos"""
    pivots = []
    pivot_dir = root_path / "xl" / "pivotTables"
    
    if not pivot_dir.exists():
        return pivots
    
    for pivot_file in pivot_dir.glob("pivotTable*.xml"):
        try:
            tree = ET.parse(pivot_file)
            root = tree.getroot()
            
            ns = {'main': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
            
            # Tentar encontrar fonte
            cache_source = root.find('.//main:cacheSource', ns)
            source_ref = "Unknown"
            
            if cache_source is not None:
                worksheet_source = cache_source.find('.//main:worksheetSource', ns)
                if worksheet_source is not None:
                    ref = worksheet_source.get('ref', '')
                    sheet = worksheet_source.get('sheet', '')
                    if ref and sheet:
                        source_ref = f"{sheet}!{ref}"
            
            pivots.append({
                'name': pivot_file.stem,
                'path': f"xl/pivotTables/{pivot_file.name}",
                'source': source_ref
            })
            
        except Exception as e:
            logging.getLogger(__name__).warning(f"Erro ao ler pivot {pivot_file}: {e}")
    
    return pivots


def main():
    """Função principal"""
    parser = argparse.ArgumentParser(
        description="Analisa pacote OOXML do Excel e gera manifesto JSON e relatório Markdown"
    )
    
    parser.add_argument(
        '--root',
        type=str,
        required=True,
        help='Caminho para a pasta extraída do .xlsx'
    )
    
    parser.add_argument(
        '--out',
        type=str,
        default='./output',
        help='Diretório de saída (default: ./output)'
    )
    
    parser.add_argument(
        '--sample-rows',
        type=int,
        default=5000,
        help='Número de linhas para amostrar (default: 5000)'
    )
    
    parser.add_argument(
        '--distinct-per-col',
        type=int,
        default=20,
        help='Número máximo de exemplos distintos por coluna (default: 20)'
    )
    
    parser.add_argument(
        '--log-level',
        type=str,
        default='INFO',
        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR'],
        help='Nível de log (default: INFO)'
    )
    
    args = parser.parse_args()
    
    # Configurar logging
    logging.basicConfig(
        level=getattr(logging, args.log_level),
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    logger = logging.getLogger(__name__)
    
    # Validar diretório de entrada
    root_path = Path(args.root).resolve()
    if not root_path.exists():
        logger.error(f"Diretório não encontrado: {root_path}")
        return 1
    
    # Criar diretório de saída
    out_path = Path(args.out).resolve()
    out_path.mkdir(parents=True, exist_ok=True)
    
    logger.info(f"Iniciando análise de: {root_path}")
    logger.info(f"Saída será gerada em: {out_path}")
    
    try:
        # Inicializar componentes
        loader = OOXMLLoader(root_path)
        builder = ManifestBuilder()
        markdown_writer = MarkdownWriter()
        
        # Carregar dados básicos
        logger.info("Carregando workbook.xml e relacionamentos...")
        workbook_data = loader.load_workbook_xml()
        relationships = loader.load_relationships()
        
        # Carregar strings compartilhadas e estilos
        logger.info("Carregando sharedStrings.xml e styles.xml...")
        shared_strings_data = loader.load_shared_strings()
        styles_data = loader.load_styles()
        
        # Encontrar pivot tables
        logger.info("Procurando pivot tables...")
        pivots = find_pivot_tables(root_path)
        
        # Analisar cada worksheet
        logger.info("Analisando worksheets...")
        sheets_profiles = []
        
        for sheet_info in workbook_data.get('sheets', []):
            sheet_name = sheet_info.get('name', '')
            sheet_path = root_path / "xl" / "worksheets" / f"sheet{sheet_info.get('sheetId', 1)}.xml"
            
            logger.info(f"Processando aba: {sheet_name}")
            
            profiler = SheetProfiler(
                sheet_path,
                shared_strings_data.get('strings', []),
                styles_data,
                args.sample_rows
            )
            
            profile = profiler.profile_sheet()
            if profile:
                profile['name'] = sheet_name
                profile['path'] = f"xl/worksheets/sheet{sheet_info.get('sheetId', 1)}.xml"
                sheets_profiles.append(profile)
        
        # Construir manifesto
        logger.info("Construindo manifesto JSON...")
        manifest = builder.build_manifest(
            workbook_data,
            relationships,
            shared_strings_data,
            styles_data,
            sheets_profiles,
            pivots
        )
        
        # Salvar JSON
        json_path = out_path / "workbook_manifest.json"
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(manifest, f, indent=2, ensure_ascii=False)
        
        logger.info(f"JSON salvo: {json_path}")
        
        # Gerar Markdown
        logger.info("Gerando relatório Markdown...")
        markdown_content = markdown_writer.generate_summary(manifest)
        
        md_path = out_path / "WORKBOOK_SUMMARY.md"
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        
        logger.info(f"Markdown salvo: {md_path}")
        
        # Imprimir caminhos absolutos
        print(f"\n✅ Análise concluída!")
        print(f"📄 Manifest JSON: {json_path.absolute()}")
        print(f"📋 Relatório Markdown: {md_path.absolute()}")
        
        return 0
        
    except Exception as e:
        logger.error(f"Erro durante processamento: {e}")
        logger.exception("Detalhes do erro:")
        return 1


if __name__ == "__main__":
    exit(main())
