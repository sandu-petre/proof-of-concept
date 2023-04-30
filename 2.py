import urllib.request
import xml.etree.ElementTree as ET

def parse_rss_feed(url):
    with urllib.request.urlopen(url) as response:
        xml_data = response.read()

    root = ET.fromstring(xml_data)
    news_list = []
    for item in root.iter('item'):
        news = {}
        news['title'] = item.findtext('title')
        news['link'] = item.findtext('link')
        news['description'] = item.findtext('description')
        news['pubDate'] = item.findtext('pubDate')
        news_list.append(news)

    return news_list

def sort_news(news_list, sort_param):
    if sort_param == 'title_asc':
        return sorted(news_list, key=lambda x: x['title'])
    elif sort_param == 'title_desc':
        return sorted(news_list, key=lambda x: x['title'], reverse=True)
    elif sort_param == 'date_asc':
        return sorted(news_list, key=lambda x: x['pubDate'])
    elif sort_param == 'date_desc':
        return sorted(news_list, key=lambda x: x['pubDate'], reverse=True)
    else:
        return news_list

def search_news(news_list, keyword):
    return [news for news in news_list if keyword.lower() in news['title'].lower() or keyword.lower() in news['description'].lower()]

import sqlite3

def save_news_to_db(news_list):
    conn = sqlite3.connect('news.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS news
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  title TEXT,
                  link TEXT,
                  description TEXT,
                  pubDate TEXT)''')

    for news in news_list:
        c.execute('INSERT INTO news (title, link, description, pubDate) VALUES (?, ?, ?, ?)',
                  (news['title'], news['link'], news['description'], news['pubDate']))

    conn.commit()
    conn.close()

