import pandas as pd
from yfinance import ticker
from .models import *
import yfinance as yf
from datetime import datetime
from os import listdir
import pytz

#TODO: Fix updating price twice if there are two same ticker trades per date!
#TODO: Fix efficiency? Maybe?

def parse_daily_content(html_content):

    table = html_content.find_elements_by_tag_name('tr')

    data_dict = {
        'index': [], 
        'Fund': [], 
        'Date': [], 
        'Direction': [], 
        'Ticker': [],
        'CUSIP': [],
        'Company': [],
        'Shares': [],
        '% of ETF': []
        }
    
    for rows in table:
        row = rows.find_elements_by_tag_name('td')
        if(row[1].text != "Fund") and (len(row) == 9):
            data_dict['index'].append(row[0].text)
            data_dict['Fund'].append(row[1].text)
            data_dict['Date'].append(row[2].text)
            data_dict['Direction'].append(row[3].text)
            data_dict['Ticker'].append(row[4].text)
            data_dict['CUSIP'].append(row[5].text)
            data_dict['Company'].append(row[6].text)
            data_dict['Shares'].append(row[7].text)
            data_dict['% of ETF'].append(float(row[8].text))

    df = pd.DataFrame(data = data_dict)

    trade_date = data_dict['Date'][0].replace('/', '-')

    #TODO: Fix file path when deploy
    
    path = '/Users/brianlu/side-projects/ark-etf-website/arketfdata/' + trade_date + '_dailytrade.csv'

    df.to_csv(path, index= False)


def save_daily_trade(csv_path):

    df = pd.read_csv(csv_path)

    for index, row in df.iterrows():
        
        print(str(index) + 'th data entry!')
        # if stock exist in db, then update price
        if Stock.objects.filter(cusip = row.CUSIP).exists() or Stock.objects.filter(ticker = row.Ticker).exists(): 

            Trade.objects.create(
                stock = Stock.objects.get(cusip = row.CUSIP),
                date = datetime.strptime(row.Date, '%m/%d/%Y').replace(tzinfo=pytz.timezone('America/New_York')),
                direction = row.Direction,
                shares = int(row.Shares.replace(',', '')),
                fund = Fund.objects.get(ticker = row.Fund), #TODO: if fund does not exist create one?
                etf_percent = float(row[8])
            )

        else:
            
            print('Creating ' + row.Ticker + ' Stock Object!')
            stock_info = yf.Ticker(row.Ticker).info

            if 'previousClose' in stock_info.keys():
                price = stock_info.get('previousClose')
            else:
                price = 0.0

            if 'marketCap' in stock_info.keys():
                market_cap = stock_info.get('marketCap')
            else:
                market_cap = 0.0

        
            Stock.objects.create(
                name = row.Company, 
                ticker = row.Ticker,
                price = price,
                market_cap = market_cap,
                cusip = row.CUSIP
                )

            Trade.objects.create(
                stock = Stock.objects.get(cusip = row.CUSIP),
                date = datetime.strptime(row.Date, '%m/%d/%Y').replace(tzinfo=pytz.timezone('America/New_York')),
                direction = row.Direction,
                shares = int(row.Shares.replace(',', '')),
                fund = Fund.objects.get(ticker = row.Fund), #TODO: if fund does not exist create one?
                etf_percent = float(row[8])
            )

def get_file_path(data_storage_path):
    
    files = listdir(data_storage_path)
    files_list = []
    date_list = []

    for t in Trade.objects.all():
        if t.date not in date_list:
            date_list.append(t.date)

    for f in files:
        if ('.csv' in f):
            date = f.split("_")[0] 
            date = datetime.strptime(date, '%m-%d-%Y').replace(tzinfo=pytz.timezone('America/New_York'))
            if date not in date_list:
                files_list.append(data_storage_path+f)
    
    return files_list

def save_holding_csv(csv_path):

    files = listdir(csv_path)

    for p in files:
        file_path = csv_path + "/" + p
        df = pd.read_csv(file_path)

        for index, row in df.iterrows():

            if pd.isnull(row.fund):
                continue

            if Stock.objects.filter(cusip = row.cusip).exists() or Stock.objects.filter(name = row.ticker).exists():
                
                try: 
                    stock = Stock.objects.get(cusip = row.cusip)
                except:
                    stock = Stock.objects.get(name = row.company)
                    print(row)

                Holding.objects.create(
                    stock = stock,
                    fund = Fund.objects.get(ticker = row.fund),
                    shares = int(row.shares),
                    market_value = float(row[6]),
                    weight = float(row[7]),
                    date = datetime.strptime(row.date, '%m/%d/%Y').replace(tzinfo=pytz.timezone('America/New_York')),
                )

            else:
                if pd.isnull(row.ticker):
                    print('Creating ' + row.company + ' Stock Object!')
                    price = 0.0
                    market_cap = 0.0
                else: 
                    print('Creating ' + row.ticker + ' Stock Object!')
                    stock_info = yf.Ticker(row.ticker).info

                    if 'previousClose' in stock_info.keys():
                        price = stock_info.get('previousClose')
                    else:
                        price = 0.0

                    if 'marketCap' in stock_info.keys():
                        market_cap = stock_info.get('marketCap')
                    else:
                        market_cap = 0.0


            
                Stock.objects.create(
                    name = row.company, 
                    ticker = row.ticker,
                    price = price,
                    market_cap = market_cap,
                    cusip = row.cusip
                    )

                try: 
                    stock = Stock.objects.get(cusip = row.cusip)
                except:
                    stock = Stock.objects.get(name = row.company)
                    print(row)
                
                Holding.objects.create(
                    stock = stock,
                    fund = Fund.objects.get(ticker = row.fund),
                    shares = int(row.shares),
                    market_value = float(row[6]),
                    weight = float(row[7]),
                    date = datetime.strptime(row.date, '%m/%d/%Y').replace(tzinfo=pytz.timezone('America/New_York')),
                )

if __name__ == '__main__':

    csv_path = '/Users/brianlu/side-projects/ark-etf-website/arketfdata/holdings'

    save_holding_csv(csv_path)
