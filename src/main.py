import logging
import gspread
import keyboard as kb

import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode
from aiogram.utils import executor
from oauth2client.service_account import ServiceAccountCredentials
from config import TOKEN

# Global variable for TOKEN etc...
SCOPE = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
# Need file creds.json from google API
CREDS = ServiceAccountCredentials.from_json_keyfile_name('creds.json', SCOPE)


# Open google sheets
client = gspread.authorize(CREDS)
sheet = client.open('abon').sheet1

API_TOKEN = TOKEN
bot = Bot(token=API_TOKEN)

# Use storage and logging
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
logging.basicConfig(level=logging.INFO)


class Form(StatesGroup):
    number_subscriptions = State()


@dp.message_handler(text='Записаться на тренировку')
async def sign_workout(message: types.Message):
    pass


@dp.message_handler(text='Забронировать проживание')
async def accommodation(message: types.Message):
    pass


@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    await message.reply("Добро пожаловать!", reply_markup=kb.button_markup)


@dp.message_handler(text='Узнать остаток сетов на абонементе')
async def cmd_start(message: types.Message):
    await Form.number_subscriptions.set()
    await message.reply("Введите номер абонемента:", reply_markup=kb.button_markup)


@dp.message_handler(state=Form.number_subscriptions)
async def get_number_subscription(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number_subscriptions'] = message.text

    data_table = sheet.get_all_records()

    for subscription in data_table:
        if int(subscription['Номер абона']) == int(data['number_subscriptions']):
            await bot.send_message(
                message.chat.id,
                md.text(
                    md.text('По абонементу №', md.bold(subscription['Номер абона']),
                            ' осталось ', md.bold(subscription['Количество сэтов']), 'сетов',
                            # md.bold(subscription['Color'])
                            )),
                # reply_markup=markup,
                parse_mode=ParseMode.MARKDOWN,
            )


@dp.message_handler(text='Instagram')
async def get_to_instagram(message: types.Message):
    pass


@dp.message_handler(text='Группа Вконтакте')
async def get_to_public_vk(message: types.Message):
    pass


@dp.message_handler(text='Позвонить')
async def call_to_admin(message: types.Message):
    pass


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
