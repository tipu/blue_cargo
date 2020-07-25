from html.parser import HTMLParser
import requests

VALID_DATA = ['free', 'closed', 'appointment required']

class Parser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.result = []

    def handle_data(self, data):
        if data.startswith(': ') and data[2:] in VALID_DATA:
            self.result.append(data[2:])

def run():
    url = 'https://bluecargo.julink.fr/site2/index.html'
    html = requests.get(url).text
    parser = Parser()
    parser.feed(html)

    return parser.result

print(run())
