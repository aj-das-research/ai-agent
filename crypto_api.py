import os
import requests

class CryptoAPI:
    def __init__(self):
        self.api_key = os.getenv('CRYPTO_API_KEY')
        self.base_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
        self.headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': self.api_key,
        }
        self.parameters = {
            'symbol': 'BTC',
            'convert': 'USD'
        }

    def get_bitcoin_price(self):
        try:
            response = requests.get(self.base_url, headers=self.headers, params=self.parameters)
            data = response.json()
            price = data['data']['BTC']['quote']['USD']['price']
            return round(price, 2)
        except Exception as e:
            print(f"Error fetching Bitcoin price: {e}")
            return None
