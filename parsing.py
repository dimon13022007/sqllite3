import requests
from bs4 import BeautifulSoup as Borsch
url = requests.get('https://ua.sinoptik.ua/погода-київ/')
sup = Borsch(url.content, 'html.parser')

for el in sup.select('#content'):
    t_min = el.select('.temperature .min')[0].text
    print(t_min)















