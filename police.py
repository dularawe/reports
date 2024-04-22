import requests
from bs4 import BeautifulSoup
import os


def download_pdf(url, directory):
    filename = os.path.join(directory, url.split('/')[-1])
    with open(filename, 'wb') as f:
        f.write(requests.get(url).content)
    print(f"Downloaded: {filename}")


url = ""


response = requests.get(url)
html_content = response.content


soup = BeautifulSoup(html_content, 'html.parser')


tables = soup.find_all('table')


directory = 'pdf_files'
if not os.path.exists(directory):
    os.makedirs(directory)


for table in tables:

    rows = table.find_all('tr')

    for row in rows:

        links = row.find_all('a', href=True)

        for link in links:
            pdf_url = link['href']
   
            if pdf_url.endswith('.pdf'):
                download_pdf(pdf_url, directory)
