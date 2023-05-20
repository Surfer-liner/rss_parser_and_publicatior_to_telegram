# import feedparser
# import telegram
# import time
#
# def parse_rss(url):
#     # Используем библиотеку feedparser для парсинга RSS-ленты
#     feed = feedparser.parse(url)
#     # Проходим по каждому элементу (посту) в ленте
#     entries = []
#     for entry in feed.entries:
#         title = entry.title
#         link = entry.link
#         content = entry.content[0].value if 'content' in entry else entry.summary
#         image = entry.image if 'image' in entry else None
#         # Создаем словарь с данными новости
#         news_entry = {
#             'title': title,
#             'link': link,
#             'content': content,
#             'image': image
#         }
#         entries.append(news_entry)
#     return entries
#
#
# def post_to_telegram(chat_id, entries):
#     # Используем Telegram Bot API для отправки сообщения в Telegram
#     # Замените 'YOUR_BOT_TOKEN' на токен вашего бота в Telegram
#     bot_token = '5964334978:AAFCFR2Ea2yTNc4bVGcWi2ouihJY4d_X9ss'
#     # Создаем экземпляр бота
#     bot = telegram.Bot(token=bot_token)
#     # Отправляем каждую новость в отформатированном виде
#     for entry in entries:
#         title = entry['title']
#         content = entry['content']
#         link = entry['link']
#         image = entry['image']
#         # Формируем текст сообщения с заголовком, содержимым и ссылкой новости
#         message_text = f"<b>{title}</b>\n\n{content}\n\n{link}"
#         # Если доступно изображение, добавляем его к сообщению
#         if image:
#             message_text += f"\n\n{image}"
#         # Отправляем сообщение с разметкой HTML
#         bot.send_message(chat_id=chat_id, text=message_text, parse_mode=telegram.ParseMode.HTML)
#         # Обработка ответа, проверка успешности отправки и другие действия
#         # ...
# # Задаем URL RSS-ленты и ID чата или группы в Telegram
# rss_url = "https://www.forbes.ru/rss/all.xml"
# telegram_chat_id = "-1001638342340"
#
# while True:
#     entries = parse_rss(rss_url)
#     post_to_telegram(telegram_chat_id, entries)
#     time.sleep(60)







#
# import feedparser
# import telegram
# # ==============================================================================
# bot_token  = '5964334978:AAFCFR2Ea2yTNc4bVGcWi2ouihJY4d_X9ss'
# telegram_chat_id = '-1001638342340'
# rss_url = 'https://www.forbes.ru/newrss.xml'
# # ==============================================================================
# def fetch_news():
#     # Загрузка и парсинг RSS-ленты
#     feed = feedparser.parse(rss_url)
#     # Получение списка новостей из RSS-ленты
#     entries = feed.entries
#     return entries
#
#
# def send_news():
#     # Создание экземпляра бота
#     bot = telegram.Bot(token=bot_token)
#     # Получение списка новостей
#     news_list = fetch_news()
#     for news in news_list:
#         title = news.title
#         link = news.link
#         content = news.content[0].value if 'content' in news else news.summary
#         image = news.image if 'image' in news else None
#         # Создаем словарь с данными новости
#         news_entry = {
#             'title': title,
#             'link': link,
#             'content': content,
#             'image': image
#         }
#         news_entry.append(news)
#
#         message = f"<b>{title}</b>\n\n{content}\n\n{link}"
#         # Если доступно изображение, добавляем его к сообщению
#         if image:
#             message += f"\n\n{image}"
#         # Отправляем сообщение с разметкой HTML
#         bot.send_message(chat_id=telegram_chat_id, text=message,
#                          parse_mode=telegram.ParseMode.HTML)
#
#
#         # Формирование текста сообщения
#         # message = f'<b>{title}</b>\n\n{link}'
#
#         # Отправка сообщения
#         # bot.send_message(chat_id=telegram_chat_id, text=message,
#         #                  parse_mode=telegram.ParseMode.HTML)
#
# # Вызов функции для отправки новостей
# send_news()





#
# import time
# import feedparser
# import telegram
#
#
# def parse_rss(url):
#     # Используем библиотеку feedparser для парсинга RSS-ленты
#     feed = feedparser.parse(url)
#     # Проходим по каждому элементу (посту) в ленте
#     for entry in feed.entries:
#         title = entry.title
#         link = entry.link
#         # Обработка полученных данных, например, сохранение в базу данных или другие действия
#         # ...
#
#
# def post_to_telegram(chat_id, title, content):
#     # Используем Telegram Bot API для отправки сообщения в Telegram
#     # Замените 'YOUR_BOT_TOKEN' на токен вашего бота в Telegram
#     bot_token = '5964334978:AAFCFR2Ea2yTNc4bVGcWi2ouihJY4d_X9ss'
#     # Создаем экземпляр бота
#     bot = telegram.Bot(token=bot_token)
#     # Формируем текст сообщения с заголовком и содержимым новости
#     message_text = f"<b>{title}</b>\n\n{content}"
#     # Отправляем сообщение с разметкой HTML
#     bot.send_message(chat_id=chat_id, text=message_text, parse_mode=telegram.ParseMode.HTML)
#     # Обработка ответа, проверка успешности отправки и другие действия
#     # ...
#
# def monitor_rss_feed(url, chat_id):
#     while True:
#         # Получаем данные из RSS-ленты
#         feed = feedparser.parse(url)
#         # Парсим новые посты и публикуем их
#         for entry in feed.entries:
#             # Проверяем, был ли этот пост уже опубликован
#             # ...
#             # Если новый пост, публикуем его в Telegram
#             message = f"{entry.title}\n{entry.link}"
#             post_to_telegram(chat_id, message)
#             # Помечаем пост как опубликованный
#             # ...
#         # Ждем определенный промежуток времени перед следующей проверкой
#         time.sleep(60)  # Например, проверяем каждую минуту
# # Задаем URL RSS-ленты и ID чата или группы в Telegram
# rss_url = "https://www.forbes.ru/rss/all.xml"
# telegram_chat_id = "-1001638342340"
# # Запускаем мониторинг RSS-ленты
# monitor_rss_feed(rss_url, telegram_chat_id)

#         https://www.forbes.ru/newrss.xml




# import feedparser
# import requests
# from io import BytesIO
# from PIL import Image
#
#
# def parse_forbes_rss(rss_url):
#     feed = feedparser.parse(rss_url)
#     items = []
#
#     for entry in feed.entries:
#         title = entry.title
#         content = entry.description
#         link = entry.link
#         image_url = None
#
#         if 'media_content' in entry and len(entry.media_content) > 0:
#             image_url = entry.media_content[0]['url']
#
#         if image_url is not None:
#             response = requests.get(image_url)
#             if response.status_code == 200:
#                 image_data = response.content
#                 image = Image.open(BytesIO(image_data))
#             else:
#                 image = None
#         else:
#             image = None
#
#         item = {
#             'title': title,
#             'content': content,
#             'link': link,
#             'image': image
#         }
#
#         items.append(item)
#
#     return items
#
#
# # Пример использования
# rss_url = 'https://www.forbes.ru/newrss.xml'
# parsed_items = parse_forbes_rss(rss_url)
#
# for i, item in enumerate(parsed_items, 1):
#     print('Заголовок:', item['title'])
#     print('Контент:', item['content'])
#     print('Ссылка:', item['link'])
#     if item['image'] is not None:
#         image_filename = f'image_{i}.jpg'
#         item['image'].save(image_filename)
#         print('Изображение сохранено в файл:', image_filename)
#     print('-----------------------------------')
import requests
from bs4 import BeautifulSoup
import urllib.parse
import os
import base64
from PIL import Image
from io import BytesIO
import uuid


def parse_forbes_rss(rss_url):
    response = requests.get(rss_url)
    rss_content = response.text
    soup = BeautifulSoup(rss_content, 'html.parser')
    parsed_items = []

    # Парсинг каждого элемента (статьи) в RSS-ленте
    items = soup.find_all('item')
    print(items)
    for item in items:
        # Извлечение заголовка, описания и ссылки на статью
        title = item.find('title').text.strip()
        description = item.find('description').text.strip()
        article_url = item.find('link').text.strip()

        # Получение ссылки на изображение из элемента enclosure (если доступно)
        image_url = None
        enclosure = item.find('enclosure')
        if enclosure and 'url' in enclosure.attrs:
            image_url = enclosure['url']

        # Проверка наличия ссылки на изображение
        if image_url:
            # Сохранение изображения
            response = requests.get(image_url)
            if response.ok:
                image_data = response.content

                # Генерация уникального имени файла для сохранения изображения
                filename = f"image_{uuid.uuid4().hex}.png"

                # Сохранение изображения
                with open(filename, 'wb') as f:
                    f.write(image_data)

                print(f"Сохранено изображение: {filename}")

        # Создание словаря с данными статьи
        article_data = {
            'title': title,
            'description': description,
            'article_url': article_url,
            'image_url': image_url
        }
        parsed_items.append(article_data)

    return parsed_items


# Пример использования
rss_url = 'https://www.forbes.ru/newrss.xml'
parsed_items = parse_forbes_rss(rss_url)
print(parsed_items)



# -1001638342340
# 5964334978:AAFCFR2Ea2yTNc4bVGcWi2ouihJY4d_X9ss

# https://www.forbes.ru/newrss.xml