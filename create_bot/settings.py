from os import getenv

from dotenv import load_dotenv

load_dotenv()

MYID = int(getenv('MYID', 0))
TOKEN = getenv('TOKEN', '')

BYBIT_KEY = getenv('BYBIT_KEY')
BYBIT_SECRET = getenv('BYBIT_SECRET')
NOT_TESTNET = getenv('NOT_TESTNET') != 'True'
ACCOUNT_TYPE = getenv('ACCOUNT_TYPE')

KUCOIN_KEY = getenv('KUCOIN_KEY')
KUCOIN_SECRET = getenv('KUCOIN_SECRET')
KUCOIN_PASSPHRASE = getenv('KUCOIN_PASSPHRASE')
