import os
import telegram
from dotenv import load_dotenv
import asyncio
import random


async def comics_public(chat_id, random_file):
    await bot.send_document(
        chat_id=chat_id, document=open(f"image/{random_file}", "rb")
    )


if __name__ == "__main__":
    load_dotenv()
    directory = os.listdir("image/")
    bot = telegram.Bot(token=os.environ["BOT_TOKEN"])
    chat_id = os.environ["CHAT_ID"]
    random_file = random.choice(directory)
    asyncio.run(comics_public(chat_id, random_file))
    os.remove(f"image/{random_file}")
