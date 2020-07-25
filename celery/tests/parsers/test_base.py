# for python 2: use mock.patch from `pip install mock`.
import unittest
from unittest.mock import patch
from parsers.base import WarehouseBase
from parsers.whcorp import Parser, WHCorpWarehouse
from importer import import_data
import redis

redis = redis.Redis(host='localhost', port=6379)

class TestBaseWarehouse(unittest.TestCase):
    def test_checks_initialization(self):
        class BadWarehouse(WarehouseBase):
            pass
        warehouse = BadWarehouse(None, None, None)
        self.assertRaises(ValueError, warehouse.run)

    def test_checks_for_scraping_changes(self):
        class BadWHCorpWarehouse(WHCorpWarehouse):
            def __init__(self):
                super().__init__()
                self.status_map = {}
        warehouse = BadWHCorpWarehouse()
        self.assertRaises(ValueError, warehouse.run)


    def test_check_successful_run(self):
        redis.flushdb()
        self.assertEqual(0, redis.dbsize())
        import_data()
        self.assertEqual(2, redis.dbsize())
        self.assertEqual(10, len(redis.lrange('warehouse_whcorp', 0, -1)))
        self.assertEqual(10, len(redis.lrange('warehouse_american_storage', 0, -1)))
