from requests import get
from bs4 import BeautifulSoup
import pyarabic.araby as araby
import re
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


class Mawdoo3():

    def __init__(self):
        self.url = 'https://mawdoo3.com/'
        self.website = get(self.url).content
        self.content = BeautifulSoup(self.website, 'html.parser')
        self.categories = self.content.find_all("div", {"class": "category"})
        self.scrapped_categories = []
        self.scrapped_articles = []

    def proccess_data(self, data):
        arabic_alpha_unicodes = ['\u0627', '\u0628', '\u0622', '\u062a', '\u062b', '\u062c', '\u062d', '\u062e',
                                 '\u062f', '\u0630',
                                 '\u0631', '\u0632', '\u0633', '\u0634', '\u0635', '\u0636', '\u0637', '\u0638',
                                 '\u0639',
                                 '\u063a', '\u0641', '\u0642', '\u0643', '\u06a9', '\u0644', '\u0645', '\u0646',
                                 '\u0648',
                                 '\u0629', '\u0647', '\u064a', '\u0621', '\u0649', '\u0623', '\u0624', '\u0625',
                                 '\u0626']
        data = re.sub(' +', ' ', data)  # to remove any multi spaces
        data = araby.strip_tashkeel(data)  # to remove tashkeel
        patterns_regex = '(' + '|'.join(arabic_alpha_unicodes) + ')'
        data = re.sub(f'[^{patterns_regex}^\s]', '',
                      data)  # to remove any character that is not in arabic alphabetic system
        data = re.sub('(آ|إ|أ)', 'ا', data)  # normalize hamzah
        data = re.sub('\u0629', 'ه', data)  # sub tah with hah
        for alph in arabic_alpha_unicodes:  # remove duplicate letter more than 2
            data = re.sub(f'({alph})' + '{3,}', alph, data)
        data = '\n'.join([re.sub(' +', ' ', line) for line in data.split('\n') if line != ''])
        return data.strip()

    def get_categories(self):
        for category in self.categories:
            for category_item in category.find_all('li'):
                if not category_item.find('a')['href'].startswith('http'):
                    self.scrapped_categories.append(category_item.find('a')['href'])

    def get_category_articles(self, title):
        url = f'https://mawdoo3.com{title}'
        print(f'Category url : {url}')
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
        options = webdriver.ChromeOptions()
        options.headless = True
        options.add_argument(f'user-agent={user_agent}')
        options.add_argument("--window-size=1920,1080")
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--allow-running-insecure-content')
        options.add_argument("--disable-extensions")
        options.add_argument("--proxy-server='direct://'")
        options.add_argument("--proxy-bypass-list=*")
        options.add_argument("--start-maximized")
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--no-sandbox')
        driver = webdriver.Chrome(options=options)
        driver.get(url)

        while True:
            try:
                see_more_btn = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.ID, 'more_results_btn')))
                see_more_btn.click()
                time.sleep(2)
            except:
                break
        website = driver.page_source
        content = BeautifulSoup(website, 'html.parser')
        articles = content.find_all("a", {"class": "category-box"})
        self.scrapped_articles.extend([article['href'] for article in articles])
        driver.close()

    def save_all_articles_title_into_file(self, file_name=f'{(int(time.time() * 1000))}_mawdoo3_article_titles.txt'):
        self.get_categories()
        for category in self.scrapped_categories:
            self.get_category_articles(category)
        articles_file = open(file_name, 'a')
        articles_file.write(',\n'.join(self.scrapped_articles))
        articles_file.close()

    def get_target_article(self, title):
        url = f'https://mawdoo3.com{title}'
        website = get(url).content
        content = BeautifulSoup(website, 'html.parser')
        article = content.find('div', {'class': 'article-text'})
        try:
            article.find('div', {'class': 'printfooter'}).decompose()
        except:
            pass
        try:
            article.find('ul', {'class': 'related-articles-list1'}).decompose()
        except:
            pass
        try:
            article.find('div', {'class': 'toc'}).decompose()
        except:
            pass
        try:
            article.find('div', {'class': 'feedback-feature'}).decompose()
        except:
            pass
        try:
            article.find('div', {'id': 'feedback-yes-option'}).decompose()
        except:
            pass
        try:
            article.find('div', {'id': 'feedback-no-option'}).decompose()
        except:
            pass
        try:
            article.find('div', {'id': 'feedback-thanks-msg'}).decompose()
        except:
            pass
        article_category = content.find_all('span', {'itemprop': 'name'})
        if len(article_category) < 2:
            print('Error no category found')
            return
        article_text = self.proccess_data(data=article.text)
        self.scrapped_articles.append(f'{article_category[1].text}|{article_text}')


    def save_articles_into_file(self, file_name=f'{(int(time.time() * 1000))}_mawdoo3_articles.txt'):
        articles_title = open('mawdoo3_all_article_titles.txt').read()
        articles_title_list = articles_title.split(',')
        for index, title in enumerate(articles_title_list):
            print(f'{index + 1}. {title.strip()}')
            self.get_target_article(title.strip())
        articles_file = open(file_name, 'a')
        articles_file.write(',\n'.join(self.scrapped_articles))
        articles_file.close()

    def save_all_articles_into_file(self, file_name=f'{(int(time.time() * 1000))}_mawdoo3_articles.txt'):
        self.get_categories()
        for index, category in enumerate(self.scrapped_categories):
            print(f'Reading category number : {index + 1} of {len(self.scrapped_categories)}')
            for index, article in enumerate(self.get_category_articles(category)):
                print(f'Reading article number : {index + 1}')
                self.scrapped_articles.append(f'{category}|{article}|{self.get_target_article(article)}')
        print(f'Total articles read is : {len(self.scrapped_articles)}')
        file = open(file_name, 'w')
        file.write(',\n'.join(self.scrapped_articles))
        file.close()
