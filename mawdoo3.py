import asyncio
import aiohttp
from requests import get
from bs4 import BeautifulSoup
import pyarabic.araby as araby
import re
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import json


class Mawdoo3:

    def __init__(self,chunk_length=2000):
        self.url = 'https://mawdoo3.com/'
        self.website = get(self.url).content
        self.content = BeautifulSoup(self.website, 'html.parser')
        self.categories = self.content.find_all("div", {"class": "category"})
        self.scrapped_categories = []
        self.scrapped_articles = {}
        self.articles = []
        self.get_categories()
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
        self.driver = webdriver.Chrome(options=options)
        self.chunk_length = chunk_length

    def get_categories(self):
        for category in self.categories:
            main_category = category.find_next("h2").find("span", {"class": "title"}).text
            category_dic = {"main_category": main_category, "sub_category": [sub_category["href"] for sub_category in
                                                                             category.find_next("ul").find_all("a")]}
            self.scrapped_categories.append(category_dic)
        print(self.scrapped_categories)

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

    def get_category_articles(self, main_category, category):
        url = f'https://mawdoo3.com{category}'
        print(f'{url} under scrapping . . . ')
        self.driver.get(url)
        click_more = True
        try:
            element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, 'more_results_btn')))
            counter = 1
            while click_more:
                time.sleep(10)
                print(f'{url} see more articles . . . ({counter})')
                if element.is_displayed():
                    # element.click()
                    self.driver.execute_script('arguments[0].click()', element)
                else:
                    click_more = False
                counter += 1
        except Exception as e:
            print(f'{url} Error . . . {e}')

        website = self.driver.page_source
        content = BeautifulSoup(website, 'html.parser')
        articles = content.find_all("a", {"class": "category-box"})
        if main_category in self.scrapped_articles:
            self.scrapped_articles[main_category].extend([article['href'] for article in articles])
        else:
            self.scrapped_articles[main_category] = [article['href'] for article in articles]

    def save_all_articles_title_into_file(self, file_name=f'{(int(time.time() * 1000))}_mawdoo3_article_titles.json'):
        for index, category in enumerate(self.scrapped_categories):
            main_category = category['main_category']
            for sub_category in category['sub_category']:
                print(f'scrapping main category : {main_category} -> sub category : {sub_category}')
                self.get_category_articles(main_category, sub_category)
        print(len(self.scrapped_articles))

        with open(file_name, 'w') as file:
            json.dump(self.scrapped_articles, file)

    def extract_sub_category(self, strCateg=''):
        slash_matches = [i for i, ltr in enumerate(strCateg) if ltr == '/']
        result = ''
        try:
           result = strCateg[slash_matches[0]:slash_matches[1]].strip()
        except:
           pass
        if result.find(',') != -1:
            result = result.split(',')[1].strip()
        if result.find('،') != -1:
            result = result.split('،')[1].strip()
        if result.find('/') != -1:
            result = result.split('/')[1].strip()
        return result

    async def get_target_article(self, category, title,session,index=0):
        url = f'https://mawdoo3.com{title}'
        try:
            async with session.get(url) as r:
                if r.status != 200:
                    r.raise_for_status()
                website = await r.text()
                content = BeautifulSoup(website, 'html.parser')
                article = content.find('div', {'class': 'article-text'})
                sub_category = content.find('ul', {'class': 'breadcrumbs'}).text
                sub_category = self.extract_sub_category(sub_category)

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
                try:
                    article.find('ol', {'class': 'references'}).find_previous('h2').decompose()
                    article.find('ol', {'class': 'references'}).decompose()
                except:
                    pass
                try:
                    article = article.get_text(separator=' ')
                except:
                    pass

                article = {'category': category, 'sub_category': sub_category, 'title': title, 'content': article}
                print(index,article)
                self.articles.append(article)
                if len(self.articles) == self.chunk_length:
                    with open(f'{(int(time.time() * 1000))}_mawdoo3_articles.json', 'w') as json_file:
                        json.dump(self.articles, json_file, ensure_ascii=False)
                    self.articles = []
        except Exception as e:
          print(e)

    async def save_articles_into_file(self, titles_file):
        with open(titles_file) as json_file:
            data = json.load(json_file)
            counter = 1
            category_counter = 1
            tasks = []
            total_timeout = aiohttp.ClientTimeout(total=60 * 500)
            connector = aiohttp.TCPConnector(limit=50)
            semaphore = asyncio.Semaphore(200)
            async with semaphore:
                async with aiohttp.ClientSession(timeout=total_timeout,connector=connector) as session:
                    try:
                        for category, title_list in data.items():
                            print(f'{category_counter}. {category} is under scrapping . . . ')
                            for title in title_list:
                                print(f'{counter}. {self.url}{title} scrapping article . . . ')
                                task = asyncio.create_task(self.get_target_article(category, title,session,counter))
                                tasks.append(task)
                                counter += 1
                            category_counter += 1
                        await asyncio.gather(*tasks)
                    except Exception as e:
                        with open(f'{(int(time.time() * 1000))}_mawdoo3_articles.json', 'w') as json_file:
                            json.dump(self.articles, json_file, ensure_ascii=False)
                        self.articles = []
                        print(e)

