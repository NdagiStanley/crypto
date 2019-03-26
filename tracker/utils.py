from django_cron import CronJobBase, Schedule
from django.core.mail import send_mail

from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

import os


def get_prices(coins):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
        'start': '1',
        'limit': '5000',
        'convert': 'USD',
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': os.getenv('API_KEY_COINMARKET'),
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)

        prices = {}
        coins = [coin.lower() for coin in coins]

        for price in data['data']:
            if price['slug'] in coins:
                prices[price['slug']] = price['quote']['USD']['price']
        return prices

    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
        return None


def send_email(email, prices):
    message = '''Good morning! This is how your coins are priced today.
                '''
    for coin_name, price in prices.items():
        message += f'''
            The price for {coin_name.upper()} in USD is ${price}'''

    send_mail(
        'Crypto daily update',
        message,
        'no_reply@crypto.io',
        [email],
        fail_silently=False,
    )


def daily_send_emails():
    from .models import User
    users = User.objects.all()
    for user in users:
        email = user.email
        coins = user.get_coins()
        prices = get_prices(coins)

        print(f'< {email} | {prices} >')
        send_email(email, prices)


class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 1

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'crypto.my_cron_job'

    def do(self):
        daily_send_emails()
