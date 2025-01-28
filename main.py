from data_model import *
from parse_tmdl import TMLDParser

file_content = 'pbip/PNP_Publicada_dev.SemanticModel/definition/tables/NaturezaDespesa.tmdl'
file_content = 'pbip/PNP_Publicada_dev.SemanticModel/definition/model.tmdl'
file_content = 'pbip/PNP_Publicada_dev.SemanticModel/definition/tables/dimCurso.tmdl'

tmdl = TMLDParser('pbip/PNP_Publicada_dev.pbip')
tables = tmdl.parse_all_tables()

for table_name, table_data in tables.items():
    print('\n\n\n')
    print(f"Table Name: {table_name}")
    for t in table_data:
        print(t)

tmdl.save_to_json('pbip/tables.json')

