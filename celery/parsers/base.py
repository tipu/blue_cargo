import requests

class WarehouseBase:
    def __init__(self, id, url, parser):
        self.id = id
        self.url = url
        self.parser = parser

    def run(self):
        if not hasattr(self, 'status_map'):
            raise ValueError('a `status_map` property must exist')
        html = requests.get(self.url).text
        self.parser.feed(html)
        try:
            standardized_statuses = [self.status_map[status]
                                     for status
                                     in self.parser.statuses]
        except KeyError:
            raise ValueError('status values for whcorp have changed')

        return standardized_statuses
