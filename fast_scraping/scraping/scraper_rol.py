import requests


def download_rol(url, endereco):
    response = requests.get(url)
    with open(endereco, 'wb') as novo_arquivo:
        novo_arquivo.write(response.content)

if __name__ == "__main__":
    download_rol("https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf", 'testeanexo1.pdf')
    download_rol("https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_II_DUT_2021_RN_465.2021_RN628.2025_RN629.2025.pdf", 'testeanexo2.pdf')

