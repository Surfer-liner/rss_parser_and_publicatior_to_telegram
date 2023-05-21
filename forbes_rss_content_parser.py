import requests
from bs4 import BeautifulSoup
import hashlib
import os

# ==============================================================================
rss_url = 'https://www.forbes.ru/newrss.xml'
processed_links_file = 'processed_links.txt'
categories = ['Инвестиции', 'Миллиардеры', 'Бизнес', 'Финансы', 'Технологии',
              'Карьера и свой бизнес']
# ==============================================================================

def get_link_hash(link):
    """Возвращает хеш ссылки"""
    link_hash = hashlib.sha1(link.encode()).hexdigest()
    return link_hash


def parse_forbes_rss(rss_url, categories):
    response = requests.get(rss_url)
    rss_content = response.text
    soup = BeautifulSoup(rss_content, 'xml')

    # Проверка наличия файла с обработанными ссылками
    processed_links = []
    if os.path.exists(processed_links_file):
        with open(processed_links_file, 'r') as f:
            processed_links = f.read().splitlines()

    parsed_items = []

    # Парсинг каждого элемента (статьи) в RSS-ленте
    items = soup.find_all('item')
    for item in items:
        # Извлечение заголовка, описания, ссылки на статью и категории
        title = item.find('title').text.strip()
        description = item.find('description').text.strip()
        article_url = item.find('link').text.strip()
        categories_tags = item.find_all('category')

        # Проверка наличия ссылки на статью в списке обработанных ссылок
        if article_url in processed_links:
            continue  # Пропускаем уже обработанную ссылку

        # Извлечение категорий и проверка на их наличие в списке выбранных категорий
        article_categories = [category.text.strip() for category in categories_tags]
        if not any(category in article_categories for category in categories):
            continue  # Пропускаем статью, если нет выбранных категорий

        # Получение ссылки на изображение из элемента enclosure (если доступно)
        image_url = None
        enclosure = item.find('enclosure')
        if enclosure and 'url' in enclosure.attrs:
            image_url = enclosure['url']

        # Сохранение изображения (если доступно)
        if image_url:
            image_filename = download_image(image_url)
        else:
            image_filename = None

        # Создание словаря с данными статьи
        article_data = {
            'title': title,
            'description': description,
            'article_url': article_url,
            'image_filename': image_filename,
            'categories': article_categories
        }
        parsed_items.append(article_data)

        # Добавление ссылки на статью в список обработанных ссылок
        processed_links.append(article_url)

    # Сохранение списка обработанных ссылок в файл
    with open(processed_links_file, 'w') as f:
        f.write('\n'.join(processed_links))

    return parsed_items


def download_image(image_url):
    """Скачивает изображение по указанной ссылке и возвращает имя сохраненного файла"""
    response = requests.get(image_url)
    image_content = response.content
    image_extension = os.path.splitext(image_url)[1]
    image_filename = f'{get_link_hash(image_url)}{image_extension}'

    # Создание папки для хранения изображений (если не существует)
    os.makedirs('images', exist_ok=True)

    # Сохранение изображения
    image_path = os.path.join('images', image_filename)
    with open(image_path, 'wb') as f:
        f.write(image_content)

    return image_filename
