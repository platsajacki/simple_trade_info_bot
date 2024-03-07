import asyncio
from concurrent.futures import ThreadPoolExecutor
from functools import partial
from typing import Any

from pybit.unified_trading import WebSocket

from create_bot import API_KEY, API_SECRET, MYID, NOT_TESTNET, bot
from create_bot.utils import handle_message_in_thread


def get_text_execution(data: dict[str, Any]):
    return (
        '<b>{symbol} - {side}</b>\n'
        'Price: <b>{execPrice}</b>\n'
        'Asset volume: <b>{execQty}</b>\n'
    ).format(**data)


async def handle_message(msg: dict[str, Any], main_loop: asyncio.AbstractEventLoop) -> None:
    for data in msg['data']:
        if data['category'] == 'spot':
            asyncio.run_coroutine_threadsafe(
                bot.send_message(text=get_text_execution(data), chat_id=MYID), main_loop
            )


async def start_execution_stream():
    ws = WebSocket(testnet=NOT_TESTNET, api_key=API_KEY, api_secret=API_SECRET, channel_type='private')
    with ThreadPoolExecutor() as executor:
        try:
            loop = asyncio.get_event_loop()
            await loop.run_in_executor(
                executor,
                ws.execution_stream,
                partial(handle_message_in_thread, coro=handle_message, main_loop=loop),
            )
        except Exception as error:
            await bot.send_message(text=str(error), chat_id=MYID)
