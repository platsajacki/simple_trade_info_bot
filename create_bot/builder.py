from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from create_bot.settings import TOKEN

bot: Bot = Bot(TOKEN, parse_mode='HTML')
dp: Dispatcher = Dispatcher(storage=MemoryStorage())

keyboard = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text='/balance')]],
    resize_keyboard=True,
)
