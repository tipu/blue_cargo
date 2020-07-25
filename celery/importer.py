from celery import Celery
import celeryconfig
from parsers import whcorp, american_storage

app = Celery()
app.config_from_object('celeryconfig')

parsers = [whcorp, american_storage]
@app.task
def import_data():
    for parser in parsers:
        if not hasattr(parser, 'run'):
            raise ValueError('parser file must define a `run` function')
        result = parser.run()
        print(result)


