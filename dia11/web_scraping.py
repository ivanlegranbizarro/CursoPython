import bs4
import requests

url = "https://escueladirecta-blog.blogspot.com/"

resultado = requests.get(url)

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

print(sopa.select('title')[0].get_text())
