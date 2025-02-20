from requests import get
from bs4 import BeautifulSoup


def run_crawler(query):
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = f'https://cn.bing.com/search?q={query}'

    try:
        response = get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        results = []

        for item in soup.select('.b_algo'):
            title = item.select_one('h2').text.strip()
            url = item.select_one('a')['href']
            content = item.select_one('.b_caption > p').text.strip()
            results.append({
                'title': title,
                'url': url,
                'content': content
            })
        return results[:5]
    except Exception as e:
        print(f"Error: {e}")
        return []