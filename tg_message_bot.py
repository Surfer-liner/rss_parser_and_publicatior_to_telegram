import telebot
import os
import time
from forbes_rss_content_parser import parse_forbes_rss

# ==============================================================================
TOKEN = '5964334978:AAFCFR2Ea2yTNc4bVGcWi2ouihJY4d_X9ss'
CHAT_ID = '-1001661936464'
IMAGE_FOLDER = 'images'
CATEGORIES = ['Инвестиции', 'Миллиардеры', 'Бизнес', 'Финансы', 'Технологии', 'Карьера и свой бизнес']
rss_url = 'https://www.forbes.ru/newrss.xml'
# ==============================================================================
bot = telebot.TeleBot(TOKEN)


def publish_news(news):
    title = news['title']
    description = news['description']
    article_url = news['article_url']
    image_filename = news.get('image_filename')  # Получение имени файла изображения, если оно есть

    # Формирование текста сообщения
    message = f"<b>#Forbes</b>\n\n"
    message += f"<b>{title}</b>\n\n"
    message += f"{description}\n\n"
    message += f"<a href='{article_url}'>Читать статью</a>\n\n"
    message += "🧠 <b>MONEY</b>: Financial | Markets | " \
               "<a href='https://t.me/+azeeYWEGALRiM2Qy'>News</a>"

    # Отправка сообщения без изображения, если его нет
    if image_filename is None:
        bot.send_message(chat_id=CHAT_ID, text=message, parse_mode='HTML',
                         disable_web_page_preview=True)
    else:
        # Полный путь к файлу изображения
        image_path = os.path.join(IMAGE_FOLDER, image_filename)

        # Отправка сообщения с изображением
        with open(image_path, 'rb') as photo:
            bot.send_photo(chat_id=CHAT_ID, photo=photo, caption=message, parse_mode='HTML')

        # Удаление изображения
        os.remove(image_path)


def check_new_news():
    while True:
        # Получение последних новостей из модуля парсера
        latest_news = parse_forbes_rss(rss_url, CATEGORIES)

        if latest_news:
            for news in latest_news:
                publish_news(news)
        time.sleep(60)  # Интервал проверки новых новостей (в секундах)


if __name__ == '__main__':
    check_new_news()


# TOKEN = '5964334978:AAFCFR2Ea2yTNc4bVGcWi2ouihJY4d_X9ss'
# CHAT_ID = '-1001638342340'

#     message = f"<a href='{article_url}'>Forbes</a>\n\n"
#     message += f"<b>{title}</b>\n\n"
#     message += f"{description}\n\n"
#     message += "🧠 MONEY: Financial | Markets | News"
#     message += f" (<a href='https://t.me/+azeeYWEGALRiM2Qy'>News</a>)"