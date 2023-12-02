from datetime import datetime

import aiogram
import pytz

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import executor
import time

bot = Bot(token="6858771486:AAFDx_E3EfliKMGigg9O722B7lQ1toWHuD8")
dp = Dispatcher(bot)

inline_btn_1 = InlineKeyboardButton('Ответить', callback_data='answer')
inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply(
        "Welcome to the Student Union Bot!\nWe are here to help you with your requests and complaints. Please feel free to type your query and we will do our best to assist you.")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Write me something and I will send it to the Students Council!")


@dp.callback_query_handler(func=lambda c: c.data == 'answer')
async def process_callback_button1(callback_query: types.CallbackQuery):
    global user_id
    await bot.answer_callback_query(callback_query.id)
    text = callback_query.message.text
    user_id = text[17:29]
    await bot.send_message(callback_query.from_user.id, f'Write down your answer to this question')

@dp.message_handler()
async def echo_message(msg: types.Message):
    if msg.from_user.id == 1679253464 or msg.from_user.id == 1669864103:
        print(user_id, msg.text)
        await bot.send_message(chat_id=int(user_id), text=f"Admin's answer to your question :\n{msg.text}")
        await bot.send_message(chat_id=msg.chat.id, text="Answered successfully")
    else:
        current_time = str(datetime.now(pytz.timezone('Asia/Tashkent'))) + " " + str(datetime.now().strftime("%H:%M:%S"))
        await bot.send_message(1679253464, f"New message \n"
                                           f"ID : {msg.from_user.id}\n"
                                           f"Time : {current_time}\n"
                                           f"First name : {msg.from_user.first_name}\n"
                                           f"Last name: {msg.from_user.last_name}\n"
                                           f"Username @{msg.from_user.username}\n"
                                           f"Text : {msg.text}", reply_markup=inline_kb1)
        await bot.send_message(1669864103, f"New message \n"
                                           f"ID : {msg.from_user.id}\n"
                                           f"Time : {current_time}\n"
                                           f"First name : {msg.from_user.first_name}\n"
                                           f"Last name: {msg.from_user.last_name}\n"
                                           f"Username @{msg.from_user.username}\n"
                                           f"Text : {msg.text}", reply_markup=inline_kb1)
        await bot.send_message(msg.from_user.id, "Your message was sent successfully!")





if __name__ == '__main__':
    executor.start_polling(dp)
