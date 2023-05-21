import requests
from bs4 import BeautifulSoup
import hashlib
import os

# ==============================================================================
rss_url = 'https://www.forbes.ru/newrss.xml'
processed_links_file = 'processed_links.txt'
categories = ['ADD_YOUR_CATEGORY']
# ==============================================================================

def get_link_hash(link):
    """"""
    link_hash = hashlib.sha1(link.encode()).hexdigest()
    return link_hash


def parse_forbes_rss(rss_url, categories):
    response = requests.get(rss_url)
    rss_content = response.text
    soup = BeautifulSoup(rss_content, 'xml')

    processed_links = []
    if os.path.exists(processed_links_file):
        with open(processed_links_file, 'r') as f:
            processed_links = f.read().splitlines()

    parsed_items = []

    items = soup.find_all('item')
    for item in items:
        title = item.find('title').text.strip()
        description = item.find('description').text.strip()
        article_url = item.find('link').text.strip()
        categories_tags = item.find_all('category')

        if article_url in processed_links:
            continue  

        article_categories = [category.text.strip() for category in categories_tags]
        if not any(category in article_categories for category in categories):
            continue 

        image_url = None
        enclosure = item.find('enclosure')
        if enclosure and 'url' in enclosure.attrs:
            image_url = enclosure['url']

        if image_url:
            image_filename = download_image(image_url)
        else:
            image_filename = None

        article_data = {
            'title': title,
            'description': description,
            'article_url': article_url,
            'image_filename': image_filename,
            'categories': article_categories
        }
        parsed_items.append(article_data)

        processed_links.append(article_url)

    with open(processed_links_file, 'w') as f:
        f.write('\n'.join(processed_links))

    return parsed_items


def download_image(image_url):
    """"""
    response = requests.get(image_url)
    image_content = response.content
    image_extension = os.path.splitext(image_url)[1]
    image_filename = f'{get_link_hash(image_url)}{image_extension}'

    os.makedirs('images', exist_ok=True)

    image_path = os.path.join('images', image_filename)
    with open(image_path, 'wb') as f:
        f.write(image_content)

    return image_filename
