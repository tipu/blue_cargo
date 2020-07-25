from html.parser import HTMLParser
import requests

VALID_DATA = ['OPEN', 'CLOSED']

class Parser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.result = []

    def handle_data(self, data):
        if data in VALID_DATA:
            self.result.append(data)

def run():
    url = 'https://bluecargo.julink.fr/site1/index.html'
    html = requests.get(url).text
    parser = Parser()
    parser.feed(html)

    return parser.result
