# Extração e Transformação de Dados com Python

Este projeto realiza o processo de **web scraping**, **compactação de arquivos** e **transformação de dados** utilizando a linguagem **Python**, com foco em automação e estruturação de dados públicos.

## 🕸️ Web Scraping

Foi feito o acesso ao site oficial da ANS:

🔗 [https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos](https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos)

Utilizando a biblioteca **requests**, o sistema realiza o download automático dos arquivos **Anexo I** e **Anexo II** em formato **PDF**.

## 🗜️ Compactação dos Arquivos

Após o download, os arquivos são compactados em um único `.zip` com a biblioteca **zipfile**. O código também utiliza **os** e **os.path** para manipulação de diretórios e nomes de arquivos.

## 📄 Extração e Transformação de Dados

A tabela *Rol de Procedimentos e Eventos em Saúde*, presente no **Anexo I**, é extraída utilizando a biblioteca **pdfplumber**, que permite a leitura precisa de tabelas em arquivos PDF.

Em seguida, os dados extraídos são organizados e convertidos em uma tabela estruturada no formato **CSV** com o uso da biblioteca **pandas**.

## 📦 Bibliotecas Utilizadas

- **requests** – Para fazer requisições HTTP e download de arquivos PDF.
- **pdfplumber** – Para extração de dados de tabelas dentro dos PDFs.
- **pandas** – Para manipulação e exportação dos dados estruturados em CSV.
- **zipfile** – Para compressão dos arquivos em um único `.zip`.
- **os** e **os.path** – Para operações com o sistema de arquivos.
- **data** – Módulo interno utilizado para separação de lógica e organização do código.

---

Sinta-se à vontade para clonar, testar e sugerir melhorias neste projeto! 🚀
