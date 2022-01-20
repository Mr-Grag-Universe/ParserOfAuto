import requests
import webbrowser
import time
import random
import re

import pandas as pd
import numpy as np
#import modin.pandas as pd
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

from bs4    import BeautifulSoup



def GetURLs():
    city = "novosibirskaya_oblast"   # Old: sankt-peterburg; ekaterinburg; moskva; sochi; kazan; voronezhskaya_oblast; arhangelskaya_oblast; lipetskaya_oblast;
    # zabaykalskiy_kray; hanty-mansiyskiy_ao; volgograd; altayskiy_kray; magnitogorskmagnitogorsk; murmanskaya_oblast; habarovskiy_kray;
    # krym

    url_HomePage = "https://auto.ru/"+city+"/cars/all/?from=wizard.common&output_type=list&sort=fresh_relevance_1-desc&utm_campaign=common&utm_content=listing&utm_medium=desktop&utm_source=auto_wizard"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
    }

    csvFile = open("hrefs.csv", "a")

    pageNumber  = 1
    hrefCount   = 0
    url         = url_HomePage

    with open('hrefs.csv', 'r') as f:
        hrefCount = sum(1 for _ in f)

    while pageNumber <= 99:                 #hrefCount < 50000 and
        time.sleep(random.uniform(0, 5))

        print("PageNumber: ", pageNumber)

        url = str("https://auto.ru/"+city+"/cars/all/?from=wizard.common&output_type=list&page=" + str(pageNumber) + "&sort=fresh_relevance_1-desc&utm_campaign=common&utm_content=listing&utm_medium=desktop&utm_source=auto_wizard")

        response = requests.get(url, headers=headers)
        response.encoding = response.apparent_encoding
        if response.status_code != 200:
            fname = 'helloworld.html'

            with open(fname, "w", encoding="utf-8") as f:
                f.write(response.text)

            webbrowser.open_new_tab('helloworld.html')

            break
            a = 0

        soup        = BeautifulSoup(response.text, features="lxml")
        tags_a      = soup.find_all("a", class_="Link ListingItemTitle-module__link")
        hrefCount   += len(tags_a)

        if len(tags_a) == 0:
            break

        for elem in tags_a:
            href = elem.get('href')

            csvFile.write(href)
            csvFile.write("\n")
            a = 0

        pageNumber += 1
        a = 0

    csvFile.close()

    return 0;

def GetDataFromTag_li(soup, dfer, i, className, flagConvertValueToDigit = False):
    try:
        tag_li = soup.find_all("li", class_=className)[0]

        name = tag_li.contents[0].get_text()
        value = tag_li.contents[1].get_text()
        value = value.replace(' ', ' ')
        if flagConvertValueToDigit:
            value = value.replace(' ', '')
            value = int(re.sub("\D", "", value))

        #print(name, "=", value, "; ", end='')
        dfer.loc[i, name] = value
    except Exception as e:
         print("Exception=" + str(e), end='; ')

# def GetDataFromTag_Untitled(soup, df, i, tagName, className, flagConvertValueToDigit = False, name=None):
#     tag = soup.find_all(tagName, class_=className)[0]
#
#     # if name == None:
#     #     name = tag.get_text()
#     value = tag.get_text()
#     if flagConvertValueToDigit:
#         value = value.replace(' ', '')
#         value = int(re.sub("\D", "", value))
#
#     print(name, "=", value, "; ", end='')
#     df.loc[i, name] = value


def GetCarsDataFromURL():
   # try:
    df = pd.DataFrame()
    
    offset = 0

    file = open("hrefs.csv", "r")
    
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
    }

    lines = file.readlines()
    lines = lines[offset:]

    with open("headers.txt", 'r') as f:
        header_s = f.readlines()
    header_iter = 0

    header_changer = random.uniform(5, 50)


    profile = webdriver.FirefoxProfile()
    profile.set_preference("general.useragent.override", header['User-Agent'])
    binary = FirefoxBinary('D:/Programming/OpenServer (PHP)/progs/_Internet/FirefoxPortable/App/firefox64/firefox.exe')
    driver = webdriver.Firefox(profile, executable_path='D:/Programming/_Python/___venv/geckodriver.exe',
                               firefox_binary=binary)
    driver.minimize_window()

    for i, line in enumerate(lines):
        header_iter += 1
        if header_iter >= header_changer:
            driver.close()
            header_iter = 0
            header['User-Agent'] = random.choice(header_s)[:-1]
            header_changer = random.uniform(5, 50)

            profile = webdriver.FirefoxProfile()
            profile.set_preference("general.useragent.override", header['User-Agent'])
            binary = FirefoxBinary(
                'D:/Programming/OpenServer (PHP)/progs/_Internet/FirefoxPortable/App/firefox64/firefox.exe')
            driver = webdriver.Firefox(profile, executable_path='D:/Programming/_Python/___venv/geckodriver.exe',
                                       firefox_binary=binary)
            driver.minimize_window()
            a = 0
        try:
            time.sleep(int(random.uniform(0, 4))+1)

            url = line[:-1]
            try:
                # response = requests.get(url, headers=header)
                # response.encoding = response.apparent_encoding


                # randick = random.randint(0, 6)
                # if randick==0 or randick==1:
                #     driver = webdriver.Firefox(profile)
                # if randick==2:
                #     driver = webdriver.Chrome(profile)
                # if randick==3:
                #     driver = webdriver.Safari(profile)
                # if randick>=4:
                #     driver = webdriver.Opera(profile)


                driver.get(url=url)
                html = driver.page_source

                # if response.status_code != 200:
                #     print("Code = ", response.status_code)
                #
                #     fname = 'helloworld.html'
                #
                #     with open(fname, "w", encoding="utf-8") as f:
                #         f.write(response.text)
                #
                #     webbrowser.open_new_tab('helloworld.html')
                #
                #     break
                #     a = 0

                #soup = BeautifulSoup(response.text, features="lxml")
                soup = BeautifulSoup(html, features="lxml")
                tag_span_price = soup.find_all("span", class_="OfferPriceCaption__price")
            except Exception as e:
                print(e)
                continue

            if len(tag_span_price) == 0:
                continue
            try:
                price = tag_span_price[0].get_text()
                if price == "" or price == None:
                    continue
                price = price.replace(' ', '')
                price = int(re.sub("\D", "", price))
            except Exception as e:
                continue

            print(str(i+offset) + ". ", end="")

            print("Price=", price, "; ", end='')
            df.loc[i, "цена"] = price

            if len(soup.find_all("li", class_="CardInfoRow CardInfoRow_year")) != 0:
                GetDataFromTag_li(soup=soup, dfer=df, i=i, className="CardInfoRow CardInfoRow_year",          # Год
                                  flagConvertValueToDigit=False)
                GetDataFromTag_li(soup=soup, dfer=df, i=i, className="CardInfoRow CardInfoRow_kmAge",         # Пробег
                                  flagConvertValueToDigit=True)
                GetDataFromTag_li(soup=soup, dfer=df, i=i, className="CardInfoRow CardInfoRow_bodytype",      # Кузов
                                  flagConvertValueToDigit=False)
                GetDataFromTag_li(soup=soup, dfer=df, i=i, className="CardInfoRow CardInfoRow_color",         # Цвет
                                  flagConvertValueToDigit=False)
                GetDataFromTag_li(soup=soup, dfer=df, i=i, className="CardInfoRow CardInfoRow_engine",        # Двигатель
                                  flagConvertValueToDigit=False)
                GetDataFromTag_li(soup=soup, dfer=df, i=i, className="CardInfoRow CardInfoRow_transmission",  # Коробка
                                  flagConvertValueToDigit=False)
                GetDataFromTag_li(soup=soup, dfer=df, i=i, className="CardInfoRow CardInfoRow_drive",         # Привод
                                  flagConvertValueToDigit=False)
                GetDataFromTag_li(soup=soup, dfer=df, i=i, className="CardInfoRow CardInfoRow_wheel",         # Руль
                                  flagConvertValueToDigit=False)
                GetDataFromTag_li(soup=soup, dfer=df, i=i, className="CardInfoRow CardInfoRow_state",         # Состояние
                                  flagConvertValueToDigit=False)
                GetDataFromTag_li(soup=soup, dfer=df, i=i, className="CardInfoRow CardInfoRow_ownersCount",   # Владельцы
                                  flagConvertValueToDigit=False)
                GetDataFromTag_li(soup=soup, dfer=df, i=i, className="CardInfoRow CardInfoRow_pts",           # ПТС
                                  flagConvertValueToDigit=False)
                GetDataFromTag_li(soup=soup, dfer=df, i=i, className="CardInfoRow CardInfoRow_customs",       # Таможня
                                  flagConvertValueToDigit=False)
                GetDataFromTag_li(soup=soup, dfer=df, i=i, className="CardInfoRow CardInfoRow_transportTax",  # Налог
                                  flagConvertValueToDigit=False)
            else:
                try:
                    tag = soup.find_all("div", class_="LayoutSidebar__content")[0].contents[0].contents[2]
                    tag = tag.contents[1].contents[0].contents[1].contents[0]

                    name = "год выпуска"
                    value = tag.get_text()
                    value = value.replace(' ', ' ')

                    #print(name, "=", value, "; ", end='')
                    df.loc[i, name] = value
                except Exception as e:
                    print("Exception=" + str(e), end='; ')
                # ----------------------------------------------------------------------------------------------------------
                tag = soup.find_all("div", class_="CardInfoGrouped__cellLabel")

                for elem in tag:
                    part = elem.contents

                    name = part[0].get_text()
                    value = part[1].get_text()
                    value = value.replace(' ', ' ')

                    #print(name, "=", value, "; ", end='')
                    df.loc[i, name] = value
                # ----------------------------------------------------------------------------------------------------------
                name = "Пробег"
                value = 0

                #print(name, "=", value, "; ", end='')
                df.loc[i, name] = value

                b = 0

            print("")
            df.fillna("-")
            df.to_csv("data.csv", index=False, sep=';', encoding='utf-8')
        except Exception as e:
            continue
        # pd.options.display.max_rows = 100
        # pd.options.display.max_columns = 100
        # print(df.head())
        # if i > 20:
        #     df.to_csv("data.csv", index=False, sep=';', encoding='utf-8')
        #
        #     b = 0
        a = 0
    # except Exception as e:
    #     print("\nException " + str(e))
    driver.close()
    df.fillna("-")
    df.to_csv("data.csv", index=False, sep=';', encoding='utf-8')
    file.close()
    return 0


if __name__ == '__main__':
    # GetURLs()
    GetCarsDataFromURL()


