from html.parser import HTMLParser
from .base import WarehouseBase

class Parser(HTMLParser):
    STATUSES = ['OPEN', 'CLOSED']
    def __init__(self):
        super().__init__()
        self.statuses = []

    def handle_data(self, data):
        if data in Parser.STATUSES:
            self.statuses.append(data)

class WHCorpWarehouse(WarehouseBase):
    def __init__(self):
        super().__init__('whcorp', 'https://bluecargo.julink.fr/site1/index.html', Parser())
        self.status_map = {
            'OPEN': 'Free',
            'CLOSED': 'closed',
        }
