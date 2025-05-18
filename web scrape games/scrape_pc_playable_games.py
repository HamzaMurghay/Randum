from bs4 import BeautifulSoup
import requests
import pandas as pd


with open("cookies.txt") as f:
    x = f.read()

x = x.splitlines()

cookie_val = {line.split("\t")[0]:line.split("\t")[1] for line in x}

print(cookie_val)

url = "https://www.pcgamebenchmark.com/compatible-games"

page = requests.get(url)

chai = BeautifulSoup(page.text, 'lxml')

# print(chai)