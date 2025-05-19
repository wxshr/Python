import requests
from bs4 import BeautifulSoup
import json
import time

def get_books():
    books = []
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    for page in range(1, 6):
        url = f"https://spa5.scrape.center/page/{page}"
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        items = soup.select('.el-card')
        for item in items:
            id_ = item.a['href'].split('/')[-1]
            name = item.select_one('h2').text.strip()
            score = item.select_one('.score')
            score = score.text.strip() if score else '0'
            cover = item.img['src']
            authors = [tag.text.strip()
                       for tag in item.select('.authors .author')]
            book = {
                "id": id_,
                "name": name,
                "authors": authors,
                "cover": cover,
                "score": score
            }
            books.append(book)
        time.sleep(1)  # 防止爬太快被封
    return books

def save_to_json(data):
    with open("books.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    book_list = get_books()
    save_to_json(book_list)
    print("前五页图书信息已保存到 books.json")
