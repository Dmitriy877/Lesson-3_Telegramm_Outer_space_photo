import telegram
import os
from dotenv import load_dotenv
import random
import argparse
load_dotenv()


token = os.environ["TELEGRAMM_API_KEY"]
chat_id = "@OuterSpacePhoto"
images_list = os.listdir(r"images")


def create_parser():
    parser = argparse.ArgumentParser(
        description="""Данный скрипт принимает в качестве аргумента название 
        картинки в директории images и публикует ее в телеграмм канале, если 
        название файла не указано то публикует случайную картинку из директории 
        images."""
        )
    parser.add_argument('image_name', nargs='?')
    return parser


def post_image_name(entered_value):
    bot = telegram.Bot(token=token)
    bot.send_photo(chat_id=chat_id,
                   photo=open("images/{0}".format(entered_value),
                              "rb"))


def post_random_image():
    bot = telegram.Bot(token=token)
    bot.send_photo(chat_id=chat_id,
                   photo=open("images/{0}".format(random.choice(images_list)),
                              "rb"))

    
def main():

    parser = create_parser()
    entered_value = parser.parse_args()

    if entered_value.image_name:
        post_image_name(entered_value.image_name)
    else:
        post_random_image()  


if __name__ == "__main__":
    main()
