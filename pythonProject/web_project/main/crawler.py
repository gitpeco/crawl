# main/crawler.py
import requests
from bs4 import BeautifulSoup


def run_crawler(query):
    # 示例爬虫（以百度搜索为例）
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = f'https://www.baidu.com/s?wd={query}'

    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        results = []

        for item in soup.select('.result'):
            title = item.select_one('h3').text.strip()
            link = item.select_one('a')['href']
            content = item.select_one('.c-abstract').text.strip()
            results.append({
                'title': title,
                'url': link,
                'content': content
            })
        return results[:5]  # 返回前5条结果
    except Exception as e:
        print(f"爬虫错误: {e}")
        return []