import os
from dotenv import load_dotenv
import random
import argparse
from telegramm_post_image import post_image


def create_parser():
    parser = argparse.ArgumentParser(
        description="""Данный скрипт принимает в качестве аргумента название 
        картинки в директории images и публикует ее в телеграмм канале, если 
        название файла не указано то публикует случайную картинку из директории 
        images."""
        )
    parser.add_argument('image_name', nargs='?')
    return parser


def main():
    load_dotenv()
    token = os.environ["TELEGRAMM_API_KEY"]
    chat_id = os.environ["TELEGRAMM_CHAT_ID"]
    random_image = random.choice(os.listdir(r"images"))

    parser = create_parser()
    args = parser.parse_args()

    if args.image_name:
        post_image(args.image_name, token, chat_id)
    else:

        post_image(random_image, token, chat_id)


if __name__ == "__main__":
    main()
