from datetime import datetime

import aiogram
import pytz

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import executor
import time
q_id = 1
a_id = 1
CHANNEL_ID = -1002121777457
bot = Bot(token="6530826034:AAG44bwHVIrL-UaQSL1abWk35AA9hvVIkBc")
dp = Dispatcher(bot)

inline_btn_1 = InlineKeyboardButton('Answer', callback_data='answer')
inline_btn_2 = InlineKeyboardButton('Delete', callback_data='delete')
inline_kb1 = InlineKeyboardMarkup()
inline_kb1.add(inline_btn_1)
inline_kb1.add(inline_btn_2)


async def send_message(channel_id: int, text: str):
    await bot.send_message(channel_id, text)



@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply(
        "Welcome to the Student Union Bot!\nWe are here to help you with your requests and complaints. Please feel free to type your query and we will do our best to assist you.")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Write me something and I will send it to the Students Council!")


@dp.callback_query_handler(lambda c: c.data == 'answer')
async def process_callback_button1(callback_query: types.CallbackQuery):
    global q_id, user_id
    await bot.answer_callback_query(callback_query.id)
    text = callback_query.message.text
    user_info_list = list(text.split())
    user_id = user_info_list[4]
    await bot.send_message(callback_query.from_user.id, f'Write down your answer to this question')
    await send_message(CHANNEL_ID, text=f"Question number #q{q_id}:\n{callback_query.message.text}")
    q_id +=1


@dp.callback_query_handler(lambda c: c.data == 'delete')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text="Previous question was deleted successfully.\nIf you want to ban that user, use '/ban' command")



@dp.message_handler()
async def echo_message(msg: types.Message):
    global a_id
    if msg.from_user.id == 1669864103 or msg.from_user.id ==1679253464:
        await bot.send_message(chat_id=user_id, text=f"Admin's answer to your question :\n{msg.text}")
        await bot.send_message(chat_id=msg.chat.id, text="Answered successfully")
        await send_message(CHANNEL_ID, text=f"Answer number : #a{a_id}\n"
                                            f"Question number: #q{q_id-1}\n"
                                            f"Name: {msg.chat.first_name} {msg.chat.last_name}\n"
                                            f"Username : @{msg.chat.username}\n"
                                            f"Text: {msg.text}")
        a_id += 1

        return
    else:
        current_time = str(datetime.now(pytz.timezone('Asia/Tashkent'))) + " " + str(
            datetime.now().strftime("%H:%M:%S"))
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
        await bot.send_message(msg.from_user.id, f"Your message was sent successfully! ID of your question is #q{q_id}")


if __name__ == '__main__':
    executor.start_polling(dp)
