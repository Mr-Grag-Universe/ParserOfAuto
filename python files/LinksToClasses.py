from bs4 import BeautifulSoup as bs
import requests


def links_to_classes_to_file(links_to_classes):
    file = open("links_to_classes.txt", 'w')
    for link in links_to_classes:
        file.write(link+'\n')


def get_links_to_classes(url):
    # слизываем страничку по ссылке
    r = requests.get(url)
    # меняем кодировку, чтобы абракадабры не получить вместо русского текста
    r.encoding = 'utf-8'

    # удостоверимся, что всё прошло успешно (статус https)

    # считываем текст со странички
    content_of_html_file = r.text

    # создаём объект soup класса BeautiSoup через который будет осуществляться работа с кодом страницы
    soup = bs(content_of_html_file, 'html.parser')

    # нужен весь список марок с их ссылками
    # но нужны лишь те, у которых есть объявления

    # извлечение массива ссылок на категории автомобилей
    links_to_classes = soup.find_all("a", "IndexMarks__item")
    links_to_classes = list(map(lambda x: x['href'], links_to_classes))

    #print(links_to_classes)

    # print(links_to_classes)
    links_to_classes_to_file(links_to_classes)
    return links_to_classes
