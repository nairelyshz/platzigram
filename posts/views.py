from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import json

posts = [
    {
        'name': 'Mont Blac',
        'user': 'Yesica',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/id/237/200/300'
    },
    {
        'name': 'Mont Blac',
        'user': 'Yesica',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/seed/picsum/200/300'
    },
    {
        'name': 'Mont Blac',
        'user': 'Yesica',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/300?grayscale'
    }
]
# Create your views here.
def list_posts(request):
    content = []
    for post in posts:
        content.append("""
            <p><strong>{name}</strong></p>
            <p><small>{user} - <i>{timestamp}</i></small></p>
            <figure><img src="{picture}"/></figure>""".format(**post))
    return HttpResponse('<br>'.join(content))