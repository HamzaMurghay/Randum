from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://www.pcgamebenchmark.com/compatible-games"

page = requests.get(url)

chai = BeautifulSoup(page.text, 'lxml')

print(chai)