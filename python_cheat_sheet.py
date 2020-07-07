import requests
from bs4 import BeautifulSoup
import datetime

def course():
    url = 'https://www.nbkr.kg/XML/daily.xml'
    page = requests.get(url).text
    valuta = BeautifulSoup(page, 'html.parser')

    id_dollar = 'USD'
    id_evro = 'EUR'
    id_rub = 'RUB'
    id_tenge = 'KZT'

    for line in valuta.currencyrates('currency'):
        for line2 in line.value:
            tyni = line2
        tag =  line
        id_v = tag['isocode']
        if id_v == id_dollar:
            som_dollar = tyni
        if id_v == id_evro:
            som_euro = tyni
        if id_v == id_rub:
            som_rub = tyni
        if id_v == id_tenge:
            som_tenge = tyni
    today = datetime.date.today()
    return som_dollar, som_euro, som_rub, som_tenge, today        
          
dollar, euro, rub, tenge, todaydata = course()
# if __name__ == "__main__":
#         print("\n",course())

# -------------------------------------------------------------------------------------