from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

inline_kb1 = InlineKeyboardMarkup()
inline_btn_1 = InlineKeyboardButton('ураа', callback_data='button_ura')
inline_btn_2 = InlineKeyboardButton('ааару', callback_data='button_aru')
inline_kb1.row(inline_btn_1, inline_btn_2)