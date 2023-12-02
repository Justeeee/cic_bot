from datetime import datetime

import aiogram
import pytz


from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import time


bot = Bot(token="6530826034:AAFlQ-j5q0ohOc_RwKlxPwHwg0WyljSMRrQ")
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Welcome to the Student Union Bot!\nWe are here to help you with your requests and complaints. Please feel free to type your query and we will do our best to assist you.")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Write me something and I will send it to the Students Council!")


@dp.message_handler()
async def echo_message(msg: types.Message):
    current_time = str(datetime.now(pytz.timezone('Asia/Uzbekistan'))) + " " + str(datetime.now().strftime("%H:%M:%S"))
    await bot.send_message(1679253464, f"New message \n"
                                       f"Time : {current_time}"
                                       f"First name : {msg.from_user.first_name}\n"
                                       f"Last name: {msg.from_user.last_name}\n"
                                       f"ID : {msg.from_user.id}\n"
                                       f"Username @{msg.from_user.username}\n"
                                       f"Text : {msg.text}")
    await bot.send_message(1669864103, f"New message \n"
                                       f"Time : {current_time}"
                                       f"First name : {msg.from_user.first_name}\n"
                                       f"Last name: {msg.from_user.last_name}\n"
                                       f"ID : {msg.from_user.id}\n"
                                       f"Username @{msg.from_user.username}\n"
                                       f"Text : {msg.text}")
    await bot.send_message(msg.from_user.id, "Your message was sent successfully!")


if __name__ == '__main__':
    executor.start_polling(dp)
