from zipfile import ZipFile
import os
from os.path import basename

arquivos_pdf = ['testeanexo1.pdf', 'testeanexo2.pdf']

def compress_attachments(files, arquivo_zip):
    output_dir = "/Users/izabellamaria/fast-scraping/data"  # Pasta onde será salvo o ZIP
    zip_path = os.path.join(output_dir, arquivo_zip)  # Caminho do ZIP

    with ZipFile(zip_path, 'w') as zipObj:
        for folderName, subfolders, filenames in os.walk(output_dir):  # Compacta tudo da pasta attachments
            for filename in filenames:
                filepath = os.path.join(folderName, filename)
                zipObj.write(filepath, basename(filepath))

    print(f"Arquivos compactados com sucesso em {zip_path}")

compress_attachments(arquivos_pdf, "attachments.zip")
