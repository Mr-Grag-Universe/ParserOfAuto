from bs4 import BeautifulSoup as bs
import requests


def cards_of_auto_class(url):
    r = requests.get(url)
    r.encoding = 'utf-8'
    #print(r.status_code)

    cards_class = "Button Button_color_white Button_size_s Button_type_link Button_width_default ListingPagination__next"


    content_of_html_file = r.text
    soup = bs(content_of_html_file, 'html.parser')

    # если остались ещё страницы
    # задание ссылки на следующую страничку
    next_page = soup.find("a", cards_class)
    if next_page is None:
        next_page = soup.find_all("a", "Button Button_color_white Button_size_s Button_type_link Button_width_default ListingPagination__next")
    next_page = next_page['href']
    #print(next_page)

    # ограничитель для перелистывания страниц
    last_page = soup.find_all('a', "Button Button_color_whiteHoverBlue Button_size_s Button_type_link Button_width_default ListingPagination__page")
    last_page = last_page[-1]
    last_page = last_page.find('span', 'Button__text')
    last_page = last_page.text

    links_to_cards = []

    #print(next_page[-2::], end=' ')

    if next_page[-2::] != '=5': #last_page:
        temp = soup.find_all("a", 'Link OfferThumb')

        temp = list(map(lambda x: x['href'], temp))

        links_to_cards += temp
        links_to_cards += cards_of_auto_class(next_page)
    else:
        temp = soup.find_all("a", 'Link OfferThumb')
        links_to_cards += list(map(lambda x: x['href'], temp))

    return links_to_cards
