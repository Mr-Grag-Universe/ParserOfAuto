from bs4 import BeautifulSoup as bs
import requests


def get_characteristic(url):
    # открытие объявления
    r = requests.get(url)
    r.encoding = 'utf-8'

    # копируем код страницы
    content_of_html_file = r.text
    soup = bs(content_of_html_file, 'html.parser')

    list_of_char = []
    table = []

    price = soup.find("div", "CardHead__price CardHead__topRowRightColumn")
    if price is not None:
        price = price.find("span", "OfferPriceCaption__price")
    if price is not None:
        price = price.text
    table.append(["Цена", price])

    name = soup.find("div", "CardHead__topRowLeftColumn")
    if name is not None:
        name = name.find("h1")
    if name is not None:
        name = name.text
    table.append(["имя", name])

    #if it's a dialler offer
    if soup.find("svg", "IconSvg IconSvg_official-dealer IconSvg_size_48 CardSellerNamePlace__official-dealer-sign") is None:
        # берём элемент, содержащий характеристики машины
        container_with_table = soup.find('div', 'CardOfferBody__leftColumn')
        if container_with_table is None:
            container_with_table = soup.find("ul")
        if container_with_table is None:
            print("Error here")
            return []

        # разбиваем на части
        list_of_char = container_with_table.find_all("li")

        list_of_char = list(map(lambda x: x.find_all("span"), list_of_char))

        # генерируем общую табличку свойств и параметров
        table += [list(map(lambda x: x.text.lower(), list_of_char[i])) for i in range(len(list_of_char))]
    else:
        container_with_table = soup.find("ul", "CardInfoGrouped__list")
        list_of_char = container_with_table.find_all("li")
        for li in list_of_char:
            container = li.find("div", "CardInfoGroupedRow__cellLabel")
            tags = container.find_all("div") + container.find_all("a")
            temp_list = []
            for tag in tags:
                temp_list.append(tag.text.lower())
            table.append(temp_list)

    return table
