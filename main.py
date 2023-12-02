import aiogram

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor



bot = Bot(token="6637408089:AAEewGo8LALefLK9mQ9dGR8pCHnKX00WvD8")
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши мне свою жалобу или же просьбу, и я отправлю это Студенческому Совету!")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст Студенческому Совету!")


@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(1679253464, f"New message \n"
                                       f"Time : {msg.forward_date.time()}"
                                       f"First name : {msg.from_user.first_name}\n"
                                       f"Last name: {msg.from_user.last_name}\n"
                                       f"ID : {msg.from_user.id}\n"
                                       f"Username @{msg.from_user.username}\n"
                                       f"Text : {msg.text}")
    await bot.send_message(msg.from_user.id, "Успешно отправлено! Если нас заинтересует твоя идея или же проблема мы свяжемся с тобой!")


if __name__ == '__main__':
    executor.start_polling(dp)
