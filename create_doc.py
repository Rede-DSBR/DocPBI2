import json
from jinja2 import Environment, FileSystemLoader

def generate_documentation(json_path, template_path, output_path):
    """
    Generate an HTML file documenting all tables, using Jinja2 to populate a template.
    """
    with open("tables.json", "r", encoding="utf-8") as f:
        tmdl_data = json.load(f)
    tables = []
    for file_name, tmdl_list in tmdl_data.items():
        for tmdl_obj in tmdl_list:
            element = tmdl_obj.get("element", "")
            if element.startswith("table "):
                table_name = element[len("table "):].strip()
                raw_desc_list = tmdl_obj.get("description", [])
                table_description = "\n".join(raw_desc_list)
                columns = []
                for prop in tmdl_obj.get("properties", []):
                    prop_element = prop.get("element", "")
                    if prop_element.startswith("column "):
                        col_name = prop_element[len("column "):].strip()
                        col_desc_list = prop.get("description", [])
                        col_description = "\n".join(col_desc_list)
                        data_type = None
                        summarize_by = None
                        for line in prop.get("properties", []):
                            line = line.strip()
                            if line.startswith("dataType:"):
                                data_type = line.split(":", 1)[1].strip()
                            elif line.startswith("summarizeBy:"):
                                summarize_by = line.split(":", 1)[1].strip()
                        columns.append({
                            "name": col_name,
                            "description": col_description,
                            "dataType": data_type,
                            "summarizeBy": summarize_by
                        })
                tables.append({
                    "name": table_name,
                    "description": table_description,
                    "columns": columns
                })

    env = Environment(loader=FileSystemLoader('.'), autoescape=True)
    template = env.get_template(template_path)
    rendered_html = template.render(tables=tables)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(rendered_html)
    print(f"Documentation successfully generated at {output_path}")

if __name__ == "__main__":
    generate_documentation(
        json_path="tables.json",         
        template_path="template/doc_template2.html", 
        output_path="documentation.html"  
    )