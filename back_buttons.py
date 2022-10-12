from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

inline_kb1 = InlineKeyboardMarkup()
inline_btn_food = InlineKeyboardButton('Еда', callback_data='button_food')
inline_btn_drink = InlineKeyboardButton('Напитки', callback_data='button_drink')
inline_kb1.row(inline_btn_food, inline_btn_drink)

inline_kb2 = InlineKeyboardMarkup()
inline_btn_1st = InlineKeyboardButton('Первое', callback_data='button_food_1st')
inline_btn_2nd = InlineKeyboardButton('Второе', callback_data='button_food_2nd')
inline_btn_snak = InlineKeyboardButton('Закуски', callback_data='button_food_snak')
inline_btn_desert = InlineKeyboardButton('Десерты', callback_data='button_food_desert')
inline_btn_back = InlineKeyboardButton('Назад', callback_data='button_f_back')
inline_kb2.add(inline_btn_1st, inline_btn_2nd, inline_btn_snak, inline_btn_desert, inline_btn_back)

inline_kb3 = InlineKeyboardMarkup()
inline_btn_hot = InlineKeyboardButton('Горячие', callback_data='button_drink_hot')
inline_btn_cold = InlineKeyboardButton('Холодные', callback_data='button_drink_cold')
inline_btn_alk = InlineKeyboardButton('Алкогольные', callback_data='button_drink_alk')
inline_kb3.add(inline_btn_hot, inline_btn_cold, inline_btn_alk, inline_btn_back)

inline_kb4 = InlineKeyboardMarkup()
inline_btn_tea = InlineKeyboardButton('Чай', callback_data='button_drink_hot_tea')
inline_btn_coffe = InlineKeyboardButton('Кофе', callback_data='button_drink_hot_coffe')
inline_btn_cacao = InlineKeyboardButton('Какао', callback_data='button_drink_hot_cacao')
inline_btn_back2 = InlineKeyboardButton('Назад', callback_data='button_f_back2')
inline_kb4.add(inline_btn_tea, inline_btn_coffe, inline_btn_cacao, inline_btn_back2)

inline_kb5 = InlineKeyboardMarkup()
inline_btn_water = InlineKeyboardButton('Вода', callback_data='button_drink_cold_water')
inline_btn_juce = InlineKeyboardButton('Сок', callback_data='button_drink_cold_juce')
inline_btn_fizzy_w = InlineKeyboardButton('Газировка', callback_data='button_drink_cold_fizzy_water')
inline_kb5.add(inline_btn_water, inline_btn_juce, inline_btn_fizzy_w, inline_btn_back2)

inline_kb6 = InlineKeyboardMarkup()
inline_btn_pivo = InlineKeyboardButton('Пиво', callback_data='button_drink_alk_pivo')
inline_btn_vodka = InlineKeyboardButton('Водка', callback_data='button_drink_alk_vodka')
inline_btn_vino = InlineKeyboardButton('Вино', callback_data='button_drink_alk_vino')
inline_btn_shamp = InlineKeyboardButton('Шампанское', callback_data='button_drink_alk_shamp')
inline_kb6.add(inline_btn_pivo, inline_btn_vodka, inline_btn_vino, inline_btn_shamp, inline_btn_back2)