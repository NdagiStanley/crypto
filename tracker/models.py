from django.db import models


class User(models.Model):
    email = models.EmailField(unique=True)
    coins = models.TextField()

    def set_coins(self, coins):
        for coin in coins:
            self.coins += f'{coin},'

    def get_coins(self):
        if self.coins:
            return self.coins.split(',')[:-1]  # Because of the trailing comma
        else:
            None
