# 作者: 大数据 浪哥
# 2025年06月12日01时17分12秒
# 1054074422@qq.com
#帮# 安装所需的库
# pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup

def fetch_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # 如果响应状态码不是200，引发HTTPError异常
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def extract_titles(html):
    soup = BeautifulSoup(html, 'html.parser')
    titles = soup.find_all('h1')  # 假设我们要抓取所有h1标签
    return [title.get_text() for title in titles]

def main():
    url = 'https://example.com'  # 替换为你想要抓取的网页URL
    html_content = fetch_page(url)
    if html_content:
        titles = extract_titles(html_content)
        for title in titles:
            print(title)

if __name__ == "__main__":
    main()

