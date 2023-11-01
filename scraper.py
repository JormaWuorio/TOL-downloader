import requests
from bs4 import BeautifulSoup

def download_file(url, filename):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(filename, 'wb') as file:
            for i, chunk in enumerate(response.iter_content(chunk_size=8192)):
                file.write(chunk)
        print("Writing done\n")
    else:
        print("Not found\n")
        return False

with open('links.txt', 'r') as file:
    for i, row in enumerate(file):
        print(f"File nr {i}.webm")
        URL = row.strip()
        status = download_file(URL, f"video{i}")
        if status == False:
            continue
