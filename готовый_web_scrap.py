import requests
from bs4 import BeautifulSoup as bs

flag = True


def get_news():

    url = 'https://ria.ru/'
    r = requests.get(url)
    soup = bs(r.text, 'lxml')
    #print(r.content)

    items = soup.find_all("a", class_='cell-list__item-link color-font-hover-only')
#    print(titles) - выведет список

    news_dict = []

    for index, item in enumerate(items, 1):
        #print(ti["title"])
        item_title = item.get("title")
        item_url = item.get("href")

        #print(f'Номер новости: {index}; заголовок: {item_title}; ссылка: {item_url}')

        news_self = {
            "Номер новости": index,
            "Заголовок новости": item_title,
            "Ссылка на новость": item_url
        }

        news_dict.append(news_self)

    for news in news_dict: #print(news_dict)
        print(f"{news['Номер новости']}: {news['Заголовок новости']}")

    news_num = int(input("Выберите номер новости: "))

    #print(news_dict[news_num-1]["Ссылка на новость"])

    new_link = news_dict[news_num-1]["Ссылка на новость"]

    r = requests.get(new_link)
    soup = bs(r.text, 'lxml')


    news_text = soup.find_all("div", class_="article__text")

    #print(news_text)

    for text in news_text:
        print(text.get_text())

while flag == True:
    get_news()
    num = int(input(f'\nВведите число 1 для закрытия или любое другое для продолжения: '))
    if num == 1:
        break
