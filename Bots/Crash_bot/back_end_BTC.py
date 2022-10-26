import time
from pycoingecko import CoinGeckoAPI
from aiogram.types import ReplyKeyboardRemove, \
    InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup

cg = CoinGeckoAPI()

def crypto_crash(id, stv):
    crypto = cg.get_price(ids=id, vs_currencies='usd')
    price = crypto[id]['usd']
    prc_for_comp = price * 100

    time.sleep(35)

    crypto2 = cg.get_price(ids=id, vs_currencies='usd')
    price2 = crypto2[id]['usd']
    prc_for_comp2 = price2 * 100

    if "больше" in stv:
        if prc_for_comp2 > prc_for_comp:
            result = 'Ура, вы выиграли!'
        else:
            result = 'К сожалению вы проиграли!'
    elif 'меньше' in stv:
        if prc_for_comp2 < prc_for_comp:
            result = 'Ура, вы выиграли!'
        else:
            result = 'К сожалению вы проиграли!'

    return result

inline_kb_st = InlineKeyboardMarkup()
inline_btn_more = InlineKeyboardButton('Больше', callback_data='button_more')
inline_btn_less = InlineKeyboardButton('Меньше', callback_data='button_less')
inline_kb_st.row(inline_btn_more, inline_btn_less)

inline_kb_ch = InlineKeyboardMarkup()
inline_btn_btc = InlineKeyboardButton('Bitcoin', callback_data='button_btc')
inline_btn_eth = InlineKeyboardButton('Ethereum', callback_data='button_ef')
inline_btn_bnb = InlineKeyboardButton('BNB', callback_data='button_bnb')
inline_kb_ch.row(inline_btn_btc, inline_btn_eth, inline_btn_bnb)