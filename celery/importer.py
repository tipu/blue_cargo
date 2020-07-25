from celery import Celery
import json
import celeryconfig
from parsers import whcorp, american_storage
import redis

redis = redis.Redis(host='localhost', port=6379)

app = Celery()
app.config_from_object('celeryconfig')

warehouses = [whcorp.WHCorpWarehouse(),
              american_storage.AmericanStorageWarehouse()]
@app.task
def import_data():
    for warehouse in warehouses:
        result = warehouse.run()
        key = 'warehouse_%s' % warehouse.id
        pipe = redis.pipeline()
        pipe.delete(key)
        pipe.lpush(key, *result)
        pipe.execute()


