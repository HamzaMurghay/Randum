from bs4 import BeautifulSoup
import requests
import time
import pandas as pd


with open("cookies.txt") as f:
    x = f.read()

x = x.splitlines()

cookie_val = {line.split("\t")[0]:line.split("\t")[1] for line in x}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
}

url = "https://www.pcgamebenchmark.com/compatible-games"


base_url = "https://www.pcgamebenchmark.com/compatible-games/page-{}"

for page in range(2, 7):
    url = base_url.format(page)
    response = requests.get(url, cookies=cookie_val, headers=headers)

    if response.status_code != 200:
        print(f'Failed to fetch page {page}')
        continue

    chai = BeautifulSoup(response.content, 'lxml')

    titles = chai.find_all('a', class_="name")

    for tag in titles:
        title = tag['title']
        title = title.replace(" System Requirements", "")

        print(title)



# print(chai)