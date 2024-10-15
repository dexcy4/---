import json
import requests
from config import keys

class error(Exception):
    pass

class CruptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):

        if quote == base:
            raise error(f'Невозможно перевести одинаковые валюты!')

        try:
            quote_t = keys[quote]
        except KeyError:
            raise error(f'Не удалось обработать валюту {quote}')

        try:
            base_t = keys[base]
        except KeyError:
            raise error(f'Не удалось обработать валюту {base}')

        try:
            amount_t = float(amount)
        except ValueError:
            raise error(f'Не удалось обработать колл-во {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_t}&tsyms={base_t}')
        total_base = json.loads(r.content)[keys[base]]

        return total_base