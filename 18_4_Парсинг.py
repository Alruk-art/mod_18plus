import requests # импортируем наш знакомый модуль
import lxml.html
from lxml import etree

html = requests.get('https://www.python.org/').content  # получим html главной странички официального сайта Python

tree = lxml.html.document_fromstring(html)
title = tree.xpath('/html/head/title/text()')

print(title)  # выводим полученный заголовок страницы


from lxml import etree

tree = etree.parse('Welcome to Python.org.html', lxml.html.HTMLParser())

ul = tree.findall('body/div[1]/div[3]/div/section/div/div[1]/div/ul/li')

# создаём цикл в котором будем выводить название каждого элемента из списка
for li in ul:
    a = li.find('a')
    print(a.text)



