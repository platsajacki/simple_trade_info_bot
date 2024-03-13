from decimal import Decimal

from kucoin.client import Client
from pybit.unified_trading import HTTP

from create_bot import ACCOUNT_TYPE, BYBIT_KEY, BYBIT_SECRET, KUCOIN_KEY, KUCOIN_PASSPHRASE, KUCOIN_SECRET, NOT_TESTNET

bybit_http = HTTP(testnet=NOT_TESTNET, api_key=BYBIT_KEY, api_secret=BYBIT_SECRET)
kucoin_http = Client(api_key=KUCOIN_KEY, api_secret=KUCOIN_SECRET, passphrase=KUCOIN_PASSPHRASE)


def get_kucoin_wallet_balance() -> Decimal:
    balance = Decimal('0')
    for coin in kucoin_http.get_accounts():
        response = kucoin_http.get_ticker(f'{coin['currency']}-USDT')
        if response:
            balance += Decimal(response['price']) * Decimal(coin['balance'])
    return round(balance, 2)


def get_bybit_wallet_balance() -> Decimal:
    balance_str = (
        bybit_http.get_wallet_balance(accountType=ACCOUNT_TYPE)
        ['result']['list'][0]['totalEquity']
    )
    return round(Decimal(balance_str), 2)
