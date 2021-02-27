import random
from selenium import webdriver
import time
import pickle


def write_to_file(data):
    with open('data.pickle', 'wb') as f:
        pickle.dump(data, f)


def get_top_250_films():
    films_dic = {}

    wd = webdriver.Firefox()

    for i in range(1, 6):
        wd.get(f'https://www.kinopoisk.ru/lists/top250/?page={i}&tab=all')
        films = wd.find_elements_by_class_name('selection-film-item-meta__link')
        films_hrefs = []


        for el in films:
            films_hrefs.append(el.get_attribute('href'))
        for el in films_hrefs:
            wd.get(el)
            time.sleep(1)
            film_name = wd.find_element_by_class_name('styles_title__2l0HH').text
            img = wd.find_element_by_class_name('film-poster').get_attribute('src')
            film_description = wd.find_element_by_class_name('styles_paragraph__2Otvx').text

            films_dic[film_name] = [img, film_description]




    wd.close()

    write_to_file(films_dic)


def random_film():
    with open('data.pickle', 'rb') as f:
        data = pickle.load(f)

    index = random.randint(0, 249)

    film_name = list(data.keys())[index]
    poster = data[film_name][0]
    description = data[film_name][1]

    return [film_name, poster, description]



if __name__ == '__main__':
   get_top_250_films()