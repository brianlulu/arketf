import pandas as pd
from .models import *
import yfinance as yf
from datetime import datetime

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
        if Stock.objects.filter(cusip = row.CUSIP).exists():

            Trade.objects.create(
                stock = Stock.objects.get(cusip = row.CUSIP),
                date = datetime.strptime(row.Date, '%m/%d/%Y'),
                direction = row.Direction,
                shares = int(row.Shares.replace(',', '')),
                fund = Fund.objects.get(ticker = row.Fund), #TODO: if fund does not exist create one?
                etf_percent = float(row[8])
            )

        else:
            
            print('Creating ' + row.Ticker + ' Stock Object!')
            stock_info = yf.Ticker(row.Ticker).info
            Stock.objects.create(
                name = row.Company, 
                ticker = row.Ticker,
                price = stock_info.get('previousClose'),
                market_cap = stock_info.get('marketCap'),
                cusip = row.CUSIP
                )

            Trade.objects.create(
                stock = Stock.objects.get(cusip = row.CUSIP),
                date = datetime.strptime(row.Date, '%m/%d/%Y'),
                direction = row.Direction,
                shares = int(row.Shares.replace(',', '')),
                fund = Fund.objects.get(ticker = row.Fund), #TODO: if fund does not exist create one?
                etf_percent = float(row[8])
            )

if __name__ == '__main__':

    csv_path = '/Users/brianlu/side-projects/ark-etf-website/arketfdata/03-25-2021_dailytrade.csv'

    save_to_db(csv_path)