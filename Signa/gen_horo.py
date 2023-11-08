import requests
from bs4 import BeautifulSoup
from datetime import date
import random
from Signa.models import Horoscope



def scrap(sign:str):
    url = f"https://www.spiriteo.com/fr-fr/horoscope-du-jour/{sign}"
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to get page: {url}")
        return None
    soup = BeautifulSoup(response.text, 'html.parser')
    element_amour = soup.select_one('body > main > article > div.container > div > div:nth-child(2) > div > div.content_box.col-sm-12.col-md-12.wow.fadeIn.animated > div.horoscope-page > div > div:nth-child(1) > section:nth-child(1) > p')
    element_sante = soup.select_one('body > main > article > div.container > div > div:nth-child(2) > div > div.content_box.col-sm-12.col-md-12.wow.fadeIn.animated > div.horoscope-page > div > div:nth-child(2) > section:nth-child(1) > p')
    element_argent = soup.select_one('body > main > article > div.container > div > div:nth-child(2) > div > div.content_box.col-sm-12.col-md-12.wow.fadeIn.animated > div.horoscope-page > div > div:nth-child(1) > section:nth-child(2) > p')
    element_travail = soup.select_one('body > main > article > div.container > div > div:nth-child(2) > div > div.content_box.col-sm-12.col-md-12.wow.fadeIn.animated > div.horoscope-page > div > div:nth-child(2) > section:nth-child(2) > p')
    element_famille = soup.select_one('body > main > article > div.container > div > div:nth-child(2) > div > div.content_box.col-sm-12.col-md-12.wow.fadeIn.animated > div.horoscope-page > div > div:nth-child(4) > section:nth-child(1) > p')
    dic = {
        "amour":element_amour.text,
        "sante":element_sante.text,
        "argent":element_argent.text,
        "travail":element_travail.text,
        "famille":element_famille.text,
        }
    return dic

def database():
    signes = ["belier","taureau","gemeaux","cancer","lion","vierge","balance","scorpion","sagittaire","capricorne","verseau","poisson"]
    for signe in signes:
        dic = scrap(signe)
        Horoscope.objects.create(
                date = date.today(),
                sign = signe,
                travail = dic["travail"],
                argent = dic["argent"],
                sante = dic["sante"],
                amour = dic["amour"],
                nombre = random.randint(0,1000),
                famille = dic["famille"]
              )



