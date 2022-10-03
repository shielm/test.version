#Задание 1 (Курс по Питону - МФТИ)
#Напишите функцию, которая возвращает название валюты (поле 'Name') с максимальным значением курса с помощью
# сервиса https://www.cbr-xml-daily.ru/daily_json.js

import requests

def max_currency_value():
        all_currencies_value={}
        r = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
        response = r.json()['Valute']
        for i in response:
            all_currencies_value[i]=response[i]['Value']
        max_currencies_value_name=max(all_currencies_value.keys(),key=(lambda x:all_currencies_value[x]))
        return response[max_currencies_value_name]['Name']

print(max_currency_value())
