import telebot
import requests

API_TOKEN = '5252544232:AAEdNsKto4n3cZv_g_QLwcL_rl3JbeAreUk'
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands={'start'})
def start(message):
    bot.send_message(message.chat.id, '<b>Введите ip адрес</b>',parse_mode='html')

@bot.message_handler(content_types=['text'])

@bot.message_handler({''})
def get_info_by_ip(message):
    try:
        global text
        text = message.text
        ip = message.text
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()

        data = {
            '[IP]': response.get('query'),
            '[Int prov]': response.get('isp'),
            '[Org]': response.get('org'),
            '[Country]': response.get('country'),
            '[Region Name]': response.get('regionName'),
            '[City]': response.get('city'),
            '[ZIP]': response.get('zip'),
            '[Time zone]': response.get('timezone'),
            '[Lat]': response.get('lat'),
            '[Lon]': response.get('lon'),
                                         }


        bot.send_message(message.chat.id,f'[IP]: { response.get("query")}' "\n" f'[Int prov]: {response.get("isp")}'"\n" f'[Org]: {response.get("org")}'"\n" f'[Country]: {response.get("country")}'"\n" f'[Region Name]: {response.get("regionName")}'"\n" f'[City]: {response.get("city")}'    "\n"f'[Time zone]: {response.get("timezone")}'    "\n" f'[ZIP]: {response.get("zip")}'    "\n" f'[Lat]: {response.get("lat")}'   "\n" f'[Lon]: {response.get("lon")}')
        bot.send_location(message.chat.id,response.get('lat'),response.get('lon'))



    except requests.exceptions.ConnectionError:
        bot.send_message(message.chat.id,'[!] Please check your connection!')

    except Exception as e:
        bot.send_message(message.chat.id, 'Неверный ip адрес, введите заново! ')


bot.polling(none_stop=True)

