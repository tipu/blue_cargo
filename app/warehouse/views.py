from django.shortcuts import render
import redis

redis = redis.Redis(host='localhost', port=6379, decode_responses=True)

#TODO: need to store time in a timezone-agnostic way
hours = {
    'whcorp': [
    ],
    'american_storage': [
    ],
}

def home(request):
    keys = ['whcorp', 'american_storage']
    result = {}
    for key in keys:
        result[key] = redis.lrange('warehouse_%s' % key, 0, -1)
    return render(request, 'home.html', result)

def availability(request):
    pass
