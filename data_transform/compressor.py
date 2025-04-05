from zipfile import ZipFile
import os
from os.path import basename

arquivos_csv = ['anexocsv1.csv']

def compress_attachments(files, arquivo_zip):
    output_dir = "/Users/izabellamaria/fast-scraping/data"
    zip_path = os.path.join(output_dir, arquivo_zip)

    with ZipFile(zip_path, 'w') as zipObj:
        for folderName, subfolders, filenames in os.walk(output_dir):
            for filename in filenames:
                filepath = os.path.join(folderName, filename)
                zipObj.write(filepath, basename(filepath))

    print(f"Arquivos compactados com sucesso em {zip_path}")

compress_attachments(arquivos_csv, "csv_attachments.zip")
