import requests


url_list = ["https://younglinux.info/",
            "https://webspoon.ru/",
            "https://www.altx-soft.ru/",
            "http://zetblog.ru/",
            "https://www.sfedu.ru/"]

for url in url_list:
    for i in range(100):
        response = requests.get(url)
        print(f"{i} | {url} | {response}")