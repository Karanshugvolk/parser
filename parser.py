import requests
from bs4 import BeautifulSoup

search = input().replace(" ", "+")
url = f"https://store.steampowered.com/search/?term={search}&supportedlang=russian&ndl=1"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")


games = soup.find_all("div", class_="responsive_search_name_combined")

for game in games:
    title = game.find("span", class_="title").text.strip()
    price = game.find("div", class_="search_price").text.strip()
    discount = game.find("div", class_="search_discount").text.strip()
    index = price.find(".")

    if discount != '':
        print(f"Название: {title} \n Цена без скидки: {price[:index]} \n Скидка: {discount} \n Цена со скидкой: {price[index+1:]}\n")

    else:
        print(
            f"Название: {title} \n Цена без скидки: {price[:index]} \n Скидка: нет \n Цена со скидкой: Цена не изменилась\n")