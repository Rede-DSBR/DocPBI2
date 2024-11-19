from dataclasses import dataclass, field

@dataclass
class TMDL:
    """
    Estrutura de dados para o modelo de dados (DataModelSchema) retirados do json
    do pbi para alimentar o jinja2
    """
    description: str = ''
    element: str = ""
    properties: list = field(default_factory=lambda : [])
    calculation: str = ''
    @classmethod
    def create(cls, description, element, properties, calculation=''):
        return cls(description, element, properties, calculation)
    
    def __str__(self):
        prop_str = "\n".join(
            f"\t{'-' * 10}\n\tDescription: {prop.description}\n\tElement: {prop.element}\n\tProps: {prop.properties}\n\tCalcs: {prop.calculation}"
            if isinstance(prop, TMDL) else f"\t{prop}"
            for prop in self.properties
        )
        return (
            f"Description: \n{self.description}\n"
            f"Element: \n{self.element}\n"
            f"Properties:\n{prop_str}\n"
            f"Calculation: {self.calculation}\n{'-' * 20}"
        )

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