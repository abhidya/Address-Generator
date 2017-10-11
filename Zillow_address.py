import requests
from bs4 import BeautifulSoup
from random import randrange
import random
import json
from fng import FakeNameGenerator
boo = True
person= FakeNameGenerator('random', 'us', 'us')
requests.packages.urllib3.disable_warnings()
while boo:
    try:
        global use
        use = False
        class ZillowGenerator():
            def __init__(self, state):
                self.state = state
                self.html = BeautifulSoup(self.page_source(), "html.parser")
                boo = False

            def page_source(self):
                fng = requests.session()
                fng.verify = False
                rand_page = randrange(1,20,1)
                url = 'https://www.zillow.com/homes/for_sale/{}/{}_p/'.format(self.state, rand_page)
                html = fng.get(url)
                if html.text.find("The document has moved here") or html.text.find("Please verify you're a human to continue"):
                    print("zillow is unavailable: using FNG")
                    global use
                    use = True
                    global addressfng
                    addressfng= person.address()
                    global cityfng
                    cityfng = person.city()
                    global zipfng
                    zipfng = person.zip()
                boo = False

                return html.text

            def address_source(self):
                global use

                if use:
                    boo = False

                    return person.address_source()
                address_string = self.html.find_all('span', {'itemprop' : 'address'})
                boo = False

                return random.choice(address_string)

            def address(self):
                global use

                if use:
                    boo = False

                    return addressfng
                address_string = self.address_source()
                soup = BeautifulSoup(str(address_string), "html.parser")
                address = soup.find('span', {'itemprop' : 'streetAddress'})
                boo = False

                return address.get_text()

            def city(self):
                global use

                if use:
                    boo = False

                    return cityfng
                address_string = self.address_source()
                soup = BeautifulSoup(str(address_string), "html.parser")
                city = soup.find('span', {'itemprop' : 'addressLocality'})
                boo = False

                return city.get_text()

            def zip(self):
                global use

                if use:
                    boo = False

                    return zipfng
                address_string = self.address_source()
                soup = BeautifulSoup(str(address_string), "html.parser")
                zipcode = soup.find('span', {'itemprop' : 'postalCode'})
                boo = False

                return zipcode.get_text()


    except:
        print("oops")
        boo = True
        pass
#addressgen = ZillowGenerator('TN')
#print(addressgen.address())
