# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urlparse
import re

class MyHTMLParser(object):

    def parser(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding="utf-8")
        new_url = self._get_new_url(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_url, new_data

    def _get_new_url(self, page_url, soup):
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r'/item/.*'))
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        data = {}
        data['url'] = page_url
        title = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find('h1')
        data['title'] = title.get_text()
        summary = soup.find('div', class_="lemma-summary")
        data['summary'] = summary.get_text()
        return data


if __name__ == "__main__":
    import requests
    url = "https://baike.baidu.com/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB"
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
    headers = {"User-Agent": user_agent}
    r = requests.get(url, headers=headers, verify=False)
    htmlParser = MyHTMLParser()
    new_url, new_data = htmlParser.parser(url, r.text)
    print new_url
    print new_data