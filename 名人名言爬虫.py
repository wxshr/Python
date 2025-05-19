import requests
from bs4 import BeautifulSoup
import json
import time

def get_author_info(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    date = soup.select_one('.author-born-date').text
    place = soup.select_one('.author-born-location').text
    return f"{date}{place}"

def get_quotes():
    quotes = []
    base = "https://quotes.toscrape.com"
    for page in range(1, 11):
        url = f"{base}/page/{page}/"
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "html.parser")
        items = soup.select('.quote')

        for item in items:
            text = item.select_one('.text').text.strip('“”')
            author = item.select_one('.author').text
            link = item.select_one('a')['href']
            info = get_author_info(base + link)
            quotes.append({
                "名人名言": text,
                "作者": author,
                "出生日期和地点": info
            })
        time.sleep(1)
    return quotes

def save_json(data):
    with open("quotes.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    quote_list = get_quotes()
    save_json(quote_list)
    print("前十页名言已保存到 quotes.json")
