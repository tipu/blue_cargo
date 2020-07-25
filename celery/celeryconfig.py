from celery.schedules import crontab

broker_url = 'redis://localhost:6379/1'
imports = ('importer',)

beat_schedule = {
    'warehouse-parser': {
        'task': 'importer.import_data',
        'schedule': crontab(),
    },
}
