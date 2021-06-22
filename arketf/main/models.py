from django.db import models


class Stock(models.Model):
    name = models.CharField(max_length = 100)
    ticker = models.CharField(max_length = 10)
    price = models.DecimalField(max_digits = 20, decimal_places=2, null = True) # Always the current date close price?
    market_cap = models.DecimalField(max_digits = 20, decimal_places=2, null = True)
    cusip = models.CharField(max_length = 20, unique = True) # ark's own ID for stock (unique per stock)
    
    def __str__(self):
        return self.ticker

class Fund(models.Model):
    name = models.CharField(max_length = 100)
    ticker = models.CharField(max_length = 20, unique = True)
    price = models.DecimalField(max_digits = 20, decimal_places=2)

    def __str__(self):
        return self.ticker

class Trade(models.Model):
    stock = models.ForeignKey(Stock, on_delete = models.CASCADE) # Do nothing because even the stock is deleted but the trade exist.
    date = models.DateTimeField()
    direction = models.CharField(max_length = 5)
    shares = models.BigIntegerField()
    fund = models.ForeignKey(Fund, on_delete = models.CASCADE)
    etf_percent = models.DecimalField(max_digits = 10, decimal_places=2)

    
    def __str__(self):
        return "Buy " + self.stock.ticker + " for " + str(self.shares) 


class Holding(models.Model):
    stock = models.ForeignKey(Stock, on_delete= models.CASCADE)
    fund = models.ForeignKey(Fund, on_delete= models.CASCADE)
    shares = models.BigIntegerField()
    market_value = models.DecimalField(max_digits = 20, decimal_places=2)
    weight = models.DecimalField(max_digits = 10, decimal_places=2)

    def __str__(self):
        return self.fund.ticker + ' ' + self.stock.ticker

