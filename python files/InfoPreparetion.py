def info_preparation(all_cars_info):
    header = []
    # убираем лишние колонки, перенося из лишних столбцов информацию
    for i in range(len(all_cars_info)):
        len_ = len(all_cars_info[i])
        for j in range(len_):
            try:
                if len(all_cars_info[i][j]) > 2:
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

                if header.count(all_cars_info[i][j][0].lower()) == 0:
                    if all_cars_info[i][j][0] == 'Двигатель':
                        if header.count('Топливо') == 0:
                            header.append('Объём двигателя')
                            header.append('Лошадиные силы')
                            header.append('Топливо')
                    else:
                        header.append(all_cars_info[i][j][0].lower())

            except IndexError:
                if not all_cars_info[i]:
                    continue
                '''if len(all_cars_info[i]) == 0:
                    continue
                if not all_cars_info[i][j]:
                    all_cars_info = all_cars_info[i][:j:] + all_cars_info[i][j + 1::]
                    j -= 1
                    len_ -= 1
                    print("empty")
                    # print(all_cars_info[i])
                    continue'''
                print("IndexError1")

    for i in range(len(all_cars_info)):
        for j in range(len(all_cars_info[i])):
            try:
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

                if all_cars_info[i][j][0] == 'Налог':
                    if all_cars_info[i][j][1] is None:
                        all_cars_info[i][j][1] = '0'
                        continue

                    elif all_cars_info[i][j][1] != '0':
                        tax = all_cars_info[i][j][1]
                        new_price = tax.split(" ")
                        tax = ""
                        for a in new_price:
                            if a.isdigit():
                                tax += a
                        all_cars_info[i][j][1] = tax

                if all_cars_info[i][j][0] == 'Владельцы':
                    if all_cars_info[i][j][1] is None:
                        all_cars_info[i][j][1] = '0'
                        continue

                    elif all_cars_info[i][j][1] != '0':
                        owners = all_cars_info[i][j][1]
                        new_price = owners.split(" ")
                        owners = ""
                        for a in new_price:
                            if a.isdigit():
                                owners += a
                        all_cars_info[i][j][1] = owners

                if all_cars_info[i][j][0] == 'Двигатель':
                    if all_cars_info[i][j][1] is None:
                        #all_cars_info[i][j][1] = '0'
                        continue

                while "\xa0" in all_cars_info[i][j][0]:
                    all_cars_info[i][j][0] = all_cars_info[i][j][0].replace(" ", ' ')
                    break

                while "\xa0" in all_cars_info[i][j][1]:
                    all_cars_info[i][j][1] = all_cars_info[i][j][1].replace(" ", ' ')
                    break

            except IndexError:
                print("IndexError")

    for i in range(len(all_cars_info)):
        for j in range(len(all_cars_info[i])):
            try:
                if all_cars_info[i][j][0] == 'Двигатель':
                    char = all_cars_info[i][j][1].split(' ')
                    all_cars_info[i] = all_cars_info[i][:j:] + all_cars_info[i][j+1::]
                    all_cars_info[i].append(['Объём двигателя', ''])
                    all_cars_info[i].append(['Лошадиные силы', ''])
                    all_cars_info[i].append(['Топливо', ''])
                    if not char:
                        break
                    all_cars_info[i][-1][1] = char[-1]
                    all_cars_info[i][-2][1] = char[3]
                    all_cars_info[i][-3][1] = char[0]
                    # print(all_cars_info[i])
                    break
            except IndexError:
                print("Error")

    for i in range(len(header)):
        header[i] = header[i].lower()

    return header, all_cars_info
