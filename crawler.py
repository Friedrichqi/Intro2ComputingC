import requests
from bs4 import BeautifulSoup

content = ""
for chapter in range(1, 11):
    url = f"https://www.shicimingju.com/book/xiyouji/{chapter}.html"  # 需要爬取的网址
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'
    }
    r = requests.get(url, headers=headers, timeout=30)  # 获取网页的内容，并返回给r变量，timeout为超时时间
    r.encoding = r.apparent_encoding  # 统一编码方式
    file = open(f'XYJ_Chapter{chapter}.html', 'w', encoding='utf-8')
    file.write(r.text)
    file.close()

    soup = BeautifulSoup(r.text, 'html.parser')
    
    title = soup.find("h1", class_ = "bt")
    print(title.text)
    content += title.text + '\n'

    div_text = soup.find("div", class_ = "text p_pad")
    paragraphs = div_text.find_all('p')
    for p in paragraphs:
        print(p.text)
        content += p.text + '\n'
    
file = open('XYJ.txt', 'w', encoding='utf-8')
file.write(content)
file.close()