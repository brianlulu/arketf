from .crawlers import *
import pandas as pd


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
    
    path = '/Users/brianlu/side-projects/ark-etf-website/arketfdata/' + trade_date + '_dailytrade.csv'

    df.to_csv(path, index= False)



    

