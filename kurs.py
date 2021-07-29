# -*- coding: utf-8 -*-
from lxml import etree
from prettytable import PrettyTable
import requests

def kursvalue():
    x = PrettyTable()
    valuta = {
    }
    get_xml = requests.get('https://nationalbank.kz/rss/rates_all.xml')
    structure = etree.fromstring(get_xml.content)
    usd = structure.find(".//*[title='USD']/description")
    valuta['dollar'] = usd.text
    euro = structure.find(".//*[title='EUR']/description")
    valuta['euro'] = euro.text
    rub = structure.find(".//*[title='RUB']/description")
    valuta['rub'] = rub.text

    x.field_names = ["Валюта", "Курс"]
    x.add_row(["Dollar", valuta['dollar']])
    x.add_row(["Euro", valuta['euro']])
    x.add_row(["RUB", valuta['rub']])
    print(x)
kursvalue()
k = input("Программа завершена, нажмите клавишу Enter для закрытия окна приложения")