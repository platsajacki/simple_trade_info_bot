from decimal import Decimal

from pybit.unified_trading import HTTP

from create_bot import ACCOUNT_TYPE, API_KEY, API_SECRET, NOT_TESTNET

http_session = HTTP(testnet=NOT_TESTNET, api_key=API_KEY, api_secret=API_SECRET)


def get_wallet_balance() -> str:
    balance_str = (
        http_session.get_wallet_balance(accountType=ACCOUNT_TYPE)
        ['result']['list'][0]['totalEquity']
    )
    return f'<b>{round(Decimal(balance_str), 2)} USDT</b>'
