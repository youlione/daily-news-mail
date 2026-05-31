import time
import random
import requests
from bs4 import BeautifulSoup

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
]

def get_top_news():
    try:
        url = "https://news.sina.com.cn/"
        headers = {
            "User-Agent": random.choice(USER_AGENTS),
            "Accept-Language": "zh-CN,zh;q=0.9",
        }
        time.sleep(random.uniform(1, 2))
        res = requests.get(url, headers=headers, timeout=15)
        res.raise_for_status()
        res.encoding = "utf-8"
        soup = BeautifulSoup(res.text, "html.parser")

        news_list = []
        
        for a in soup.find_all("a", href=True):
            title = a.get_text(strip=True)
            link = a["href"]
            if title and len(title) > 5 and link.startswith("http"):
                if "news" in link or "sina" in link:
                    news_list.append({"title": title, "link": link})
                    if len(news_list) >= 10:
                        break

        if not news_list:
            news_list.append({"title": "未获取到新闻，程序正常运行", "link": "https://news.sina.com.cn/"})
        
        return news_list

    except Exception as e:
        print("抓取异常，返回默认新闻：", e)
        return [{"title": "抓取失败，请检查网络", "link": "https://news.sina.com.cn/"}]

if __name__ == "__main__":
    news = get_top_news()
    for n in news:
        print(n["title"], n["link"])
