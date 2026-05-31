import time
import random
import requests
from bs4 import BeautifulSoup

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.76"
]

def get_top_news():
    url = "https://news.sina.com.cn/"
    headers = {
        "User-Agent": random.choice(USER_AGENTS),
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Referer": "https://www.sina.com.cn/"
    }
    time.sleep(random.uniform(1, 2))
    res = requests.get(url, headers=headers, timeout=10)
    res.raise_for_status()
    res.encoding = "utf-8"
    soup = BeautifulSoup(res.text, "html.parser")

    news_list = []
    for a in soup.select(".news-item a")[:10]:
        title = a.get_text(strip=True)
        link = a["href"]
        if title and link:
            news_list.append({"title": title, "link": link})
    return news_list

if __name__ == "__main__":
    news = get_top_news()
    for n in news:
        print(n["title"], n["link"])
