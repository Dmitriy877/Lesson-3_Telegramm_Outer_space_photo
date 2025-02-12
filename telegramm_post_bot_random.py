import telegram
import os
from dotenv import load_dotenv
import random
import argparse
from telegramm_post_image import post_image_name


def create_parser():
    parser = argparse.ArgumentParser(
        description="""Данный скрипт принимает в качестве аргумента название 
        картинки в директории images и публикует ее в телеграмм канале, если 
        название файла не указано то публикует случайную картинку из директории 
        images."""
        )
    parser.add_argument('image_name', nargs='?')
    return parser


def post_random_image(token, chat_id, images):
    with open("images/{0}".format(random.choice(images)), "rb") as photo:
        bot = telegram.Bot(token=token)
        bot.send_photo(chat_id=chat_id,
                       photo=photo
                       )

    
def main():
    load_dotenv()
    token = os.environ["TELEGRAMM_API_KEY"]
    chat_id = "@OuterSpacePhoto"
    images = os.listdir(r"images")

    parser = create_parser()
    args = parser.parse_args()

    if args.image_name:
        post_image_name(args.image_name, token, chat_id)
    else:
        post_random_image(token, chat_id, images)


if __name__ == "__main__":
    main()
