from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

menu_kb = ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = KeyboardButton('Menu 1')
btn2 = KeyboardButton('2 Menu')
btn3 = KeyboardButton('Me 3 nu')
btn4 = KeyboardButton('nu 4 Me')
menu_kb.row(btn1, btn2)
menu_kb.row(btn3, btn4)