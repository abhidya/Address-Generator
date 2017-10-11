# Address-Generator
Returns a real address from Zillow.com or a fake address from Fakenamegenerator.com

To use this with your program you need the file in the root project folder and in your program header​
Code:

from Zillow_address import ZillowGenerator

Usage:​

addressgen = ZillowGenerator('AK')

address = addressgen.address()

city = addressgen.city()

zip = addressgen.zip()




it would return

address: 2288 W Rivulet Ave

city: Wasilla

zip: 99577

