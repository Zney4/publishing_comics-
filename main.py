import requests
import pprint
from random import randint
import os


def check_file():
    if not os.path.exists("image"):
        os.makedirs("image")

def get_comics(filename):
    url = "https://xkcd.com/353/info.0.json"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def get_random_comics(random_name):
    url = f"https://xkcd.com/{random_name}/info.0.json"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def downloading_random_image(random_name, random_photo):
    response = requests.get(random_photo['img'])
    response.raise_for_status()
    filename_random = f"comics{random_name}.png"
    with open(f"image/{filename_random}", "wb") as file:
        file.write(response.content)


def downloading_image(get_info, filename):
    response = requests.get(get_info['img'])
    response.raise_for_status()


    with open(f"image/{filename}", "wb") as file:
        file.write(response.content)


def comments_avtor(get_info):
    print(get_info['alt'])


if __name__ == "__main__":
    check_file()
    random_name = randint(1, 3150)
    filename = "comics.png"
    get_info = get_comics(filename)
    downloading_image(get_info, filename)
    comments_avtor(get_info)
    random_photo = get_random_comics(random_name)
    downloading_random_image(random_name, random_photo)