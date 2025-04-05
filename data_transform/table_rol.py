import pdfplumber
import pandas as pd


pdf_path = "/Users/izabellamaria/fast-scraping/data/attachments/anexo1.pdf"
csv_path = "/Users/izabellamaria/fast-scraping/data/attachments/anexocsv1.csv"

all_tables = []

with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        tables = page.extract_table()
        if tables:
            all_tables.extend(tables)

if all_tables:
    df = pd.DataFrame(all_tables)
    df.to_csv(csv_path, index=False, header=False)
    print(f"Conversão concluída! CSV salvo em {csv_path}")
else:
    print("Nenhuma tabela encontrada no PDF.")

#chama a função
