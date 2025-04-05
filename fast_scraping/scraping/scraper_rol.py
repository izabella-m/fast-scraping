import requests
import data

def download_rol(url, endereco):
    response = requests.get(url)
    if response.status_code == requests.codes.ok:
        with open(endereco, 'wb') as novo_arquivo:
            novo_arquivo.write(response.content)
        print("Download concluído com sucesso!")
    else:
        response.raise_for_status()

if __name__ == "__main__":
    download_rol("https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf", '/Users/izabellamaria/fast-scraping/data/attachments/anexo1.pdf')
    download_rol("https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_II_DUT_2021_RN_465.2021_RN628.2025_RN629.2025.pdf", '/Users/izabellamaria/fast-scraping/data/attachments/anexo2.pdf')
