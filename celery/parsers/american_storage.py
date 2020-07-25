from html.parser import HTMLParser
from .base import WarehouseBase

class Parser(HTMLParser):
    STATUSES = ['free', 'closed', 'appointment required']
    def __init__(self):
        super().__init__()
        self.statuses = []

    def handle_data(self, data):
        if data.startswith(': ') and \
           data[2:] in Parser.STATUSES and \
           len(self.statuses) < 10:
            self.statuses.append(data[2:])

class AmericanStorageWarehouse(WarehouseBase):
    def __init__(self):
        super().__init__('american_storage', 'https://bluecargo.julink.fr/site2/index.html', Parser())
        self.status_map = {
            'free': 'Free',
            'appointment required': 'Appointment required',
            'closed': 'closed'
        }
