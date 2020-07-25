from django.shortcuts import render
import redis

redis = redis.Redis(host='localhost', port=6379, decode_responses=True)

def home(request):
    #TODO: store in an agnostic way
    data = {
        'whcorp': ['10am', '3pm', '7am', '3pm', '7am', '3pm', '7am', '3pm', '7am', '3pm'],
        'american_storage': ['7a', '3pm', '7a', '3pm', '7a', '3pm', '7a', '3pm', '7a', '3pm']
    }

    keys = ['whcorp', 'american_storage']
    for key in keys:
        i = 0
        for status in redis.lrange('warehouse_%s' % key, 0, -1):
            data[key][i] += ': ' + status
            i += 1
    return render(request, 'home.html', data)

def availability(request):
    pass
