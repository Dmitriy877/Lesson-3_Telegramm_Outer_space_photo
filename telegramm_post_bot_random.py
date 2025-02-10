import telegram
import os
from dotenv import load_dotenv
import random
import argparse


images = os.listdir(r"images")


def create_parser():
    parser = argparse.ArgumentParser(
        description="""Данный скрипт принимает в качестве аргумента название 
        картинки в директории images и публикует ее в телеграмм канале, если 
        название файла не указано то публикует случайную картинку из директории 
        images."""
        )
    parser.add_argument('image_name', nargs='?')
    return parser


def post_image_name(entered_value, token, chat_id):
    bot = telegram.Bot(token=token)
    bot.send_photo(chat_id=chat_id,
                   photo=open("images/{0}".format(entered_value),
                              "rb"))


def post_random_image(token, chat_id):
    bot = telegram.Bot(token=token)
    bot.send_photo(chat_id=chat_id,
                   photo=open("images/{0}".format(random.choice(images)),
                              "rb"))

    
def main():
    load_dotenv()
    token = os.environ["TELEGRAMM_API_KEY"]
    chat_id = "@OuterSpacePhoto"

    parser = create_parser()
    entered_value = parser.parse_args()

    if entered_value.image_name:
        post_image_name(entered_value.image_name, token, chat_id)
    else:
        post_random_image(token, chat_id)  


if __name__ == "__main__":
    main()
