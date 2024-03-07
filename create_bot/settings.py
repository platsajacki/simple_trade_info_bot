from os import getenv

from dotenv import load_dotenv

load_dotenv()

MYID = int(getenv('MYID', 0))
TOKEN = getenv('TOKEN', '')
API_KEY = getenv('API_KEY')
API_SECRET = getenv('API_SECRET')
NOT_TESTNET = getenv('NOT_TESTNET') != 'True'
ACCOUNT_TYPE = getenv('ACCOUNT_TYPE')
