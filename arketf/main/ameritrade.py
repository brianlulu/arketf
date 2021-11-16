import requests

apikey = 'COJC2C8MBNZRPM0OMMCME18KD381WWTI'

url = 'https://api.tdameritrade.com/v1/marketdata/quotes'

payload = {
    'apikey': apikey,
    'symbol': ['AAPL','MSFT']
}

result = requests.get(url, params=payload)

if __name__ == '__main__':
    print(result.json())
    
    