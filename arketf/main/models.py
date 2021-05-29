from django.db import models


class Stock(models.Model):
    name = models.CharField(max_length = 100)
    ticker = models.CharField(max_length = 20, unique = True)
    price = models.DecimalField(max_digits = 20, decimal_places=2) # Always the current date close price?
    market_cap = models.DecimalField(max_digits = 20, decimal_places=2)
    cusip = models.CharField(max_length = 20, unique = True) # ark's own ID for stock (unique per stock)
    
    def __str__(self):
        return self.ticker


class Trade(models.Model):
    stock = models.ForeignKey(Stock, on_delete = models.DO_NOTHING) # Do nothing because even the stock is deleted but the trade exist.
    date = models.DateTimeField()
    direction = models.CharField(max_length = 5)
    shares = models.BigIntegerField()
    # fund = models.ForeignKey(Fund, on_delete = models.DO_NOTHING)
    etf_percent = models.DecimalField(max_digits = 10, decimal_places=2)

    
    def __str__(self):
        return "Buy " + self.stock.ticker + " for " + str(self.shares) + " on " + self.date

# class Fund(models.Model):
    


# tsla = Stock(name = "Tesla", ticker = "TSLA", price = 187.87, market_cap = 87.87, cusip = "88160R101")
# msft = Stock(name = "Microsoft", ticker = "MSFT", price = 287.87, market_cap = 387.87, cusip = "881608787")
# gme = Stock(name = "Gamestop", ticker = "GME", price = 693.87, market_cap = 69.420, cusip = "881606969")

# trade1 = Trade(stock = tsla, date = datetime.date(2020, 10, 9), direction = "Buy", shares = 1234356, etf_percent = 0.087)
# trade2 = Trade(stock = tsla, date = datetime.date(2020, 10, 10), direction = "Sell", shares = 1256, etf_percent = 0.007)
# trade3 = Trade(stock = msft, date = datetime.date(2020, 8, 7), direction = "Buy", shares = 8787, etf_percent = 0.00087)
# trade4 = Trade(stock = msft, date = datetime.date(2020, 8, 8), direction = "Sell", shares = 6969, etf_percent = 0.00697)
# trade5 = Trade(stock = gme, date = datetime.date(2020, 4, 20), direction = "Buy", shares = 42069, etf_percent = 0.0042069)
# trade6 = Trade(stock = gme, date = datetime.date(2020, 4, 21), direction = "Sell", shares = 156, etf_percent = 0.00087)
