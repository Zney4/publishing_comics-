import os
import telegram
from dotenv import load_dotenv
import asyncio
from random import randint, choice
import requests


def get_comics_by_number(number_comics):
    url = f"https://xkcd.com/{number_comics}/info.0.json"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def download_image(comics_number, comics_image, file_path):
    response = requests.get(comics_image["img"])
    response.raise_for_status()
    file_name = f"comic_{comics_number}.png"
    with open(os.path.join(file_path, file_name), "wb") as file:
        file.write(response.content)


async def publishing_comics(chat_id, choice_comics, comics_image):
    await bot.send_document(
        chat_id=chat_id, document=open(os.path.join(file_path, choice_comics), "rb")
    )
    await bot.send_message(chat_id, f'{comics_image["alt"]}')


if __name__ == "__main__":
    load_dotenv()
    bot = telegram.Bot(token=os.environ["TG_TOKEN"])
    chat_id = os.environ["CHAT_ID"]

    file_path = "images"
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    try:
        comics_number = randint(1, 3150)
        comics_image = get_comics_by_number(comics_number)
        download_image(comics_number, comics_image, file_path)
        selection_comics = os.listdir(file_path)
        choice_comics = choice(selection_comics)
        asyncio.run(publishing_comics(chat_id, choice_comics, comics_image))
    finally:
        os.remove(os.path.join(file_path, choice_comics))
