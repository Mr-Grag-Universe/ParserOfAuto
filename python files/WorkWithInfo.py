import csv
import pandas as pd
import numpy as np
from InfoPreparetion import info_preparation
# -*- coding: utf-8 -*-


def table_to_dictionris(table):
    pass

'''
def info_to_csv(all_cars_info):
    with open("info.csv", "w", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter="\t", lineterminator="\r")
        writer.writerow(["Параметр", "Характеристика"])
        for table in all_cars_info:
            for line in table:
                writer.writerow(line)
            #writer.writerows(table)


def temp_file(all_tables):
    print("Hello")
    #print(all_tables)
    f = open("results.txt", 'w')
    f.close()
    f = open("results.txt", 'a', encoding="utf-8")
    for table in all_tables:
        for line in table:
            for word in line:
                word1 = str(word)
                f.write(word1 + ' ')
            f.write('\n')
        f.write('\n')
    f.close()
'''


def info_to_csv(all_cars_info, mark):
    '''
    header = []#['Марка']
    for i in range(len(all_cars_info)):
        for j in range(len(all_cars_info[i])):
            if not all_cars_info[i][j]:
                all_cars_info = all_cars_info[i][:j:] + all_cars_info[i][j+1::]
                j -= 1
                print("empty")
                #print(all_cars_info[i])
                continue
            if header.count(all_cars_info[i][j][0]) == 0:
                header.append(all_cars_info[i][j][0])
            if len(all_cars_info[i][j]) > 2:
                #print(all_cars_info[i][j])
                if all_cars_info[i][j][0] == 'Комплектация':
                    pass
                elif all_cars_info[i][j][0] == 'Двигатель':
                    pass
                elif all_cars_info[i][j][0] == 'Налог':
                    all_cars_info[i][j][1] = all_cars_info[i][j][3]
                else:
                    print(all_cars_info[i][j])
                all_cars_info[i][j] = [all_cars_info[i][j][0], all_cars_info[i][j][1]]
            elif len(all_cars_info[i][j]) < 2:
                all_cars_info[i][j] = [all_cars_info[i][j][0], '']

    for i in range(len(all_cars_info)):
        for j in range(len(all_cars_info[i])):
            #print(all_cars_info[i][j])
            if all_cars_info[i][j][0] == 'Цена':
                if all_cars_info[i][j][1] is None:
                    all_cars_info[i][j][1] = '0'
                    continue
                elif all_cars_info[i][j][1] != '0':
                    price = all_cars_info[i][j][1]
                    new_price = price.split(" ")
                    if 'от' in new_price[0]:
                        new_price = new_price[1::]
                    if new_price[-1] == "₽":
                        new_price = new_price[:-1:]
                    price = ""
                    for a in new_price:
                        price += a
                    all_cars_info[i][j][1] = price
            if all_cars_info[i][j][0] == 'Пробег':
                if all_cars_info[i][j][1] is None:
                    all_cars_info[i][j][1] = '0'
                    continue
                elif all_cars_info[i][j][1] != '0':
                    run = all_cars_info[i][j][1]
                    new_price = run.split(" ")
                    run = ""
                    for a in new_price:
                        if a.isdigit():
                         run += a
                    all_cars_info[i][j][1] = run
            while "\xa0" in all_cars_info[i][j][0]:
                all_cars_info[i][j][0] = all_cars_info[i][j][0].replace(" ", ' ')
                #print(all_cars_info[i][j])

            while "\xa0" in all_cars_info[i][j][1]:
                all_cars_info[i][j][1] = all_cars_info[i][j][1].replace(" ", ' ')
                break

    #print(all_cars_info)
    '''

    header, all_cars_info = info_preparation(all_cars_info)

    # print(header, all_cars_info)

    df = pd.DataFrame()
    # print(header)
    df.append(header, ignore_index=True)
    # print(header)

    if len(header) == 9:
        print("Error")

    for table in all_cars_info:
        params = {}
        for h in header:
            l = len(params)
            for line in table:
                if len(line) < 2:
                    break
                if line[0].lower() == h:
                    # params.append(:line[1])
                    params[h] = line[1]
                    break
            if l == len(params):
                # params.append('')
                params[h] = ''
        # print(params)
        df = df.append(params, ignore_index=True)

    # print(df)
    file_name = f"спаршенные марки/data_{mark}.csv"
    df.to_csv(file_name, index=False, sep=';', encoding='utf-8')
