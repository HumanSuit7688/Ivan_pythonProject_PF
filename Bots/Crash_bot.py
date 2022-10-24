import time
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

print("Выберете криптовалюту!\nИ Сделайте, ставку: Больше или Меньше...")
crypta = input()
stv = input().lower()
id = crypta
crypto = cg.get_price(ids= id , vs_currencies= 'usd')
price = crypto[id]['usd']
print(f'One {crypta} = {price} долларов')
time.sleep(35)
crypto2 = cg.get_price(ids= id , vs_currencies= 'usd')
price2 = crypto2[id]['usd']
# большем
if "больше" in stv:
    if price2 > price:
        print('Ураа, Вы победили!')
        print(f'One {crypta} = {price2} долларов')
    else:
        print("К сожалению вы проиграли")
        print(f'One {crypta} = {price2} долларов')
elif 'меньше' in stv:
    if price2 < price:
        print('Ураа, Вы победили!')
        print(f'One {crypta} = {price2} долларов')
    else:
        print("К сожалению вы проиграли")
        print(f'One {crypta} = {price2} долларов')