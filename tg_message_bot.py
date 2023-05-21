import telebot
import os
import time
from forbes_rss_content_parser import parse_forbes_rss

# ==============================================================================
TOKEN = ''
CHAT_ID = ''
IMAGE_FOLDER = 'images'
CATEGORIES = ['YOUR_CATEGORY_HERE']
rss_url = 'https://www.forbes.ru/newrss.xml'
# ==============================================================================
bot = telebot.TeleBot(TOKEN)


def publish_news(news):
    title = news['title']
    description = news['description']
    article_url = news['article_url']
    image_filename = news.get('image_filename') 

    message = f"<b>#Forbes</b>\n\n"
    message += f"<b>{title}</b>\n\n"
    message += f"{description}\n\n"
    message += f"<a href='{article_url}'>Читать статью</a>\n\n"
    message += "🧠 <b>MONEY</b>: Financial | Markets | " \
               "<a href='https://t.me/+azeeYWEGALRiM2Qy'>News</a>"

    if image_filename is None:
        bot.send_message(chat_id=CHAT_ID, text=message, parse_mode='HTML',
                         disable_web_page_preview=True)
    else:
        image_path = os.path.join(IMAGE_FOLDER, image_filename)

        with open(image_path, 'rb') as photo:
            bot.send_photo(chat_id=CHAT_ID, photo=photo, caption=message, parse_mode='HTML')

        os.remove(image_path)


def check_new_news():
    while True:
        latest_news = parse_forbes_rss(rss_url, CATEGORIES)

        if latest_news:
            for news in latest_news:
                publish_news(news)
        time.sleep(60) 


if __name__ == '__main__':
    check_new_news()
