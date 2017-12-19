import requests
from bs4 import BeautifulSoup

url = input("Enter url to scrape links: ")

data = requests.get(url)

soup = BeautifulSoup(data.content, 'lxml')

links = soup.find_all('a')

for link in links:
    print(link.get('href'))
