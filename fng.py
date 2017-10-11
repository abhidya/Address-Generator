'''
Script: FakeNameGenerator Scraper
Version: 0.1.3
Update: January 3 2014
Author: rastof.com@gmail.com
'''

import requests
from bs4 import BeautifulSoup


class FakeNameGenerator():
    def __init__(self, gender="random", name="us", country="us"):
        self.gender = gender
        self.name = name
        self.country = country
        self.html = BeautifulSoup(self.page_source(), "html.parser")

    def page_source(self):
        fng = requests.session()
        fng.headers.update({
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'en-US,en;q=0.8',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'DNT': '1',
            'Host': 'www.fakenamegenerator.com',
            'Pragma': 'no-cache',
            'Referer': 'http://www.fakenamegenerator.com/',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
        })
        url = 'http://www.fakenamegenerator.com/gen-{}-{}-{}.php'.format(self.gender, self.name, self.country)
        html = fng.get(url)

        return html.text

    def full_name(self):
        name_string = self.html.select('#details > div.content > div.info > div > div.address > h3')
        name = ''

        if len(name_string) > 0:
            name = name_string[0].get_text()
        else:
            name = "can't find name"
        return name

    def first_name(self):
        name = self.full_name()
        name_parts = name.split(" ")

        return name_parts[0]

    def last_name(self):
        name = self.full_name()
        name_parts = name.split(" ")

        return name_parts[2]

    def address_source(self):
        address_string = self.html.select('#details > div.content > div.info > div > div.address > div')

        return address_string

    def address(self):
        address_string = self.address_source()
        address = ''

        if len(address_string) > 0:
            address = str(address_string[0]).split('<br/>')[0].replace('<div class="adr">', '').strip()
        else:
            address = "can't find address"
        return address

    def city(self):
        city_string = self.address_source()
        city = ''

        if len(city_string) > 0:
            city = str(city_string[0]).split('<br/>')[1].split(',')[0]
        else:
            city = "can't find city"
        return city

    def state(self):
        state_string = self.address_source()
        state = ''

        if len(state_string) > 0:
            state = str(state_string[0]).split('<br/>')[1].split(',')[1].strip().split(' ')[0]
        else:
            state = "can't find state"
        return state

    def zip(self):
        zip_string = self.address_source()
        zipcode = ''

        if len(zip_string) > 0:
            zipcode = str(zip_string[0]).split('<br/>')[1].split(',')[1].strip().split(' ')[1]
        else:
            zipcode = "can't find zipcode"
        return zipcode

    def phone(self):
        phone_string = self.html.select('#details > div.content > div.info > div > div.extra > dl.dl-horizontal > dd')
        phone = ''
        print(phone_string)
        if len(phone_string) > 0:
            phone = phone_string[0].get_text()
        else:
            phone = "can't find phone"
        return phone

    def username(self):
        username_string = self.html.find_all("dd")[9].text.lower()

        if len(username_string) > 0:
            username = username_string
        else:
            username = "can't find username"
        return username

    def company(self):
        company_string = self.html.find_all("dd")[16].text
        return company_string
