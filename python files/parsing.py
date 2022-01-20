from LinksToClasses import get_links_to_classes
from LinksToCards import cards_of_auto_class
from WorkWithCar import get_characteristic
from UsersEnter import get_users_ask
from WorkWithInfo import *

URL_AUTO_RU = "https://auto.ru/"
HEADER = {
    'User-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
    'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
}


def ready_(ready, i, n):
    if i > n // 10 and ready == 0:
        print("10%")
        return 10
    if i > n // 3 and ready == 10:
        print("30%")
        return 30
    if i > n // 2 and ready == 30:
        print("50%")
        return 50
    if i > 0.8 * n and ready == 50:
        print("80%")
        return 80
    if i > 0.95 * n and ready == 80:
        print("100%")
        return 100
    return ready


def parser():
    # смотрит не все марки - нужно открывать по кнопке. скрипт? / не доступен?
    links_to_classes = get_links_to_classes(URL_AUTO_RU)
    # print(links_to_classes)

    # ввод пользователем характеристик продаваемой машины
    # car_characteristics = get_users_ask()

    start = 0
    # kia
    for link in links_to_classes:
        if link.count("kia"):
            start = links_to_classes.index(link)
            break
    print(links_to_classes)
    for link in links_to_classes[start+1::]:
        print(link)
        links_to_offers = cards_of_auto_class(link)
        n = len(links_to_offers)
        ready = 0
        cars_info = []
        for i in range(n):
            try:
                cars_info += [get_characteristic(links_to_offers[i])]
            except:
                print("sorry")
            ready = ready_(ready, i, n)
            try:
                info_to_csv(cars_info, (link.split('/'))[-3])
            except:
                print("may be next time")


parser()
