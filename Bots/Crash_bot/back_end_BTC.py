from pycoingecko import CoinGeckoAPI
from aiogram.types import ReplyKeyboardRemove, \
    InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
cg = CoinGeckoAPI()
def crypto_crash(id, stv, price, stv_int):
    crypto2 = cg.get_price(ids=id, vs_currencies='usd')
    price2 = crypto2[id]['usd']

    if "больше" in stv:
        if price2 > price:
            result = 'Ура, вы выиграли!'
            stv_int = stv_int * 2
        else:
            result = 'К сожалению вы проиграли!'
            stv_int = 0
    elif 'меньше' in stv:
        if price2 < price:
            result = 'Ура, вы выиграли!'
            stv_int = stv_int * 2
        else:
            result = 'К сожалению вы проиграли!'
            stv_int = 0
    return result, str(stv_int)

inline_kb_st = InlineKeyboardMarkup()
inline_btn_more = InlineKeyboardButton('Больше', callback_data='button_more')
inline_btn_less = InlineKeyboardButton('Меньше', callback_data='button_less')
inline_kb_st.row(inline_btn_more, inline_btn_less)

inline_kb_ch = InlineKeyboardMarkup()
inline_btn_btc = InlineKeyboardButton('Bitcoin', callback_data='button_btc')
inline_btn_eth = InlineKeyboardButton('Ethereum', callback_data='button_eth')
inline_btn_bnb = InlineKeyboardButton('BNB', callback_data='button_bnb')
inline_kb_ch.row(inline_btn_btc, inline_btn_eth, inline_btn_bnb)

inline_kb_st_int = InlineKeyboardMarkup()
inline_btn_100c = InlineKeyboardButton('100 монет', callback_data='button_100c')
inline_btn_200c = InlineKeyboardButton('200 монет', callback_data='button_200c')
inline_btn_500c = InlineKeyboardButton('500 монет', callback_data='button_500c')
inline_btn_1000c = InlineKeyboardButton('1000 монет', callback_data='button_1000c')
inline_kb_st_int.row(inline_btn_100c, inline_btn_200c, inline_btn_500c, inline_btn_1000c)