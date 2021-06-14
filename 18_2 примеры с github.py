
import requests
import json


r = requests.get('https://baconipsum.com/api/?type=meat-and-filler')
texts = json.loads(r.content)  # делаем из полученных байтов python объект для удобной работы
print(texts[0])  # проверяем тип сконвертированных данных
