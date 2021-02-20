import random
from selenium import webdriver
import time
import pickle


def write_to_file(list):
    with open('films.txt', 'w', encoding='utf-8') as file:
        for el in list:
            file.write(el + '\n')


def get_top_250_films():
    all_films_list = []

    wd = webdriver.Firefox()

    for i in range(1, 6):
        wd.get(f'https://www.kinopoisk.ru/lists/top250/?page={i}&tab=all')
        films = wd.find_elements_by_class_name('selection-film-item-meta__name')

        for el in films:
            all_films_list.append(el.text)
            print(el.text)

        time.sleep(1)

    wd.close()
    write_to_file(all_films_list)


def random_film():

    with open('films.txt', 'r', encoding='utf-8') as file:
        lines = file.read().splitlines()

    index = random.randint(0, len(lines))
    film = lines[index]

    return film


if __name__ == '__main__':
    get_top_250_films()

    data = {
        'a': [1, 2.0, 3, 4 + 6j],
        'b': ("character string", b"byte string"),
    }

    # сохранение в файл
    with open('data.pickle', 'wb') as f:
        pickle.dump(data, f)

    # чтение из файла
    with open('data.pickle', 'rb') as f:
        data_new = pickle.load(f)

    print(data_new)
