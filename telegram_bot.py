import os
import telegram
from dotenv import load_dotenv
import asyncio
from random import randint
import random
import requests


def get_random_comics(random_number):
    url = f"https://xkcd.com/{random_number}/info.0.json"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def downloading_random_image(random_number, random_photo, directory_image):
    response = requests.get(random_photo["img"])
    response.raise_for_status()
    filename_random = f"comics{random_number}.png"
    with open(os.path.join(directory_image, filename_random), "wb") as file:
        file.write(response.content)


async def public_comics(chat_id, random_file, random_photo):
    await bot.send_document(
        chat_id=chat_id, document=open(os.path.join(directory_image, random_file), "rb")
    )
    await bot.send_message(chat_id, f'{random_photo["alt"]}')

if __name__ == "__main__":
    load_dotenv()
    if not os.path.exists("image"):
        os.makedirs("image")
    random_number = randint(1, 3150)
    random_photo = get_random_comics(random_number)
    directory_image = "image"
    downloading_random_image(random_number, random_photo, directory_image)

    directory = os.listdir("image/")
    bot = telegram.Bot(token=os.environ["TG_TOKEN"])
    chat_id = os.environ["CHAT_ID"]
    random_file = random.choice(directory)
    asyncio.run(public_comics(chat_id, random_file, random_photo))
    os.remove(os.path.join(directory_image, random_file))
