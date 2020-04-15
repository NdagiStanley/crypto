from django.shortcuts import render, render_to_response
from .utils import get_prices, send_email
from .models import User


def index(request):
    return render(request, 'index.html')


def track(request):
    payload = dict(request.GET)
    if payload.get('email') and payload.get('coin'):
        submitted = True
        coins, email = payload.get('coin'), payload.get('email')[0]
        if User.objects.filter(email=email):
            user = User.objects.get(email=email)
            user.set_coins(coins)
            user.save()
        else:
            new_user = User.objects.create(email=email)
            new_user.set_coins(coins)
            new_user.save()
        prices = get_prices(coins)
        send_email(email, prices)

    else:
        submitted = False
    return render_to_response('index.html', {'submitted': submitted})


def unsubscribe(request):
    payload = dict(request.GET)
    unsubscribed = None
    email = payload.get('email')[0]
    if User.objects.filter(email=email):
        User.objects.get(email=email).delete()
        unsubscribed = True
    else:
        unsubscribed = False
    return render_to_response('index.html', {'unsubscribed': unsubscribed})
