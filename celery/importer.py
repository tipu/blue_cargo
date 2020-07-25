from celery import Celery
import celeryconfig

app = Celery()
app.config_from_object('celeryconfig')

def american_storage_parser():
    url = 'https://bluecargo.julink.fr/site2/index.html'

def whcorp_parser():
    url = 'https://bluecargo.julink.fr/site1/index.html'

warehouses = [
    american_storage_parser,
    whcorp_parser,
]
@app.task
def import_data():
    for warehouse_details in warehouses:
        print(warehouse_details)


