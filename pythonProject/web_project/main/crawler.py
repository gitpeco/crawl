# main/crawler.py
import requests
from bs4 import BeautifulSoup


def run_crawler(query):
    if not query:
        return []

    headers = {'User-Agent': 'Mozilla/5.0'}
    url = f'https://www.example.com/search?q={query}'  # 替换为其他搜索引擎的 URL

    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        results = []

        for item in soup.select('.result'):  # 根据目标网站的 HTML 结构调整选择器
            title = item.select_one('h3').text.strip()
            link = item.select_one('a')['href']
            content = item.select_one('.content').text.strip()
            results.append({
                'title': title,
                'url': link,
                'content': content
            })
        return results[:5]  # 返回前5条结果
    except Exception as e:
        print(f"爬虫错误: {e}")
        return []