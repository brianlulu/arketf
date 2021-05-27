from django.db import models


class Stock(models.Model):
    name = models.CharField(max_length = 100)
    ticker = models.CharField(max_length = 20, unique = True)
    price = models.DecimalField(max_digits = 20, decimal_places=2) # Always the current date close price?
    market_cap = models.DecimalField(max_digits = 20, decimal_places=2)

    def __str__(self):
        return self.ticker