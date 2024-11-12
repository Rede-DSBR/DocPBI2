from dataclasses import dataclass, field

@dataclass
class Table:
    """
    Estrutura de dados para tabelas regulares (regular tables) retirados do json
    (DataModelSchema) do pbi para alimentar o jinja2
    """
    name: str
    columns: list = field(default_factory=lambda : []) 
    description: str = ''
    author: str = ''
    version: str = ''
    date: str = ''


@dataclass
class Column:
    """
    Estrutura de dados para colunas (columns) retirados do json (DataModelSchema) do
    pbi para alimentar o jinja2
    """
    name: str
    summarizeBy: str = ''
    dataType: str = ''
    description: str = ''
    author: str = ''
    version: str = ''
    date: str = ''


@dataclass
class Measure:
    """
    Estrutura de dados para medidas (measures) retirados do json (DataModelSchema) do
    pbi para alimentar o jinja2
    """
    name: str
    dax: str = ''
    description: str = ''
    author: str = ''
    version: str = ''
    date: str = ''

@dataclass
class CalculatedColumn:
    """
    Estrutura de dados de colunas calculadas (calculated columns) retirados do json
    (DataModelSchema) do pbi para alimentar o jinja2
    """
    name: str
    calc_code: str = ''
    summarizeBy: str = ''
    description: str = ''
    author: str = ''
    version: str = ''
    date: str = ''