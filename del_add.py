import csv
import os
from _csv import writer
from csv import reader, DictReader
from os.path import exists


def creating():
    file = 'phone.csv'
    with open(file, 'w', encoding='utf-8') as data:
        data.write(f'Фамилия,Имя,Номер\n')


def writing_csv(info):
    file = 'phone.csv'
    with open(file, 'a', encoding='utf-8') as data:
        data.write(f'{info[0]},{info[1]},{info[2]}\n')


def reading_csv(file):
    # возвращает данные в виде строки
    # with open(file, encoding='utf-8') as data:
    # content = data.read()
    # return content

    # возвращает данные в виде списка
    #with open(file, encoding='utf-8') as data:
        #res = list(reader(data))
    #return res

    with open(file, encoding='utf-8') as data:
        res = list(DictReader(data))
    return res


def get_info():
    info = []
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    info.append(last_name)
    info.append(first_name)
    phone_number = ''
    flag = False
    while not flag:
        try:
            phone_number = input("Введите номер: ")
            if len(phone_number) != 11:
                print("В номере должно быть 11 цифр")
            else:
                phone_number = int(phone_number)
                flag = True

        except:
            print("В номере должны быть только цифры")

    info.append(phone_number)
    return info


def record_info():
    info = get_info()
    writing_csv(info)


#record_info()

def delete_info():
    last_name = input("Введите фамилию для удаления: ")
    first_name = input("Введите имя для удаления: ")
    phone_number = input("Введите номер для удаления: ")

    file = 'phone.csv'
    rows = []

    with open(file, 'r', encoding='utf-8') as data:
        csv_reader = reader(data)
        rows = list(csv_reader)

    with open(file, 'w', encoding='utf-8') as data:
        csv_writer = writer(data)
        for row in rows:
            if row[0] != last_name or row[1] != first_name or row[2] != phone_number:
                csv_writer.writerow(row)

    print("Данные удалены успешно.")

def update_info():
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")


    file = 'phone.csv'
    temp_file = 'temp.csv'
    updated = False

    with open(file, 'r', encoding='utf-8') as data, open(temp_file, 'w', encoding='utf-8', newline='') as temp_data:
        csv_reader = csv.reader(data)
        rows = list(csv_reader)
        csv_writer = csv.writer(temp_data)

        for row in rows:
            if row[0] == last_name and row[1] == first_name:
                row[0] = input("Введите новую фамилию: ")
                row[1] = input("Введите новое имя: ")
                row[2] = input("Введите новый номер: ")
                updated = True
            csv_writer.writerow(row)

    if updated:
        os.remove(file)
        os.rename(temp_file, file)
        print("User успешно обновлен.")
    else:
        print("Данные не найдены. User не может быть обновлен.")


def view():
    print(reading_csv('phone.csv'))


#view()



def main():
    while True:
        step = input("Введите действие: ")
        if step == 'q':
            break
        elif step == 'w':
            path = 'phone.csv'
            flag = exists(path)
            if not flag:
                creating()
                record_info()
            else:
                record_info()
        elif step == 'd':
            delete_info()
        elif step == 'u':
            update_info()
        elif step == 'r':
            view()

main()