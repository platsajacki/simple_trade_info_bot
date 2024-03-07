import asyncio

from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from actions.execution_stream import start_execution_stream
from actions.wallet import get_wallet_balance
from create_bot import MYID, bot, dp, keyboard


@dp.message(CommandStart())
async def start(message: Message):
    """The "Start" command checks who started the work. If it is not an admin, then the client is not allowed."""
    if message.from_user and message.from_user.id == MYID:
        await message.answer('The STIB Bot activeted!', reply_markup=keyboard)
        return
    await message.answer('Access is denied!')


@dp.message(Command('balance'))
async def balance(message: Message):
    if message.from_user and message.from_user.id == MYID:
        await message.answer(get_wallet_balance(), reply_markup=keyboard)


async def main():
    """Start info-bot."""
    try:
        await asyncio.gather(dp.start_polling(bot), start_execution_stream())
    except Exception as error:
        await bot.send_message(str(error))


if __name__ in '__main__':
    asyncio.run(main())
