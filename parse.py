import requests
from bs4 import BeautifulSoup
import lxml
from local_fake_useragent import UserAgent

uas = UserAgent()
headers = {'User-agent': uas.rget}


def parse():
    link = 'https://coinmarketcap.com/uk/currencies/toncoin/'
    response = requests.get(link, headers=headers).text
    soup = BeautifulSoup(response, 'lxml')
    finder = soup.find('div', class_='sc-16891c57-0 hqcKQB flexStart alignBaseline').text
    price = finder.split()[0]
    return price
