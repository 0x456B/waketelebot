from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

#inline_button_vk = InlineKeyboardButton('Открыть векашечку', url='https://vk.com', callback_data='button_open_vk')
#inline_kb_open_vk = InlineKeyboardMarkup().add(inline_button_vk)

button_sign_workout = KeyboardButton('🏄 Записаться на тренировку')
button_accommodation = KeyboardButton('🏘 Забронировать проживание')
button_balance_on_subscription = KeyboardButton('❓ Узнать остаток сетов на абонементе')
button_instagram = KeyboardButton('📸 Instagram')
button_public_vk = KeyboardButton('🐶 Группа Вконтакте')
button_call = KeyboardButton('📞 Позвонить')
button_cancel = KeyboardButton(text='Отмена')
markup_start_cancel = ReplyKeyboardMarkup(resize_keyboard=True).add(button_cancel)

button_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button_sign_workout)\
    .add(button_accommodation).add(button_balance_on_subscription)\
    .row(button_instagram, button_public_vk).add(button_call)
