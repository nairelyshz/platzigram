from django.http import HttpResponse
""" Utilities """
from datetime import datetime
import json

def helloworld(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Oh! hi! Current server time is {now}'.format(now = str(now)))

def hi(request):
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    # import pdb; pdb.set_trace()
    data = {
        'status': 'ok',
        'numbers': sorted_ints,
        'message': 'Integers sorted successfully'
    }
    return HttpResponse(json.dumps(data,indent=4),content_type='application/json')

def say_hi(request,name,age):
    if age < 12:
        message = 'Sorry {}, you are not allowed here'.format(name)
    else:
        message = 'Hi, {}. Welcome to Platzigram'.format(name)
    return HttpResponse(message)